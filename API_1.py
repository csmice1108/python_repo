import requests
import json

'''
# 76-城市空气质量 - 代码参考（根据实际业务情况修改）

# 基本参数配置
apiUrl = 'http://web.juhe.cn/environment/air/cityair'  # 接口请求URL
apiKey = '0a04668fa164231fc31c863b65ed4d9c'  # 在个人中心->我的数据,接口名称上方查看

# 接口请求入参配置
requestParams = {
    'key': apiKey,
    'city': '苏州',
}

# 发起接口网络请求
response = requests.get(apiUrl, params=requestParams)

# 解析响应结果
with open('weather.json', 'a', encoding='utf-8') as f:
    if response.status_code == 200:
        responseResult = response.json()
        # 网络请求成功。可依据业务逻辑和接口文档说明自行处理。
        print(responseResult, file=f)
    else:
        # 网络异常等因素，解析结果异常。可依据业务逻辑自行处理。
        print('请求异常')
'''
with open("weather.json", "r", encoding="utf-8") as f:
    data = json.load(f)

print(data["result"][0]["citynow"]["city"])
print("feat1")
print("feat2")
print("main1")