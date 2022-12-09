import urllib.request as req
from bs4 import BeautifulSoup
import requests
import os


img_input = input('請輸入網址後編號：\n')
res = requests.get('https://telegra.ph/'+img_input)

import bs4
data = res.text
root = bs4.BeautifulSoup(data,'html.parser')
titles=root.find_all('img') #尋找所有 class="title"的div標籤

p=[]
for title in titles:
    p.append('https://telegra.ph/'+title['src'])

for index , i in enumerate(p):
    if not os.path.exists(img_input):
        os.mkdir(img_input)
    # img = requests.get(i)

    with open(img_input+'\\'  + img_input +str(index+1) + ".jpg", "wb") as file:  # 開啟資料夾及命名圖片檔
        file.write(img.content)  # 寫入圖片的二進位碼