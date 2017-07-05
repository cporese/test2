import requests
import os
from bs4 import BeautifulSoup

url_1 = "http://www.aesvch.com/"
r = requests.get("http://www.aesvch.com/acg/2423-1/")
soup = BeautifulSoup(r.text,"html.parser")

def savepics(url):
    root = "D://图片//test//"
    path = root + url.split('/')[-1]
    try:
        if not os.path.exists(root):
            os.mkdir(root)
            if not os.path.exists(path):
                r1 = requests.get(url)
                with open(path,"wb") as f:
                    f.write(r1.content)
                    f.close()
                    print("图片保存成功")
            else:
                print("图片已存在")
        else:
            if not os.path.exists(path):
                r1 = requests.get(url)
                with open(path,"wb") as f:
                    f.write(r1.content)
                    f.close()
                    print("图片保存成功")
            else:
                print("图片已存在")
    except:
        print("图片爬取失败")

for link in soup.find_all('img'):
    tag = link.get('file')
    if not tag is None:
        url = url_1 + tag
        savepics(url)


