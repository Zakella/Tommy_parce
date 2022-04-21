from vs_config import Bot as token
import requests


def post_sales():

    url = "https://api.telegram.org/bot"
    channel_id = "1001648134992"
    url += token
    method = url + "/sendMessage"

    a = requests.get("https://api.telegram.org/bot5322880379:AAHZeHrcSRoQtOekGdNJFlWc4UuZZe-lh3U/getupdates")
    print(a.text)

    res = requests.get("https://api.telegram.org/bot5322880379:AAHZeHrcSRoQtOekGdNJFlWc4UuZZe-lh3U/sendMessage?chat_id=-1001648134992&text=you are ready?!")
    print(res.text)

    # r = requests.post(method, data={
    #     "chat_id": channel_id,
    #     "text": "Hi Maria!"
    # })
    #
    # if r.status_code != 200:
    #     raise Exception("post_text")



if __name__ == "__main__":
    post_sales()
