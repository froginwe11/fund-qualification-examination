# 不提供cookies，某些章节会缺失
import json
from collections import namedtuple
from requests_html import HTMLSession
from requests.cookies import cookiejar_from_dict

cookie = "UM_distinctid=17b39549229466-0c80bac37ced24-31710157-137df8-17b3954922a211; UserId=33668060; denglumoblie=18468069469; userDefaultClassId=1004; Hm_lvt_41458584ac7611d4bad1fc47207293a2=1629084230; CNZZDATA1273056636=1557580480-1629084348-https%253A%252F%252Fwww.233.com%252F%7C1629084348; CNZZDATA1527823=cnzz_eid%3D2053284968-1629083430-https%253A%252F%252Fwww.233.com%252F%26ntime%3D1629083430; Hm_lvt_d4e7ae37d3a3d52a6fc57f690de53ecd=1629084391; CNZZDATA1277995585=1202351027-1628842347-https%253A%252F%252Fwww.233.com%252F%7C1629102712; CNZZDATA5895265=cnzz_eid%3D1804945351-1628842347-https%253A%252F%252Fwww.233.com%252F%26ntime%3D1629102712; CNZZDATA1260565743=100125119-1628844234-https%253A%252F%252Fwww.233.com%252F%7C1629103508; CNZZDATA1257759894=79737955-1628750583-https%253A%252F%252Fwww.233.com%252F%7C1629165280; _cnzz_CV1257759894=%E8%BA%AB%E4%BB%BD%7C%E4%BC%9A%E5%91%98%7C0; 233ZhichiUUID=eb792fcf-3f7a-479a-8abf-95953a9aef96; CNZZDATA4109769=cnzz_eid%3D880705081-1628751166-https%253A%252F%252Fwww.233.com%252F%26ntime%3D1629271305; redirectUrl=http%253a%252f%252fwx.233.com%252ftiku%252fchapter%252fdo%252f7ca734085835581a8d54d44a44074815%253fisAutoDelRight%253d0%2526extractType%253d0%2526fromUrl%253dhttps%253a%25252F%25252Fwx.233.com%25252Ftiku%25252Fchapter%25252F1004; logRegphotoCode=7p90bm7jgck9olsb63bibmfwro3c83jb; clientauthentication=eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiIzMzY2ODA2MCIsInJvbGVJZHMiOlsxXSwiYm9zc05hbWUiOiIiLCJuaWNrbmFtZSI6IiIsInVzZXJUeXBlIjoxLCJ1c2VyTmFtZSI6ImtqbW9iaWxlX2YzYmg4MyIsImV4cCI6MTYzMDEzOTIxMywidXNlcklkIjoiMzM2NjgwNjAiLCJpYXQiOjE2MjkyNzUyMTMsInBsYXRmb3JtIjowLCJqdGkiOiIwZWFjNjZjYy0xMWVlLTRhMzktODI0ZC1hODMyMGI4MGQ5Y2IifQ.7jH0ogFpAdnHmsQLNLKzUO897D6k-ENo3ZQ8KopBp00; clientauthenticationref=eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiIzMzY2ODA2MCIsInJvbGVJZHMiOlsxXSwiYm9zc05hbWUiOiIiLCJuaWNrbmFtZSI6IiIsInVzZXJUeXBlIjoxLCJ1c2VyTmFtZSI6ImtqbW9iaWxlX2YzYmg4MyIsImV4cCI6MTYzMDU3MTIxMywidXNlcklkIjoiMzM2NjgwNjAiLCJpYXQiOjE2MjkyNzUyMTMsInBsYXRmb3JtIjowLCJqdGkiOiIzYmIyZjQxMS00M2I4LTQwNDYtOTg5Mi04ZDhjNjBhNjc1ZDAifQ.S2OA-zSXH_zKgvNzPuAFmQDIViexCjCtNCKjH7vrBXI; Auth=F94DD90E6F322E7FFD8F319352373B7A200E7502B7CFE727870D8AF62956F3AA275E5BD6677FD8746C6C69FEAD39B13FDAD08C2F87867665; AuthGuid=A1AE85FD1482E7310880855B3B11CF827A87C2E50D3DFD2BE678F6802F1B8154DB9E9139352F4B96; wxuserinforset=username=kjmobile_f3bh83&userID=33668060&headpic=http%253a//img.233.com/wx/img/uc/Avatar.png&nickname=233%25u7f51%25u6821%25u7f51%25u53cb&fsclassId=&ksclassId=&classname=&registertime=2021/08/12%2015:49:15&isnewuser=0&addtime=2021-08-12%2015:49:15&paymoney=0.0; javadeviceid=d3c5eec0-06c3-4850-b8d0-00e6d27ba2af; ASP.NET_SessionId=vuumjcqf5r1q5vrbf0am2wtl; i_defaultpage=1004; ASP.NET_SessionId=vuumjcqf5r1q5vrbf0am2wtl; CNZZDATA4556415=cnzz_eid%3D2122954908-1629084496-https%253A%252F%252Fwww.233.com%252F%26ntime%3D1629337451; CNZZDATA1257783334=1147046041-1628753497-https%253A%252F%252Fwww.233.com%252F%7C1629338063; CNZZDATA3583776=cnzz_eid%3D1473370782-1628754232-https%253A%252F%252Fwww.233.com%252F%26ntime%3D1629338120; savePosition=%u5E7F%u544A%u4F4D%u7F6E; advInfo=%u9898%u5E93%u4EF7%u503C177%u5143/%u79D1%uFF0C%u62A5%u540D%u9001%u9898%u5E93VIP%u4F1A%u5458%u3010%u7ACB%u5373%u67E5%u770B%u3011; ASPSESSIONIDCSRRDCBD=KDINFAJCPGHCMGBAAAHEILJA; acw_tc=7ce3ba2316293419261613345e90c4bb14c6f865dc69733680333dc233; SERVERID=e46d3e69c190528167e95134571014a5|1629342812|1629339817; CNZZDATA5149001=cnzz_eid%3D982375356-1629082884-https%253A%252F%252Fwww.233.com%252F%26ntime%3D1629342477"
headers = {
    "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36",
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "cookie": cookie
}
subject = namedtuple(
    "subject", ['subject', 'url', 'classid', 'type', 'ktype'])
subjects = {
    "s1_practice": subject("基金法律法规_练习", "https://wx.233.com/tiku/chapter/1188", "1188", "2", "106"),
    "s1_exam": subject("基金法律法规_真题", "https://wx.233.com/tiku/exam/chapter/1188", "1188", "105", "107"),
    "s2_practice": subject("证券投资基金基础知识_练习", "https://wx.233.com/tiku/chapter/1189", "1189", "2", "106"),
    "s2_exam": subject("证券投资基金基础知识_真题", "https://wx.233.com/tiku/exam/chapter/1189", "1189", "105", "107"),
    # "s3": subject("私募股权投资基金基础知识", "https://wx.233.com/tiku/chapter/1266", "https://wx.233.com/tiku/exam/chapter/1266", "1266")
}


def _dump_subject(url, filename, classid, type, ktype):
    result = []
    session = HTMLSession()
    session.headers = headers
    res = session.get(url)
    # 章
    for li in res.html.find("ul.problems_summary_zhang > li"):
        chapter_id = li.attrs['data-chapterid']
        name = li.find("p.pro_zhang_infoTit", first=True).text
        zhang = dict(chapter_id=chapter_id, name=name,
                     classid=classid, fromUrl=url, children=[])
        result.append(zhang)
        # 节
        for li_jie in li.find("ol.problems_summary_jie > li"):
            name = li_jie.find("p.pro_jieCont_tit", first=True).text
            jie_chapter_id, knowlecount = li_jie.attrs['data-chapterid'], li_jie.attrs['data-knowlecount']
            jie = dict(chapter_id=jie_chapter_id, name=name, type=type,
                       knowlecount=knowlecount, children=[])
            zhang['children'].append(jie)
            #　知识点
            for li_zhisd in li_jie.find("ul.problems_summary_zhisd > li"):
                name = li_zhisd.find("p.pro_zhisd_tit", first=True).text
                weight = li_zhisd.find(
                    "i.pro_zhisd_perTip", first=True).text[1:-1]
                a = li_zhisd.find('a[href="javascript:;"]', first=True)
                zsd_data_kid = a.attrs['data-kid']
                zsd = dict(chapter_id=zsd_data_kid, name=name,
                           weight=weight, type=ktype)
                jie['children'].append(zsd)
    fp = f"../考试题库/{filename}.json"
    with open(fp, 'w', encoding='utf-8') as f:
        json.dump(result, f, ensure_ascii=False, indent=2)
        print(fp)


def dump_subject(subj: subject):
    _dump_subject(subj.url, subj.subject, subj.classid, subj.type, subj.ktype)


if __name__ == '__main__':
    for i in subjects.values():
        dump_subject(i)
