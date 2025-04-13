import requests
import json
import sys

def get_login_info():
    # 用户输入
    student_no = input("请输入一卡通号: ")
    id_card_no = input("请输入身份证号码: ")
    open_id = input("请输入 OpenID: ")

    # 定义请求头
    headers = {
        "Host": "tyxsjpt.seu.edu.cn",
        "xweb_xhr": "1",
        "miniappversion": "minappv3.0.1",
        "User-Agent": ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                      "(KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36 "
                      "MicroMessenger/7.0.20.1781(0x6700143B) NetType/WIFI "
                      "MiniProgramEnv/Windows WindowsWechat/WMPF WindowsWechat(0x63090c33)XWEB/11581"),
        "Content-Type": "application/json;charset=UTF-8",
        "Accept": "*/*",
        "Sec-Fetch-Site": "cross-site",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Dest": "empty",
        "Referer": "https://servicewechat.com/wx5da07e9f6f45cabf/38/page-frame.html",
        "Accept-Language": "zh-CN,zh;q=0.9"
    }

    # 定义请求数据
    data = {
        "tenant": "NDEzMjAxMDI4Ng==",
        "studentNo": student_no,
        "idCardNo": id_card_no,
        "openId": open_id,
        "grantType": "student"
    }

    try:
        # 发送 POST 请求
        response = requests.post(
            "https://tyxsjpt.seu.edu.cn/api/miniapp/anno/login",
            headers=headers,
            data=json.dumps(data),
            timeout=10  # 添加超时设置
        )
        
        # 检查HTTP状态码
        response.raise_for_status()
        
        # 解析JSON响应
        try:
            json_data = response.json()
        except json.JSONDecodeError as e:
            print(f"JSON解析错误: {e}")
            return None, None
            
        # 提取所需字段
        try:
            token = json_data['data']['token']
            user_id = json_data['data']['userId']
            print(f"\nToken:\n{token}\n")
            print(f"Student id:\n{user_id}\n")
            return token, user_id
        except Exception as e:
            print(f"响应中缺少必要字段: {e}")
            print("完整响应内容:", json_data)
            return None, None
            
    except requests.exceptions.RequestException as e:
        if isinstance(e, requests.exceptions.Timeout):
            print("请求超时")
        elif isinstance(e, requests.exceptions.ConnectionError):
            print("连接错误")
        elif isinstance(e, requests.exceptions.HTTPError):
            print(f"HTTP错误: {response.status_code}")
        else:
            print(f"请求错误: {e}")
        return None, None

if __name__ == "__main__":
    token, user_id = get_login_info()
    if token is None or user_id is None:
        input("Press enter to continue...")
        sys.exit(1)
    
    input("Press enter to continue...")