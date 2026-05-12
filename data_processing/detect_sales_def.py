# detect_sales_anomalies(sales, threshold) — 商品ごとの平均売上からthreshold倍以上乖離している売上を返す
sales = [
    {"product": "laptop", "amount": 1000},
    {"product": "laptop", "amount": 1200},
    {"product": "laptop", "amount": 5000},
    {"product": "mouse", "amount": 200},
    {"product": "mouse", "amount": 180},
    {"product": "mouse", "amount": 900}
]

threshold = 2

# 期待する出力：
# [
#   {"product": "laptop", "amount": 5000},
#   {"product": "mouse", "amount": 900}
# ]
# --- 考え方 ---
# sum で合計を出す、len で個数を数える、その2つで平均を出す、if で 平均 * threshold でover を表示
#

tmp_result = {}
result = []
def detect_sales_anomalies(sales, threshold):
    for i in sales:
        if i["product"] not in tmp_result: # 最初のproduct を入れる
            tmp_result[i["product"]] = {"amount": 0, "count": 0} # ここで int にしてあげないとダメ
        tmp_result[i["product"]]["amount"] += i["amount"] # product がすでにある場合は、同じproduct に足し算
        tmp_result[i["product"]]["count"] += 1

    for pro, data in tmp_result.items():
        ave = data["amount"] / data["count"] # 一つのproduct の平均

        for i in sales: # 上のfor 内で処理しないとave が”mouse"だけになる
            if i["product"] == pro:    #product 名と pro の一致にしないと 一つの ave で全商品をチェックする
                if i["amount"] >= ave * threshold:
                    result.append(i)
    return result
print(detect_sales_anomalies(sales, threshold))