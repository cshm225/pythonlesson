import requests
from bs4 import BeautifulSoup

# 指定urlにget通信
res = requests.get('https://joytas.net/kaba/')
# 文字化け対策
res.encoding = res.apparent_encoding

soup=BeautifulSoup(res.text,"html.parser")

#print(soup)
ele=soup.find("title")
print(ele.text)

imgs=soup.find_all("img")
for img in imgs:
    print(img.get("src"))

div=soup.find(id="headerImageBox")
imgs=soup.select(".headerImage")
for img in imgs:
    print(img.get("src"))




names=soup.find_all("td")


count = 0
for name in names:

    if count==0 or count%3==0:
        print(name.text)
    count+=1

names=soup.select("tr td:first-child")
for name in names:
    print(name.text)

# 指定urlにpost通信
res = requests.post('https://joytas.net/php/calc.php', data={'x': 10, 'y': 7})
# 文字化け対策
res.encoding = res.apparent_encoding

print(res.text)


links=soup.select("li a")

with open("zoo.txt","w",encoding="utf-8")as file:
    for link in links:
        file.write(f'{link.text}:{link.get("href")}\n')


