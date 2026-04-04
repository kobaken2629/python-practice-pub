# price_range_summary(products, ranges) — 価格帯ごとの商品数と平均価格を返す
products = [
    {"name": "laptop", "price": 1200},
    {"name": "mouse", "price": 200},
    {"name": "monitor", "price": 800},
    {"name": "keyboard", "price": 350},
    {"name": "headset", "price": 150},
    {"name": "webcam", "price": 600}
]

ranges = {
    "high": 1000,
    "mid": 500
}

# 期待する出力：
# {
#   "high": {"count": 1, "average": 1200.0},
#   "mid":  {"count": 2, "average": 700.0},
#   "low":  {"count": 3, "average": 233.3}
# }
# ----- 考え方 ----
# 出力は辞書{} key はranges からもってくる、valueは{}で該当レンジのカウント数、該当したものの平均
# for のあと if で priceを比較する
# [] に該当product のname を入れて、最後にカウント。value は都度 足し算して、それを count でわる
#

tmp_result = {
    "tmp_h":{"t_name":[], "t_total": 0},
    "tmp_m":{"t_name":[], "t_total": 0},
    "tmp_l":{"t_name":[], "t_total": 0}
}
def price_range_summary(products, ranges):
    for i in products:
        if i["price"] >= ranges["high"]:
            tmp_result["tmp_h"]["t_name"].append(i["name"])
            tmp_result["tmp_h"]["t_total"] += i["price"]
        elif i["price"] >= ranges["mid"]:
            tmp_result["tmp_m"]["t_name"].append(i["name"])
            tmp_result["tmp_m"]["t_total"] += i["price"]
        else:
            tmp_result["tmp_l"]["t_name"].append(i["name"])
            tmp_result["tmp_l"]["t_total"] += i["price"]             

    h_x = len(tmp_result["tmp_h"]["t_name"])
    h_ave = tmp_result["tmp_h"]["t_total"] / h_x
    m_x = len(tmp_result["tmp_m"]["t_name"])
    m_ave = tmp_result["tmp_m"]["t_total"] / m_x
    l_x = len(tmp_result["tmp_l"]["t_name"])
    l_ave = tmp_result["tmp_l"]["t_total"] / l_x

    result = {
    "high": {"count": h_x, "average": round(h_ave,1)},
    "mid":  {"count": m_x, "average": round(m_ave,1)},
    "low":  {"count": l_x, "average": round(l_ave,1)}
    }
    return result

print(price_range_summary(products, ranges))

"""
上記の h_x 以降は、for でまとめられる。イメージは以下。シンプルでよいかも。
result = {}
for key, data in tmp_result.items():
    count = len(data["t_name"])
    average = round(data["t_total"] / count, 1)
    result[key] = {"count": count, "average": average}
"""