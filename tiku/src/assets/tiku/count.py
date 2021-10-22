import json
from pathlib import Path

basedir = Path(__file__).parent
tiku = basedir

for c in basedir.glob("*.json"):
    name = c.stem
    with c.open() as f:
        data = json.load(f)
        for z in data:
            zcount = 0
            for j in z['children']:
                jp = tiku / \
                    f'原始版题库/{name}/{z["name"]}/{j["name"]}/{j["name"]}.json'
                try:
                    with jp.open() as jf:
                        j["count"] = json.load(jf)["count"]
                        j["path"] = f'原始版题库/{name}/{z["name"]}/{j["name"]}/{j["name"]}.json'
                    for k in j['children']:
                        kp = tiku / \
                            f'原始版题库/{name}/{z["name"]}/{j["name"]}/{k["name"]}.json'
                        with kp.open() as kf:
                            k["count"] = json.load(kf)["count"]
                            k["path"] = f'原始版题库/{name}/{z["name"]}/{j["name"]}/{k["name"]}.json'
                except Exception as e:
                    print(e)
                    j['count'] = 0
                    j["path"] = None
                zcount += j['count']
            z['count'] = zcount
        with open(f"{name}_bak.json", 'w') as t:
            json.dump(data, t, ensure_ascii=False, indent=4)
