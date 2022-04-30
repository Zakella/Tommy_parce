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
pict_domain = "https://www.victoriassecret.com/p/280x373/"


@dp.message_handler(commands="start")
async def start(message: types.Message):
    start_buttons = ["Cleareance", "Beauty", "Panties"]
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(*start_buttons)
    await message.answer("Sale", reply_markup=keyboard)


async def load_cat(name_cat, message):
    time.sleep(5)
    url = vs_config.dict_url[name_cat]["url"]
    data = parcing_vs.get_data(url, name_cat)
    if not data:
        await message.answer("No items ...")
        return

    for item in data:
        url = data[item]["url"]
        price = data[item]["price"]
        title = data[item]["name"]
        sale_price = data[item]["min_price"]
        pict_link = "".join(data[item]["pict_ref"]) + ".jpg"
        if sale_price <= vs_config.dict_url[name_cat]["min_price"]:
            card = f"{hlink(title, url)}\n" \
                   f"{hbold('Категория: ')} {name_cat.title()}\n" \
                   f"{hbold('Цена: ')} {price}\n" \
                   f"{hbold('Прайс со скидкой: ')} - {sale_price}"
            await message.answer_photo(pict_domain + pict_link, card)
            time.sleep(0.2)


@dp.message_handler(Text(equals="Cleareance"))
async def get_cleareance(message: types.Message):
    await message.answer("Please waiting...")
    await load_cat("cleareance", message)


@dp.message_handler(Text(equals="Beauty"))
async def get_cleareance(message: types.Message):
    await message.answer("Please waiting...")
    await load_cat("beauty", message)


@dp.message_handler(Text(equals="Panties"))
async def get_cleareance(message: types.Message):
    await message.answer("Please waiting...")
    await load_cat("panties", message)


def main():
    executor.start_polling(dp)


if __name__ == "__main__":
    main()
