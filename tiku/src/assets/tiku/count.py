import json
from pathlib import Path

basedir = Path(__file__).parent
names = ["基金法律法规_练习", "基金法律法规_真题", "证券投资基金基础知识_练习", "证券投资基金基础知识_真题"]
for name in names:
    tiku = basedir / f"原始版题库/{name}"

    examList = {}
    for c in tiku.rglob("第*节*.json"):
        with c.open() as f:
            d = json.load(f)
            for i in d['examDtoList']:
                examList[i['examId']] = i

    with (basedir / f"{name}_题库.json").open('w', encoding='utf-8') as f:
        json.dump(examList, f, ensure_ascii=False, indent=4)

# for c in basedir.glob("*.json"):
#     name = c.stem
#     with c.open() as f:
#         data = json.load(f)
#         for z in data:
#             zcount = 0
#             for j in z['children']:
#                 jp = tiku / \
#                     f'原始版题库/{name}/{z["name"]}/{j["name"]}/{j["name"]}.json'
#                 try:
#                     with jp.open() as jf:
#                         j["count"] = json.load(jf)["count"]
#                         j["path"] = f'原始版题库/{name}/{z["name"]}/{j["name"]}/{j["name"]}.json'
#                     for k in j['children']:
#                         kp = tiku / \
#                             f'原始版题库/{name}/{z["name"]}/{j["name"]}/{k["name"]}.json'
#                         with kp.open() as kf:
#                             k["count"] = json.load(kf)["count"]
#                             k["path"] = f'原始版题库/{name}/{z["name"]}/{j["name"]}/{k["name"]}.json'
#                 except Exception as e:
#                     print(e)
#                     j['count'] = 0
#                     j["path"] = None
#                 zcount += j['count']
#             z['count'] = zcount
#         with open(f"{name}_bak.json", 'w') as t:
#             json.dump(data, t, ensure_ascii=False, indent=4)
