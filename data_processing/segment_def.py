# segment_customers(customers, thresholds) — 顧客を購入金額でセグメント分けして返す
customers = [
    {"name": "Taro", "total_purchase": 5000},
    {"name": "Hanako", "total_purchase": 15000},
    {"name": "Jiro", "total_purchase": 800},
    {"name": "Yuki", "total_purchase": 12000},
    {"name": "Ken", "total_purchase": 3000}
]

thresholds = {
    "gold": 10000,
    "silver": 3000
}

# 期待する出力：
# {
#   "gold":   ["Hanako", "Yuki"],
#   "silver": ["Taro", "Ken"],
#   "bronze": ["Jiro"]
# }
#----- 考え方 -----
# 出力は 辞書{}で key がthresholds の中身、+ それ以外的なもの。value はそれぞれ、リスト。
# 合計金額で考えると　一旦、ユーザーごとに辞書{}でまとめつつ、金額を足して最後に thresholds との比較がよいか。
# thresholds のvalue は変更になるが文字列は変更されない前提でかく

tmp_result = {}
result = {
    "gold": [],
    "silver": [],
    "bronze": []
}
def segment_customers(customers, thresholds):
    for i in customers:
        if i["name"] not in tmp_result:
            tmp_result[i["name"]] = {"total": 0} #name をkey にした辞書をつくる
        tmp_result[i["name"]]["total"] += i["total_purchase"] #1["name"]とかは、tmp_result でなく customers の値をとって tmp_result にあるかをみている
        if tmp_result[i["name"]]["total"] >= thresholds["gold"]:
            result["gold"].append(i["name"])
        elif tmp_result[i["name"]]["total"] >= thresholds["silver"]: #elif 条件1 がFalse のときだけ確認
            result["silver"].append(i["name"])
        else:                                                       #全部False のとき
            result["bronze"].append(i["name"])
    return result

print(segment_customers(customers, thresholds))   