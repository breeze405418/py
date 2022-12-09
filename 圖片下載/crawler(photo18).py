import urllib.request as req
from bs4 import BeautifulSoup
import requests
import os


img_input = input('輸入代號')
url ='https://www.photos18.com/v/'+img_input

#建立一個 Request 物件 ,附加 Request Headers 的資訊
request=req.Request(url, headers={
    "User-Agent":"Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Mobile Safari/537.36"
})
with req.urlopen(request) as response:
    data=response.read().decode("utf-8")
print(data)
#解析原始碼,取得每篇文章的標題
import bs4
root = bs4.BeautifulSoup(data,'html.parser')
titles=root.find_all('img',{'class':'lazyimage'}) #尋找所有 class="title"的div標籤


p=[]

for title in titles:
        if len(title['data-src']) > 40:
            p.append(title['data-src'])

for index , i in enumerate(p):
    if not os.path.exists(img_input):
        os.mkdir(img_input)
    img = requests.get(i)
    with open(img_input+'\\' + img_input + str(index+1) + ".jpg", "wb") as file:  # 開啟資料夾及命名圖片檔
        file.write(img.content)  # 寫入圖片的二進位碼