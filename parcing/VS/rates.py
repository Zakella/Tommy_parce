import requests
import json
from bs4 import BeautifulSoup

responce = requests.get("http://pki.maib.md/rates/")
# print(responce.text)


root = BeautifulSoup (responce.text, 'html.parser')
root.find_all('br',responce.text)
for i in root:
    print(i)
# print(root)
# sup = BeautifulSoup.find_all(responce.text, "b")
# a = responce.text.find("5/6/2022")
# print(a)

# with open("rates", "w", encoding="utf-8") as rates:
#     json.dump(responce.text, rates, indent=4, ensure_ascii=False)
