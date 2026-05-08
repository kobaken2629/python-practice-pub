# normalize_records(records, mappings) — コードを名前に変換して返す
records = [
    {"name": "Taro", "dept_code": "ENG", "status_code": "A"},
    {"name": "Hanako", "dept_code": "SAL", "status_code": "I"},
    {"name": "Jiro", "dept_code": "ENG", "status_code": "A"},
    {"name": "Yuki", "dept_code": "MKT", "status_code": "I"}
]

mappings = {
    "dept_code": {
        "ENG": "Engineering",
        "SAL": "Sales",
        "MKT": "Marketing"
    },
    "status_code": {
        "A": "Active",
        "I": "Inactive"
    }
}

# 期待する出力：
# [
#   {"name": "Taro",   "dept_code": "Engineering", "status_code": "Active"},
#   {"name": "Hanako", "dept_code": "Sales",        "status_code": "Inactive"},
#   {"name": "Jiro",   "dept_code": "Engineering",  "status_code": "Active"},
#   {"name": "Yuki",   "dept_code": "Marketing",    "status_code": "Inactive"}
# ]
# --- 処理の考え方
# mappings の dept_code や status_code の中のvalue を取り出す必要がある。
# mapping["dept_code"]["ENG"]
# mapping["dept_code"][i["dept_code"]]   i["dept_code"]は、records の"ENG" や "SAL"をとれる
#

result = []
def normalize_records(records, mappings):
    for i in records:
        #print(mappings["dept_code"][i["dept_code"]])
        dept_c = mappings["dept_code"][i["dept_code"]]
        status_c = mappings["status_code"][i["status_code"]]
        tmp_result = {
            "name": i["name"],
            "dept_code": dept_c,
            "status_code": status_c
        }
        result.append(tmp_result)
    return result

print(normalize_records(records, mappings))
