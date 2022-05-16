import requests
import json
from fake_useragent import UserAgent
import mechanize


def parce():

    with open("headers.json") as file:
        headers = json.load(file)
        print(headers)





    url = "https://usa.tommy.com/en/tommy-hilfiger-sale"
    responce = requests.session().get(url=url, headers=headers)
    print(responce.json())

    # br = mechanize.Browser()
    # br.open(url)
    # # follow second link with element text matching regular expression
    # response1 = br.follow_link(text_regex=r"cheese\s*shop", nr=1)
    # print(response1.read())


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    parce()



