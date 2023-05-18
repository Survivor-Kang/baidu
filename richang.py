import requests
BV='BV1Jd4y1Z7TG'#需要的
cookies = {
    'sec': '33d14def5e17fd8100859a98868e5bf045b7aacd',
    's_ac': '%5B%22288feed2%22%2C%22ae17b59f%22%2C%220fcfa91f%22%2C%2254a622fb%22%2C%227c4b5fc1%22%2C%22227321dc%22%2C%22f9c28630%22%2C%228364e5ba%22%2C%221cbfe789%22%2C%22f657a60f%22%5D',
    'NM-TOKEN': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyaWQiOjEwMDIyLCJ1c2VybmFtZSI6InBlbmdqaWFuZ2NodW4iLCJvdXRUaW1lIjoxNjg0NTM3NzU1LCJncm91cCI6Ik1lbWJlciIsImV4cCI6MTY4NDY2NzM1NSwiaXNzIjoiYmlyZCJ9.NFxHazi_j6JGgT8nbH_DpQ_w7sFx1j6Ps6guF2qU79c',
    'u_tk': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyaWQiOjEwMDIyLCJ1c2VybmFtZSI6InBlbmdqaWFuZ2NodW4iLCJvdXRUaW1lIjoxNjg0NTM3NzU1LCJncm91cCI6Ik1lbWJlciIsImV4cCI6MTY4NDY2NzM1NSwiaXNzIjoiYmlyZCJ9.NFxHazi_j6JGgT8nbH_DpQ_w7sFx1j6Ps6guF2qU79c',
}
headers = {
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    'Authorization': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyaWQiOjEwMDIyLCJ1c2VybmFtZSI6InBlbmdqaWFuZ2NodW4iLCJvdXRUaW1lIjoxNjg0NTM3NzU1LCJncm91cCI6Ik1lbWJlciIsImV4cCI6MTY4NDY2NzM1NSwiaXNzIjoiYmlyZCJ9.NFxHazi_j6JGgT8nbH_DpQ_w7sFx1j6Ps6guF2qU79c',
    'Connection': 'keep-alive',
    'Content-Type': 'application/json;charset=UTF-8',
    # 'Cookie': 'sec=33d14def5e17fd8100859a98868e5bf045b7aacd; s_ac=%5B%22288feed2%22%2C%22ae17b59f%22%2C%220fcfa91f%22%2C%2254a622fb%22%2C%227c4b5fc1%22%2C%22227321dc%22%2C%22f9c28630%22%2C%228364e5ba%22%2C%221cbfe789%22%2C%22f657a60f%22%5D; NM-TOKEN=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyaWQiOjEwMDIyLCJ1c2VybmFtZSI6InBlbmdqaWFuZ2NodW4iLCJvdXRUaW1lIjoxNjg0NTM3NzU1LCJncm91cCI6Ik1lbWJlciIsImV4cCI6MTY4NDY2NzM1NSwiaXNzIjoiYmlyZCJ9.NFxHazi_j6JGgT8nbH_DpQ_w7sFx1j6Ps6guF2qU79c; u_tk=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyaWQiOjEwMDIyLCJ1c2VybmFtZSI6InBlbmdqaWFuZ2NodW4iLCJvdXRUaW1lIjoxNjg0NTM3NzU1LCJncm91cCI6Ik1lbWJlciIsImV4cCI6MTY4NDY2NzM1NSwiaXNzIjoiYmlyZCJ9.NFxHazi_j6JGgT8nbH_DpQ_w7sFx1j6Ps6guF2qU79c',
    'Origin': 'http://mashang888.shuju.cfd',
    'Referer': 'http://mashang888.shuju.cfd/shop/goods/detail?sn=230507141800190C',
    'Sign': '06bffc1226b793ce9cbb9ae047e67166590319c0f49850b5dd1c67d22408786a40b234314cac82c0f030f9748fcfffc0',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36 Edg/113.0.1774.42',
}
json_data = {
    'returnUrl': 'http://mashang888.shuju.cfd/shop/goods/detail?sn=230507141800190C',
    'goodsSN': '230507141800190C',#商品编号|TV丨播放-特价 (不解锁)日速5-10W
    'number': 2000,
    'params': [
        {
            'name': 'BV',
            'alias': 'BV',
            'value': BV ,#需要刷的视频BV号
        },
    ],
}#TV丨播放-特价 (不解锁)日速5-10W
response = requests.post( 'http://mashang888.shuju.cfd/client/goods/v2/order', cookies=cookies,headers=headers,json=json_data,verify=False,)
json_data2 = {
    'returnUrl': 'http://mashang888.shuju.cfd/shop/goods/detail?sn=2305081219001A8A',
    'goodsSN': '2305081219001A8A',#商品编号|
    'number': 50,
    'params': [
        {
            'name': '请输入作品BV',
            'alias': 'bili',
            'value': BV,#需要刷的视频BV号
        },
    ],
}#TV丨视频分享3
response2 = requests.post( 'http://mashang888.shuju.cfd/client/goods/v2/order',cookies=cookies,headers=headers,json=json_data2,verify=False,)
json_data3 = {
    'returnUrl': 'http://mashang888.shuju.cfd/shop/goods/detail?sn=2208281623000847',
    'goodsSN': '2208281623000847',#商品编号|
    'number': 10,
    'params': [
        {
            'name': '口令/链接',
            'alias': '口令/链接',
            'value': BV,#需要刷的视频BV号
        },
    ],
}#TV丨视频分享3
response3 = requests.post('http://mashang888.shuju.cfd/client/goods/v2/order',cookies=cookies,headers=headers,json=json_data3,verify=False,)
json_data4 = {
    'returnUrl': 'http://mashang888.shuju.cfd/shop/goods/detail?sn=22042120380004CC',
    'goodsSN': '22042120380004CC',#商品编号|
    'number': 30,
    'params': [
        {
            'name': 'BV号',
            'alias': 'zh',
            'value': BV,#需要刷的视频BV号
        },
        {
            'name': '间隔时间(秒)',
            'alias': 'JG',
            'value': '10',
        },
    ],
}#TV | 低级通用弹幕
response4 = requests.post('http://mashang888.shuju.cfd/client/goods/v2/order',cookies=cookies, headers=headers,json=json_data4, verify=False,)
json_data5 = {
    'returnUrl': 'http://mashang888.shuju.cfd/shop/goods/detail?sn=2302171927000F0A',
    'goodsSN': '2302171927000F0A',
    'number': 10,
    'params': [
        {
            'name': 'BV号',
            'alias': 'BV号',
            'value': BV,
        },
        {
            'name': '间隔(秒)',
            'alias': '间隔(秒)',
            'value': '10',
        },
    ],
}#TV | 低级通用评论
response5 = requests.post('http://mashang888.shuju.cfd/client/goods/v2/order',cookies=cookies, headers=headers,json=json_data5, verify=False,)