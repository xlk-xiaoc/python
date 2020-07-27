# -*- coding= utf-8 -*-
import requests
import re
import time
import random
import traceback
import os


def GetPage(keyword,pn):
    '''
    获取页面
    :param keyword:查询的关键字
    :param pn:页面图片数量
    :return:成功获取页面的连接
    '''
    content = ""
    i = 0
    while i <= pn:
        try:

            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.86 Safari/537.36'
            }
            # 得到相关页面的URL链接
            url = "https://image.baidu.com/search/flip?tn=baiduimage&ie=utf-8&word=" + keyword + "&pn=" + str(
                pn) + "&gsm=3c&ct=&ic=0&lm=-1&width=0&height=0"
            # 发送get请求并返回内容
            getcontent = requests.get(url, headers=headers).text
            content += getcontent
            i += 40
            time.sleep(random.uniform(0.8, 1.2))
        except:
            print("获取页面失败")
    return content


def Getpn(num):
    '''
    控制下载片数量为有效的值
    :param num:下载的图片数量
    :return:一个整型用来控制后面页面的加载次数
    '''
    pn = 0
    while num>60:
        num-=60
        pn+=40
    return pn


def DownLoad(content,keyword,num):
    '''
    下载图片到本地
    :param content:获取的页面内容
    :param keyword:搜索关键字
    :param num:下载的图片数量
    :return:
    '''

    # 筛选图片链接
    picurl_list = re.findall('"objURL":"(.*?)"', content)  # 匹配准确获取的链接

    # 保存有效的图片链接
    picurls = []
    for picurl in picurl_list:
        onepicurl = re.findall('http://.+g', picurl)
        picurls.append(onepicurl[0])

    # 创建文件夹
    if os.path.exists("Baidu_Picture") == False:
        os.mkdir("Baidu_Picture/")
    i = 0

    for url in picurls:
        i += 1
        filename = keyword + str(i)
        try:
            r = requests.get(url)
            path = "Baidu_Picture/" + filename + ".jpg"
            with open(path, 'wb') as f:
                f.write(r.content)
                print(filename + "爬取成功")
        except:
            print("爬取图片失败")

        if i == num:
            break


def main():
    keyword = str(input("请输入要下载的图片关键字："))
    num = int(input("请输入下载的图片数量："))
    pn = Getpn(num)
    star = time.time()
    # 获取页面的内容
    content = GetPage(keyword, pn)
    # 下载图片
    DownLoad(content,keyword,num)
    finsh = time.time()
    spend_time = finsh - star
    print("下载用时：%fs" % spend_time)


if __name__ == '__main__':
    main()
