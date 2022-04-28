from vs_config import Bot as token
import requests
import time
import json
from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher.filters import Text
from aiogram.utils.markdown import hbold, hlink
import json
import vs_config
import parcing_vs

bot = Bot(token=token, parse_mode=types.ParseMode.HTML)
dp = Dispatcher(bot)


@dp.message_handler(commands="start")
async def start(message: types.Message):
    start_buttons = ["Cleareance", "Beauty", "Panties"]
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(*start_buttons)
    await message.answer("Sale", reply_markup=keyboard)


@dp.message_handler(Text(equals="Cleareance"))
async def get_cleareance(message: types.Message):
    await message.answer("Please waiting...")
    with open("cleareance_sale.json") as file:

        # "https://www.victoriassecret.com/p/280x373/tif/b6/a0/b6a0ab7c765c434bb412c35076e77134/112005234YLO_OM_F.jpg"
        # "https://www.victoriassecret.com/p/280x373/tif/51/2d/512d2ca46e3249a1ba5482704b3b2b50/111300385CYU_OM_F.jpg"

        pict_link = "https://www.victoriassecret.com//p/280x373/tif/51/2d/512d2ca46e3249a1ba5482704b3b2b50/111300385CYU_OM_F"
        pict_domain = "https://www.victoriassecret.com/p/280x373/"
        data = json.load(file)
        for item in data:
            url = data[item]["url"]
            price = data[item]["price"]
            title = data[item]["name"]
            sale_price = data[item]["min_price"]
            pict_link = "".join(data[item]["pict_ref"] ) + ".jpg"
            if sale_price <= 10:
                card = f"{hlink(title, url)}\n" \
                       f"{hbold('Категория: ')} Cleareance\n" \
                       f"{hbold('Цена: ')} {price}\n" \
                       f"{hbold('Прайс со скидкой: ')} - {sale_price}"

                # await message.answer(card)
                # print(pict_domain + pict_link, card)
                await message.answer_photo(pict_domain + pict_link, card)
                # time.sleep(2)
                # break

            # print(item["url"])
            # # print(item.get("url"))
            # card = f'{hlink(title, url)}\n'\
            # f'{hbold('Категория')} Cleareance\n'


def main():
    executor.start_polling(dp)


# def post_sales(data):
#     url = "https://api.telegram.org/bot"
#     for el in data:
#         print(data[el]["url"])
#         if data[el]["min_price"] < 10:
#             res = requests.get(
#                 "https://api.telegram.org/bot5322880379:AAHZeHrcSRoQtOekGdNJFlWc4UuZZe-lh3U/sendMessage?chat_id=-1001648134992&text=" +
#                 data[el]["url"])
#             time.sleep(5)
#
#         # for i in el:
#         #     print(i)
#         # print(el["url"])
#
#         # url = el[]
#     #
#     # channel_id = "1001648134992"
#     # url += token
#     #
#     # method = url + "/sendMessage"
#     #
#     # a = requests.get("https://api.telegram.org/bot5322880379:AAHZeHrcSRoQtOekGdNJFlWc4UuZZe-lh3U/getupdates")
#     # print(a.text)
#     #
# res = requests.get(
#     "https://api.telegram.org/bot5322880379:AAHZeHrcSRoQtOekGdNJFlWc4UuZZe-lh3U/sendMessage?chat_id=-1001648134992&text=test!")
# print(res.text)

# r = requests.post(method, data={
#     "chat_id": channel_id,
#     "text": "Hi Maria!"
# })
#
# if r.status_code != 200:
#     raise Exception("post_text")


if __name__ == "__main__":
    main()
    # with open("cleareance_sale.json") as mists:
    #     data = json.load(mists)
    #     post_sales(data)
