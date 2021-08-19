import json
from pathlib import Path

uppercase = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')


def _parse(idx, question):
    examTypeName = question['examTypeName']
    content = question['content']
    optionList = question['optionList']
    answer = question['answer']
    source = question['source']
    expandPercent = question['expandPercent']
    expanddoExamNum = question['expanddoExamNum']
    analysis = question['analysis']
    try:
        knowledge = question['knowledge'][0]
        parentChapterName = knowledge['parentChapterName']
        chapterName = knowledge['chapterName']
        knowLedgeName = knowledge['knowLedgeName']
        yaoQiuName = knowledge['yaoQiuName']
        pageNum = knowledge['pageNum']
    except:
        knowledge = None
    s = f'**{idx} [{examTypeName}]** {content}\n\n'
    for char, option in zip(uppercase, optionList):
        s += f'{char}. {option}\n\n'
    s += "```\n"
    s += f"正确答案：{answer}\n\n"
    if source:
        s += f"来 源：{source}\n\n"
    if knowledge:
        s += f"知 识 点：{parentChapterName} > {chapterName} > {knowLedgeName} ({yaoQiuName})\n\n"
        s += f"教材页码：{pageNum}\n\n"
    s += f"试题难度：本题共被作答 {expanddoExamNum} 次 正确率 {expandPercent} %\n\n"
    s += f"参考解释：{analysis}\n"
    s += "```\n\n"
    return s


def parse(path):
    with path.open(encoding='utf-8') as f:
        data = json.load(f)['examDtoList']
    # print(path)
    result = '\n'.join([_parse(idx, d) for idx, d in enumerate(data, 1)])
    mdpath = Path(str(path).replace("原始版题库/", "").replace(".json", ".md"))
    mddir = mdpath.parent
    mddir.mkdir(parents=True, exist_ok=True)
    with mdpath.open('w', encoding='utf-8') as f:
        f.write(result)
        print(mdpath)


if __name__ == '__main__':
    basedir = Path("../考试题库/原始版题库")
    for i in basedir.rglob("*.json"):
        parse(i)
