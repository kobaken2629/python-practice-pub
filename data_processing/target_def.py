# check_targets(sales, targets) — 担当者ごとの売上合計と目標達成状況を返す
sales = [
    {"rep": "Taro", "amount": 3000},
    {"rep": "Hanako", "amount": 5000},
    {"rep": "Taro", "amount": 4000},
    {"rep": "Hanako", "amount": 3000},
    {"rep": "Jiro", "amount": 2000}
]

targets = {
    "Taro": 8000,
    "Hanako": 7000,
    "Jiro": 5000
}

# 期待する出力：
# {
#   "Taro":   {"total": 7000, "target": 8000, "achieved": False},
#   "Hanako": {"total": 8000, "target": 7000, "achieved": True},
#   "Jiro":   {"total": 2000, "target": 5000, "achieved": False}
# }
#
# 出力はdict辞書、
# rep ごとにsales を合計
# 合計がtarget 以上であれば true, 未満であればfalse とする
#

tmp_result = {}
result = {}
def check_targets(sales, targets):
    for i in sales:
        if i["rep"] not in tmp_result:
            tmp_result[i["rep"]] = {"total": 0}
        tmp_result[i["rep"]]["total"] += i["amount"]
    #print(tmp_result)

    for x, data in tmp_result.items():
        r_name = [x]
        r_total = tmp_result[x]["total"]
        r_target = targets[x]
        if r_total >= r_target:
            r_achi = True
        else:
            r_achi = False
        
        result[x] = {
            "total": r_total,
            "target": r_target,
            "achieved": r_achi
        }
    return result
print(check_targets(sales, targets))
