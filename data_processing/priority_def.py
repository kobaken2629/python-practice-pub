# prioritize_orders(orders) — 優先度ごとに注文をグループ分けして、各グループを金額の高い順に並び替えて返す
orders = [
    {"id": 1, "product": "laptop", "amount": 1000, "priority": "high"},
    {"id": 2, "product": "mouse", "amount": 200, "priority": "low"},
    {"id": 3, "product": "monitor", "amount": 800, "priority": "high"},
    {"id": 4, "product": "keyboard", "amount": 300, "priority": "medium"},
    {"id": 5, "product": "headset", "amount": 500, "priority": "medium"},
    {"id": 6, "product": "webcam", "amount": 150, "priority": "low"}
]

# 期待する出力：
# {
#   "high":   [{"id": 1, ...amount: 1000}, {"id": 3, ...amount: 800}],
#   "medium": [{"id": 5, ...amount: 500}, {"id": 4, ...amount: 300}],
#   "low":    [{"id": 2, ...amount: 200}, {"id": 6, ...amount: 150}]
# }
# ---- 考え方 ----
# 出力は{}辞書、value は priority、value は[]リストでorder入れる
# 最後に 金額(amount) の順で sort
#

tmp_result = {}
result = {}
def prioritize_orders(orders):
    for i in orders:
        if i["priority"] not in tmp_result:
            tmp_result[i["priority"]] = []
        tmp_result[i["priority"]].append(i)
        tmp2_result = sorted(tmp_result[i["priority"]], key=lambda x: x["amount"], reverse=True) #sort の指定でtmp の[]のみになるよう調整
        result[i["priority"]] = tmp2_result
    return result
print(prioritize_orders(orders))

"""
--- AI の参考回答,シンプル。sort 用のfor を使っている
def prioritize_orders(orders):
    for i in orders:
        if i["priority"] not in tmp_result:
            tmp_result[i["priority"]] = []
        tmp_result[i["priority"]].append(i)
    
    for priority, data in tmp_result.items():
        result[priority] = sorted(data, key=lambda x: x["amount"], reverse=True)
    
    return result
"""
