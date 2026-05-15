# analyze_retention(orders) — 月ごとの新規顧客数とリピート顧客数を返す
orders = [
    {"customer": "Taro", "month": "2024-01"},
    {"customer": "Hanako", "month": "2024-01"},
    {"customer": "Taro", "month": "2024-02"},
    {"customer": "Jiro", "month": "2024-02"},
    {"customer": "Hanako", "month": "2024-03"},
    {"customer": "Yuki", "month": "2024-03"},
    {"customer": "Taro", "month": "2024-03"}
]

# 期待する出力：
# {
#   "2024-01": {"new": 2, "repeat": 0},
#   "2024-02": {"new": 1, "repeat": 1},
#   "2024-03": {"new": 1, "repeat": 2}
# }
# --- 考え
# 初めて名前がでればnew、2回目はrepeat
# if not in でnew のフラグ、それ以降で repat のフラグ
# new のフラグを入れる時に　該当月のnew に、repeat のときに該当月のrepeatに 
# データは、月順にソートされている前提
# 

month_result= {}
old_result = []
def analyze_retention(orders):
    for i in orders:
        # 月の箱がなければ作る
        if i["month"] not in month_result:
            month_result[i["month"]] = {"new": 0, "repeat": 0}
        
        # 新規かリピートか判定
        if i["customer"] not in old_result:
            old_result.append(i["customer"])
            month_result[i["month"]]["new"] += 1
        else:
            month_result[i["month"]]["repeat"] += 1
    return month_result
print(analyze_retention(orders))