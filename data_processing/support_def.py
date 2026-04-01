###### ticket_summary(tickets) — 担当者ごとのチケット数・解決済み数・解決率を返す
tickets = [
    {"id": 1, "assignee": "Taro", "status": "resolved"},
    {"id": 2, "assignee": "Hanako", "status": "open"},
    {"id": 3, "assignee": "Taro", "status": "resolved"},
    {"id": 4, "assignee": "Hanako", "status": "resolved"},
    {"id": 5, "assignee": "Taro", "status": "open"},
    {"id": 6, "assignee": "Jiro", "status": "resolved"},
    {"id": 7, "assignee": "Hanako", "status": "open"},
    {"id": 8, "assignee": "Jiro", "status": "open"}
]

# 期待する出力：
# {
#   "Taro":   {"total": 3, "resolved": 2, "rate": 0.67},
#   "Hanako": {"total": 3, "resolved": 1, "rate": 0.33},
#   "Jiro":   {"total": 2, "resolved": 1, "rate": 0.5}
# }
# 
# 出力は{}辞書、key がassignee、valueが辞書{}でassigneeの数、resolved の数、rate を出す
# assigned ごとのカウントはtotal、resloved はリストに入れる、最後に割り算で rate を出す
# 

result = {}
def ticket_summary(tickets):
    for i in tickets:
        if i["assignee"] not in result:
            result[i["assignee"]] = {"total": 0, "resolved": 0, "rate": 0}
        result[i["assignee"]]["total"] += 1
        if i["status"] == "resolved":
            result[i["assignee"]]["resolved"] += 1
        tmp_rate = result[i["assignee"]]["resolved"] / result[i["assignee"]]["total"]
        rounded_tmp_rate = round(tmp_rate,2)
        result[i["assignee"]]["rate"] = rounded_tmp_rate
    return result
print(ticket_summary(tickets))
    
    
