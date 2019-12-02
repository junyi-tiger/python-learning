import requests
import time
from threading import Timer

# 请求的url（不同用户有不同的url）
url = 'https://quic.yundong.qq.com/pushsport/cgi/rank/friends?g_tk=384987321'

# post提交的数据: body
params = {
    "cmd": 1,
    "pno": 1,
    "dtype": 1,
    "pnum": 20
}  # params作为json字符串数据放置在body中，需要特别注意：把单引号（'）转化为双引号（"），并把空格去除
body = {
    'dcapiKey': 'user_rank',
    'l5apiKey': 'rank_friends',
    'params': str(params).replace(" ", "").replace("'", "\"")
}

# 头部信息
headers = {
    "Content-Type": "application/x-www-form-urlencoded",
    "Cookie": "uin=o0705018614; p_uin=o0705018614; pvid=4775731968; pgv_info=ssid=s4597757080; pgv_pvid=4969701255; skey=MOdoqQG5Ur; p_skey=np0m5dkBxN919K6iB1RWEJ3W71m5c6UgnYjgnrgAlfs_; xClientProtoVer=https_https1",
    "User-Agent": "Mozilla/5.0 (Linux; Android 9; HLK-AL00 Build/HONORHLK-AL00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/66.0.3359.126 MQQBrowser/6.2 TBS/045008 Mobile Safari/537.36 V1_AND_SQ_8.1.8_1276_YYB_D QQ/8.1.8.4260 NetType/WIFI WebP/0.3.0 Pixel/1080 StatusBarHeight/72 SimpleUISwitch/0",
    "Accept": "*/*",
    "Cache-Control": "no-cache",
    "Host": "quic.yundong.qq.com",
    "Accept-Encoding": "gzip, deflate",
    "Connection": "keep-alive",
}

# 简化的头部信息
simple_headers = {
    "User-Agent": "Mozilla/5.0 (Linux; Android 9; HLK-AL00 Build/HONORHLK-AL00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/66.0.3359.126 MQQBrowser/6.2 TBS/045008 Mobile Safari/537.36 V1_AND_SQ_8.1.8_1276_YYB_D QQ/8.1.8.4260 NetType/WIFI WebP/0.3.0 Pixel/1080 StatusBarHeight/72 SimpleUISwitch/0",
    "Cookie": "uin=o0705018614; p_uin=o0705018614; pvid=4775731968; pgv_info=ssid=s4597757080; pgv_pvid=4969701255; skey=MOdoqQG5Ur; p_skey=np0m5dkBxN919K6iB1RWEJ3W71m5c6UgnYjgnrgAlfs_; xClientProtoVer=https_https1",
}


# 重新构造post提交数据
def rebuild_data(i):
    global params
    global body
    params["pno"] = i
    body = {'dcapiKey': 'user_rank',
            'l5apiKey': 'rank_friends',
            'params': str(params).replace(" ", "").replace("'", "\"")}


# 爬取一次qq_sport_data
def crawl_qq_sport_data():
    amount = 240  # 参与排行的好友数量
    for i in range(1, amount // 20 + 1):
        rebuild_data(i)
        r = requests.post(url=url, headers=simple_headers, data=body, verify=False)
        while r.status_code != 200:
            time.sleep(3)
            print("响应出错！" + time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time())))
            r = requests.post(url=url, headers=simple_headers, data=body, verify=False)
        data = r.json()
        file_name = "qq_sport_data" + time.strftime("%Y-%m-%d", time.localtime(time.time())) + ".txt"
        with open(file_name, "a+", encoding="utf-8") as f:
            f.write(str(data) + "\n")


def select_wanted_data(name):
    file_name = "qq_sport_data" + time.strftime("%Y-%m-%d", time.localtime(time.time())) + ".txt"
    with open(file_name, "r", encoding="utf-8") as f:
        all_lines = f.readlines()
        for line in all_lines:
            data = eval(line)
            ls = data["data"]["list"]
            if ls is None:
                continue
            for item in ls:
                if item["name"] == name:
                    print(item["points"], )




# 获取特定人的qq_sport_data
# 主程序入口
def main():
    crawl_cnt = 0

    while True:
        crawl_qq_sport_data()
        print("等待10分钟...")
        time.sleep(10 * 60)


cnt = 100
while cnt > 0:
    Timer(24*60*60, select_wanted_data)