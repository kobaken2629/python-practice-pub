# analyze_bestsellers(sales, top_n) — 売上上位top_n件の商品を返す
sales = [
    {"product": "laptop", "amount": 1000},
    {"product": "mouse", "amount": 200},
    {"product": "laptop", "amount": 1500},
    {"product": "monitor", "amount": 800},
    {"product": "mouse", "amount": 300},
    {"product": "keyboard", "amount": 400},
    {"product": "monitor", "amount": 600},
    {"product": "keyboard", "amount": 200}
]

top_n = 3

# 期待する出力：
# [
#   {"product": "laptop", "total": 2500},
#   {"product": "monitor", "total": 1400},
#   {"product": "keyboard", "total": 600}
# ]
# -------- 検討 -----------
# 出力は[]リスト、中に辞書{}、辞書{}はkeyがproductで、そのproduct の合計金額をtotal で返す
# 全てのtotal を出した後に top_n　の上位を選ぶのは sortメソッド？？？
# そのまとめをリストに入れるかな？？
# ------試したところ---------
# sorted は辞書もリストもできるけど、リストでやった方が簡単かも。なので、先に全てリスト化してみる
# ------試したところ---------
# やっぱ一旦辞書でやって、その後リストに入れて、そこでsorted がよいかも
#

tmp_result = {}
result =[]
def analyze_bestsellers(sales, top_n):
    for i in sales:
        if i["product"] not in tmp_result:
            tmp_result[i["product"]] = {"total": 0}
        tmp_result[i["product"]]["total"] += i["amount"]
    #print(tmp_result)
    for x,data in tmp_result.items():
        result.append({                 # リストなので基本追加なので{}を入れても上書きされない。
            "product": x,
            "total": data["total"]
        })
    sorted_result = sorted(result, key=lambda x: x["total"], reverse=True)
    return sorted_result[:top_n]  # 上位top_n件だけ返す
print(analyze_bestsellers(sales, top_n))
