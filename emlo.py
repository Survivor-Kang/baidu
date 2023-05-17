import requests
from lxml import etree
import urllib.parse
import smtplib
from email.mime.text import MIMEText
from email.utils import formataddr
from datetime import datetime
def send_email():
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36'
    }
    url = 'https://top.baidu.com/board?tab=realtime'
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        html = etree.HTML(response.text)
        content = ""
        oo = 1
        while oo <= 30:
            elements = html.xpath(f'/html/body/div/div/main/div[2]/div/div[2]/div[{oo}]/div[2]/a/div[1]')[0]
            elements2 = html.xpath(f'/html/body/div/div/main/div[2]/div/div[2]/div[{oo}]/a')[0]
            decoded = urllib.parse.unquote(elements2.get("href"))
            content += f"百度热搜第【{oo}】\n《{elements.text}》\n'{decoded}'\n"
            oo += 1
        # 构建邮件正文
        current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        subject = f'百度最新热榜消息 - {current_time}'  # 在主题中添加当前时间
        body = f'百度最新热榜排行{url}\n,{content}'
        # 发送邮件
        sender_email = '2235442745@qq.com' # 发件人邮箱地址
        sender_password = 'ajscperiywiodhgd'  # 发件人邮箱授权码或密码
        receiver_emails = ['2448266898@qq.com', '2547852798@qq.com', 'rngming@qq.com', '1602318741@qq.com',
                           '179194516@qq.com', '1961545128@qq.com', '2273074374@qq.com']  # 收件人邮箱地址
        msg = MIMEText(body)
        msg['Subject'] = subject
        msg['From'] = formataddr(('百度热点消息排行榜', sender_email))
        msg['To'] = ','.join(receiver_emails)
        try:
            with smtplib.SMTP('smtp.qq.com', 587) as smtp:
                smtp.starttls()
                smtp.login(sender_email, sender_password)
                smtp.send_message(msg)
            print("发送成功")
        except Exception as e:
            print("发送失败:", str(e))
    else:
        print('请求失败，状态码为', response.status_code)
send_email()
