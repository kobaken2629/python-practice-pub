# transform_records(records, required_keys, rename_keys) 
# — 必須キーが揃っているレコードだけ抽出して、キー名を変換して返す
records = [
    {"name": "Taro", "age": 30, "email": "taro@example.com"},
    {"name": "Hanako", "email": "hanako@example.com"},
    {"name": "Jiro", "age": 25, "email": "jiro@example.com"},
    {"age": 22, "email": "ken@example.com"}
]

required_keys = ["name", "age", "email"]

rename_keys = {
    "name": "full_name",
    "age": "years",
    "email": "mail"
}

# 期待する出力：
# [
#   {"full_name": "Taro", "years": 30, "mail": "taro@example.com"},
#   {"full_name": "Jiro", "years": 25, "mail": "jiro@example.com"}
# ]
# -----検討
# 必須キーが揃っているレコードを all() で抽出、その後指定された形式で出力、
# key をリネームする

result = []
def transform_records(records, required_keys, rename_keys):
    for i in records:
        if all(key in i for key in required_keys):
            new_dict = {}  # ← for i の中に移動！毎回新しい辞書を作る
            for old_key, new_key in rename_keys.items():
                new_dict[new_key] = i[old_key]
            result.append(new_dict)  # ← new_dict を追加！
    return result
print(transform_records(records, required_keys, rename_keys))
