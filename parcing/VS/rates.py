import requests
import json
from bs4 import BeautifulSoup, element

responce = requests.get("http://pki.maib.md/rates/")
# print(responce.text)


soup = BeautifulSoup(responce.content, "html.parser")
print()

data = soup.find('pre')
# data = soup.find(href=True)
# print(data)

list_rates = {}

for i in data:
    # tag = i.br
    # print(tag)
    # print()
    print(type(i))
    if isinstance(i, element.NavigableString):
        print(i.string.split()[0])
        # list_rates[]
    # if not i == "<br/":
    #     print(i)
    print(i)
    # d2 = i.find("br")
    # print(d2)

    # print(i, type(i))
    # print(i.attrs.findall("a"))

# root.find_all('pre')
# for i in root:
#     print(i)
#     break
# print(root)
# sup = BeautifulSoup.find_all(responce.text, "b")
# a = responce.text.find("5/6/2022")
# print(a)

# with open("rates", "w", encoding="utf-8") as rates:
#     json.dump(responce.text, rates, indent=4, ensure_ascii=False)
