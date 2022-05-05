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


@dp.message_handler(Text(equals="Cleareance"))
async def get_cleareance(message: types.Message):
    await message.answer("Please waiting...")
    time.sleep(5)
    url = vs_config.dict_url["cleareance"]["url"]
    data = parcing_vs.get_data(url, "cleareance")
    if not data:
        await message.answer("No items ...")
        return

    for item in data:
        url = data[item]["url"]
        price = data[item]["price"]
        title = data[item]["name"]
        sale_price = data[item]["min_price"]
        pict_link = "".join(data[item]["pict_ref"]) + ".jpg"
        if sale_price <= vs_config.dict_url["cleareance"]["min_price"]:
            card = f"{hlink(title, url)}\n" \
                   f"{hbold('Категория: ')} Cleareance\n" \
                   f"{hbold('Цена: ')} {price}\n" \
                   f"{hbold('Прайс со скидкой: ')} - {sale_price}"
            await message.answer_photo(pict_domain + pict_link, card)
            time.sleep(0.2)


@dp.message_handler(Text(equals="Beauty"))
async def get_cleareance(message: types.Message):
    await message.answer("Please waiting...")
    time.sleep(5)
    url = vs_config.dict_url["beauty"]["url"]
    data = parcing_vs.get_data(url, "beauty")
    if not data:
        await message.answer("No items ...")
        return

    for item in data:
        url = data[item]["url"]
        price = data[item]["price"]
        title = data[item]["name"]
        sale_price = data[item]["min_price"]
        pict_link = "".join(data[item]["pict_ref"]) + ".jpg"
        if sale_price <= vs_config.dict_url["beauty"]["min_price"]:
            card = f"{hlink(title, url)}\n" \
                   f"{hbold('Категория: ')} Beauty\n" \
                   f"{hbold('Цена: ')} {price}\n" \
                   f"{hbold('Прайс со скидкой: ')} - {sale_price}"
            await message.answer_photo(pict_domain + pict_link, card)
            time.sleep(0.2)


@dp.message_handler(Text(equals="Panties"))
async def get_cleareance(message: types.Message):
    await message.answer("Please waiting...")
    time.sleep(5)
    url = vs_config.dict_url["panties"]["url"]
    data = parcing_vs.get_data(url, "panties")
    if not data:
        await message.answer("No items ...")
        return

    for item in data:
        url = data[item]["url"]
        price = data[item]["price"]
        title = data[item]["name"]
        sale_price = data[item]["min_price"]
        pict_link = "".join(data[item]["pict_ref"]) + ".jpg"
        if sale_price <= vs_config.dict_url["panties"]["min_price"]:
            card = f"{hlink(title, url)}\n" \
                   f"{hbold('Категория: ')} Panties\n" \
                   f"{hbold('Цена: ')} {price}\n" \
                   f"{hbold('Прайс со скидкой: ')} - {sale_price}"
            await message.answer_photo(pict_domain + pict_link, card)
            time.sleep(1)


def main():
    executor.start_polling(dp)


if __name__ == "__main__":

    main()

