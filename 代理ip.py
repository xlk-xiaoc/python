import requests
from bs4 import BeautifulSoup
#table class="table table-bordered table-striped"

url="https://www.kuaidaili.com/free/"

head={'User-Agent': 'Mozilla/5.0'}
print("正在获取代理ip......")
r=requests.get(url,headers=head)
soup=BeautifulSoup(r.text,"html.parser")
info=soup.select(".table")
for tr in info:
    ltd=tr.select('td')
    message=[]
    with open("代理ip.txt",'w') as f:
        k=7
        for td in ltd:
            k-=1
            if k>0:
                f.write(td.string+" ")
            else:
                f.write('\n')
                k=7
    f.close()
print("获取完毕，请在当前文件目录中查看!")
