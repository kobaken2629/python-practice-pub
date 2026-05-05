# python-practice-pub
python の学習用。生成AIに問題を出してもらい、それを解く。

## data_processing
データ処理の関数を練習
- 'support_def.py' - 担当者ごとのチケット数・解決率を集計
- 'analyze_def.py' - 売上上位top_n件の商品を返す
    - リストを利用して辞書を追加、top N 位を出すなど
- 'segment_def.py' -  顧客を購入金額でセグメント分けして返す
    - elif 条件1がFalse、else 全ての条件がFalse
- 'price_def.py' - 価格帯ごとの商品数と平均価格を返す
    - 同じ作業、for xxxx .items()を検討
- 'api_def.py' - エンドポイントごとのリクエスト数・平均レスポンスタイム・エラー率を返す
- 'skill_de.py' - 必要なスキルを全て持つ従業員を返す
    - all() の関数。all(x in リスト for x in 別のリスト)　で使う
        - 2つのリストが全て一致するときにTrueを返す
- 'priority_def.py' - 優先度ごとに注文をグループ分けして、各グループを金額の高い順に並び替えて返す
    - 並び替えの sort を行う場所を工夫。並べ替えようのfor文をつくる
- 'check_targets(sales, targets)' — 担当者ごとの売上合計と目標達成状況を返す
- 'validate_records(records, required_keys)' — 必須キーが全て揃っているレコードだけ返す

    - `key in i` とは、辞書 i に key というキーが存在するか確認します
```python
i = {"name": "Taro", "age": 30}
key = "name"
key in i   # True  → "name" は i に存在する

key = "email"
key in i   # False → "email" は i に存在しない
```

    -  `for key in required_keys` とは、required_keys を1つずつ取り出します
```python
required_keys = ["name", "age", "email"]

for key in required_keys:
    print(key)

# 1回目: key = "name"
# 2回目: key = "age"
# 3回目: key = "email"
```

    - `key in i` と `for key in required_keys` を組み合わせ
```python
i = {"name": "Taro", "age": 30}
required_keys = ["name", "age", "email"]

for key in required_keys:
    print(key in i)

# 1回目: key = "name"  → "name" in i  → True
# 2回目: key = "age"   → "age" in i   → True
# 3回目: key = "email" → "email" in i → False
```

    - all() はリストの中が全部 True のときだけ True を返す
```python
all([True, True, True])   # True  → 全部True
all([True, False, True])  # False → 1つでもFalseがある
all([False, False, False]) # False → 全部False
```