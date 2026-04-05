# analyze_api_logs(logs) — エンドポイントごとのリクエスト数・平均レスポンスタイム・エラー率を返す
logs = [
    {"endpoint": "/users", "status": 200, "response_time": 120},
    {"endpoint": "/orders", "status": 500, "response_time": 300},
    {"endpoint": "/users", "status": 200, "response_time": 150},
    {"endpoint": "/orders", "status": 200, "response_time": 200},
    {"endpoint": "/users", "status": 500, "response_time": 400},
    {"endpoint": "/orders", "status": 200, "response_time": 180}
]

# 期待する出力：
# {
#   "/users":  {"count": 3, "avg_response": 223.3, "error_rate": 0.33},
#   "/orders": {"count": 3, "avg_response": 226.7, "error_rate": 0.33}
# }
# ----考える
# 出力 は辞書{}でエンドポインごと、value は辞書{}でカウント、レスポンスの平均、エラー率を入れる
# カウントはカンターをつくる、
# レスポンスタイムは合計していって最後にカウンターで割る、
# エラーは500 の数をカウントして カウントでわる

tmp_result = {}
result = {}
def analyze_api_logs(logs):
    for i in logs:
        if i["endpoint"] not in tmp_result:
            tmp_result[i["endpoint"]] = {"count": 0, "t_avg_response": 0, "t_error_rate": 0}
        tmp_result[i["endpoint"]]["count"] += 1
        tmp_result[i["endpoint"]]["t_avg_response"] += i["response_time"]
        if i["status"] == 500:
            tmp_result[i["endpoint"]]["t_error_rate"] += 1
    for x , data in tmp_result.items():   ## data を使っているのに、後続で使ってなかった。。。。
        avg_response = tmp_result[x]["t_avg_response"] / tmp_result[x]["count"]
        error_rate = tmp_result[x]["t_error_rate"] / tmp_result[x]["count"]
        result[x] = {
            "count": tmp_result[x]["count"],
            "avg_response": round(avg_response,1),
            "error_rate": round(error_rate,2)
        }
    return result
print(analyze_api_logs(logs))

