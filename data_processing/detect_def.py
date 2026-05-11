# detect_anomalies(logs, threshold) — 平均レスポンスタイムよりthreshold倍以上遅いログを返す
logs = [
    {"endpoint": "/users", "response_time": 120},
    {"endpoint": "/orders", "response_time": 850},
    {"endpoint": "/users", "response_time": 130},
    {"endpoint": "/orders", "response_time": 200},
    {"endpoint": "/users", "response_time": 900},
    {"endpoint": "/products", "response_time": 150}
]

threshold = 2  # 平均の2倍以上を異常とする

# 期待する出力：
# [
#   {"endpoint": "/orders", "response_time": 850},
#   {"endpoint": "/users", "response_time": 900}
# ]
# ---考えたこと---
# 一旦、全てのエンドポイントのレスポンスタイムを足す、カウントフラグを立てて平均で使う
#

result =[]
def detect_anomalies(logs, threshold):
        x = 0
        tmp_sum = 0
        tmp_ave = 0
        for i in logs:
            #print(i["response_time"])
            tmp_sum += i["response_time"]
            x += 1
        tmp_ave = tmp_sum / x
        #print(tmp_ave)
    
        for i in logs:
            if i["response_time"] >= tmp_ave * threshold:
                result.append(i)
        return result
print(detect_anomalies(logs, threshold))