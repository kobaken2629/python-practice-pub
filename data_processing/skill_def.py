# match_skills(employees, required_skills) — 必要なスキルを全て持つ従業員を返す
employees = [
    {"name": "Taro", "skills": ["Python", "SQL", "AWS"]},
    {"name": "Hanako", "skills": ["Java", "SQL", "GCP"]},
    {"name": "Jiro", "skills": ["Python", "AWS", "Spark"]},
    {"name": "Yuki", "skills": ["SQL", "Python", "AWS", "Spark"]},
    {"name": "Ken", "skills": ["Python", "SQL"]}
]

required_skills = ["Python", "SQL", "AWS"]

# 期待する出力：
# ["Taro", "Yuki"]
#----- 考えーーーー
# 出力は[]リスト、name を入れる
# 複数のマッチなので、all 関数が利用できる
# employees を for で回して一人一人入れて、全てマッチするれば 名前をリストにいれる

result = []
def match_skills(employees, required_skills):
    for i in employees:
        if all(x in i["skills"] for x in required_skills):
            result.append(i["name"])
    return result
print(match_skills(employees, required_skills))