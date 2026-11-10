"""定时抓取百度热搜并发送到邮箱（GitHub Actions 版）。

所有敏感信息都从环境变量读取，源码里不再出现任何凭据：
    MAIL_USER  发件邮箱
    MAIL_PASS  邮箱 SMTP 授权码
    MAIL_TO    收件人列表，多个地址用英文逗号分隔
"""

import os
import smtplib
import sys
import urllib.parse
from datetime import datetime
from email.mime.text import MIMEText
from email.utils import formataddr

import requests
from lxml import etree

BAIDU_URL = "https://top.baidu.com/board?tab=realtime"
MAX_ITEMS = 30

HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/113.0.0.0 Safari/537.36"
    )
}

# 保留原来的两组 XPath，但改为逐条容错：
# 百度页面结构或条目数变化时跳过该条，而不是让整个任务抛 IndexError。
TITLE_XPATH = "/html/body/div/div/main/div[2]/div/div[2]/div[{i}]/div[2]/a/div[1]"
LINK_XPATH = "/html/body/div/div/main/div[2]/div/div[2]/div[{i}]/a"


def get_credentials():
    """从环境变量读取凭据，缺失时明确报错，避免静默失败。"""

    def required(key):
        value = os.environ.get(key, "").strip()
        if not value:
            raise RuntimeError(
                f"缺少环境变量 {key}，请在仓库 Settings → Secrets and variables → Actions 中配置"
            )
        return value

    sender = required("MAIL_USER")
    password = required("MAIL_PASS")
    receivers = [
        addr.strip() for addr in required("MAIL_TO").split(",") if addr.strip()
    ]
    if not receivers:
        raise RuntimeError("MAIL_TO 中没有有效的收件人地址")
    return sender, password, receivers


def fetch_hot_list():
    """抓取热搜列表，返回 [(标题, 链接), ...]。"""
    response = requests.get(BAIDU_URL, headers=HEADERS, timeout=20)
    if response.status_code != 200:
        raise RuntimeError(f"请求百度热搜失败，状态码 {response.status_code}")

    html = etree.HTML(response.text)
    if html is None:
        raise RuntimeError("热搜页面解析失败")

    items = []
    for i in range(1, MAX_ITEMS + 1):
        titles = html.xpath(TITLE_XPATH.format(i=i))
        links = html.xpath(LINK_XPATH.format(i=i))
        if not titles or not links:
            continue
        title = (titles[0].text or "").strip()
        href = links[0].get("href") or ""
        if not title:
            continue
        items.append((title, urllib.parse.unquote(href)))

    if not items:
        # 宁可让任务失败报警，也不要发一封空邮件。
        raise RuntimeError(
            "一条热搜都没抓到，很可能是百度页面改版了，请检查 XPath 后重试"
        )
    return items


def build_message(items, sender, receivers):
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    lines = [f"百度最新热榜排行 {BAIDU_URL}", ""]
    for idx, (title, link) in enumerate(items, 1):
        lines.append(f"百度热搜第【{idx}】")
        lines.append(f"《{title}》")
        lines.append(link)
        lines.append("")

    msg = MIMEText("\n".join(lines), "plain", "utf-8")
    msg["Subject"] = f"百度最新热榜消息 - {now}"
    msg["From"] = formataddr(("百度热点消息排行榜", sender))
    msg["To"] = ",".join(receivers)
    return msg


def send_email():
    sender, password, receivers = get_credentials()
    items = fetch_hot_list()
    msg = build_message(items, sender, receivers)

    # QQ 邮箱推荐 465 + SSL；587 + STARTTLS 在部分 CI 网络环境下会被拦截。
    with smtplib.SMTP_SSL("smtp.qq.com", 465, timeout=20) as smtp:
        smtp.login(sender, password)
        smtp.sendmail(sender, receivers, msg.as_string())

    print(f"发送成功：{len(items)} 条热搜，{len(receivers)} 位收件人")


if __name__ == "__main__":
    try:
        send_email()
    except Exception as exc:
        print(f"发送失败: {exc}", file=sys.stderr)
        sys.exit(1)
