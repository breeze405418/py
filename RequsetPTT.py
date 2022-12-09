import urllib.request as req
url ='https://www.ptt.cc/bbs/Gossiping/index.html'

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
titles=root.find_all('div',class_='title') #尋找所有 class="title"的div標籤

for title in titles:
    if title.a !=None: #如果標題包含a標籤(沒有被刪除). 印出來
        print(title.a.string)


# with open('PTT.txt','w',encoding="utf-8") as file:
#     for title in titles:
#         file.write(title.a.string + '\n')
