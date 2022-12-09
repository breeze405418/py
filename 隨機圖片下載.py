# import PTTBeautysingle

import urllib.request as req
from bs4 import BeautifulSoup
import requests
import os

indexnum=input('請輸入4000以下的數字')

url ='https://www.ptt.cc/bbs/Beauty/'
indexurl ='https://www.ptt.cc/bbs/Beauty/index'+ indexnum+ '.html'

res = requests.get(indexurl)

#建立一個 Request 物件 ,附加 Request Headers 的資訊
request=req.Request(indexurl, headers={
    "cookie": "over18=1",
    "User-Agent":"Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Mobile Safari/537.36"
})
with req.urlopen(request) as response:
    data=response.read().decode("utf-8")
#解析原始碼,取得每篇文章的標題
import bs4
root = bs4.BeautifulSoup(data,'html.parser')
titles=root.find_all('div',class_='title') #尋找所有 class="title"的div標籤
for title in titles:
    print(title.a.string)

arr=[]
for title in titles:
    arr.append(title.a['href'].replace('/bbs/Beauty/',''))

for enter in arr:

    url ='https://www.ptt.cc/bbs/Beauty/'+ enter


    #建立一個 Request 物件 ,附加 Request Headers 的資訊
    request=req.Request(url, headers={
        "cookie": "over18=1",
        "User-Agent":"Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Mobile Safari/537.36"
    })
    with req.urlopen(request) as response:
        data=response.read().decode("utf-8")

    #解析原始碼,取得每篇文章的標題
    import bs4
    root = bs4.BeautifulSoup(data,'html.parser')
    titles=root.find_all('a') #尋找所有 class="title"的div標籤
    toptitle = root.find('title').get_text()
    print(toptitle)
    p=[]
    for title in titles:
        if len(title['href']) > 30 and len(title['href'])<35 :
            p.append(title['href'])
 
    for index , i in enumerate(p):
        if not os.path.exists(toptitle):
            os.mkdir(toptitle)
        img = requests.get(i)
        with open(toptitle+'\\' + toptitle + str(index+1) + ".jpg", "wb") as file:  # 開啟資料夾及命名圖片檔
            file.write(img.content)  # 寫入圖片的二進位碼   
