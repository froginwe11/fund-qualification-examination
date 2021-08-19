import re
import json
import base64
from pathlib import Path
from requests_html import HTMLSession
from dump_chapters import headers

au_headers = {"authorization": "bearer MjbY0t3Yr0gTlI8bc0WNrqkBaZdAMhbHXxmnFIPkaNb4gGr7McFJBMLSRMFevdiAXrynaEIIAbRiTmcHI59eb9QJEaWlwKVWX1PTf82w2dMN0gtpl2W4DP5RVpy3LZ1lApdRS-IAlMY2drX4ITz0hMzDwf0fLDo9mlpdqQJDuJF_bdsxWPCHJJSUMDtDE_c9aoVKcxspcdVQuxTqFNV2Iw"}
url = "https://wx.233.com/tiku/api/exam/"
getExamUrl = "https://wx.233.com/tiku/exam/GetExam?md5={md5}&type={type}&pageIndex=1&pageSize=200&isError=0"


def _dump(classid, fromUrl, target, directory):
    session = HTMLSession()
    session.headers = headers
    data = {
        "ClassId": classid,
        "Type": target['type'],
        "ObjectId": target['chapter_id'],
        "ExamType": "-1",
        "ExtractType": 0,
        "Mode": 1,
        "Redo": False,
        "IsContinue": False,
        "Count": 0,
        "PageIndex": 0,
        "PageSize": 0,
        "IsAutoDelRight": 0,
        "FromUrl": fromUrl,
        "Rank": 0,
        "PaperType": None,
        "Channel": 0
    }
    b64data = base64.b64encode(json.dumps(data).encode()).decode()
    try:
        ttt = session.post(url, data={'url': b64data})
        examUrl = ttt.json()['list']['url']
    except:
        print(target, ttt, ttt.text)
        return
    md5 = re.search(r"md5=(\w+)", examUrl).group(1)
    tiku = session.get(getExamUrl.format(
        md5=md5, type=target['type']), headers=au_headers).json()['list']
    dirpath = Path("../考试题库") / directory
    dirpath.mkdir(parents=True, exist_ok=True)
    filepath = dirpath / (target['name']+".json")
    with filepath.open('w', encoding="utf-8") as f:
        json.dump(tiku, f, ensure_ascii=False, indent=2)
        print(filepath)


def dump_all(p: Path):
    bdir = p.stem
    with p.open(encoding='utf-8') as f:
        data = json.load(f)
    for zhang in data:
        classid, fromUrl = zhang['classid'], zhang['fromUrl']
        zd = zhang['name']
        for jie in zhang['children']:
            jd = jie['name']
            ppp = '/'.join([bdir, zd, jd])
            _dump(classid, fromUrl, jie, ppp)
            for zhisd in jie['children']:
                _dump(classid, fromUrl, zhisd, ppp)


if __name__ == '__main__':
    # dump_all(Path('../考试题库/基金法律法规_练习.json'))
    dump_all(Path('../考试题库/基金法律法规_真题.json'))
    dump_all(Path('../考试题库/证券投资基金基础知识_练习.json'))
    dump_all(Path('../考试题库/证券投资基金基础知识_真题.json'))
