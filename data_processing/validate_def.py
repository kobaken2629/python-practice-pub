# validate_records(records, required_keys) — 必須キーが全て揃っているレコードだけ返す
records = [
    {"name": "Taro", "age": 30, "email": "taro@example.com"},
    {"name": "Hanako", "email": "hanako@example.com"},
    {"name": "Jiro", "age": 25},
    {"name": "Yuki", "age": 28, "email": "yuki@example.com"},
    {"age": 22, "email": "ken@example.com"}
]

required_keys = ["name", "age", "email"]

# 期待する出力：
# [
#   {"name": "Taro", "age": 30, "email": "taro@example.com"},
#   {"name": "Yuki", "age": 28, "email": "yuki@example.com"}
# ]
# --- 検討---
# 出力は リスト、OKな records をそのまま入れる、append
# for で回して、if でマッチをみる
# for の1回目で、name 、2回目で age 、3回目でemail があったときのみ、append
# --- 試行錯誤 ---
# records に name をもってないレコードがあるため、if i["name"] がエラーになる。そのような場合は all() を使う
#

result = []
def validate_records(records, required_keys):
    for i in records:
        if all(key in i for key in required_keys):
            result.append(i)
    return result
print(validate_records(records, required_keys))

