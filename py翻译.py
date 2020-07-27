import requests
from bs4 import BeautifulSoup
def welcome():
    print("*******************")
    print("**欢迎来到py 翻译**")
    print("**退出查询请输入q**")
    print("*******************")
    return

def fanyi(words):
    try:
        url="http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule"
        head={"User-Agent": "Mozilla/5.0"}
        data={
            "i":words,
            
            "doctype":"json"
            }
        r=requests.post(url,data=data,headers=head)
        keyword=r.json()
        print(keyword['translateResult'][0][0]['tgt'])
    except:
        print("翻译出错")

welcome()
while True:
    print("输入你所要翻译的内容:")
    words=input()
    if words=='q':
        break;
    else:
        fanyi(words)
