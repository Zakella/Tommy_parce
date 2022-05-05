from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
from config import token
import time
from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher.filters import Text
from aiogram.utils.markdown import hbold, hlink
import vs_config
import parcing_vs
from callback_data import select

bot = Bot(token=token, parse_mode=types.ParseMode.HTML)
dp = Dispatcher(bot)
pict_domain = "https://www.victoriassecret.com/p/280x373/"


@dp.message_handler(commands="start")
async def start(message: types.Message):
    start_buttons = ["Sale", "Beauty", "Panties", "Lingerie", "Bras",
                     "Sleep", "Swimsuits", "Sport", "Accessories",
                     "All Brands We love", "Gifts"]
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(*start_buttons)
    await message.answer("Sale", reply_markup=keyboard)


async def load_cat(name_cat, selection , message):
    await message.answer("Please waiting...")
    data = parcing_vs.get_data(name_cat)
    counter = 0
    if not isinstance(data, list):
        await message.answer(data)
        return
    else:
        for item in data:
            if selection < item.get("min_price"):
                continue
            else:
                title = item.get("name")
                url = item.get("url")
                price = item.get("price")
                min_price = item.get("min_price")
                images = item.get("images")
                family = item.get("family")
                card = f"{hlink(title, url)}\n" \
                       f"{hbold('Family: ')} {family.title()}\n" \
                       f"{hbold('Price: ')} {price}\n" \
                       f"{hbold('Min. price: ')} - {min_price}"
                album = types.MediaGroup()
                try:
                    for image in images:
                        album.attach_photo(photo=image)
                    album.attach_photo(photo=item.get("main_image"), caption=card)
                    await message.answer_media_group(media=album)
                    counter +=1
                    time.sleep(1.2)


                except:
                    await message.answer(card)
        await message.answer(f'I m done! Total {counter} items')



async def create_inline_keyboard(message):
    print(message.text)
    if message.text == "All Brands We love":
        message.text = "al_brands_we_love"

    choise = InlineKeyboardMarkup(row_width=3)
    choise.insert(InlineKeyboardButton(text="5$",  callback_data=select.new(value=5.00,  cat=message.text.lower())))
    choise.insert(InlineKeyboardButton(text="10$", callback_data=select.new(value=10.00, cat=message.text.lower())))
    choise.insert(InlineKeyboardButton(text="15$", callback_data=select.new(value=15.00, cat=message.text.lower())))
    choise.insert(InlineKeyboardButton(text="20$", callback_data=select.new(value=20.00, cat=message.text.lower())))
    choise.insert(InlineKeyboardButton(text="25$", callback_data=select.new(value=25.00, cat=message.text.lower())))
    choise.insert(InlineKeyboardButton(text="35$", callback_data=select.new(value=35.00, cat=message.text.lower())))
    choise.insert(InlineKeyboardButton(text="45$", callback_data=select.new(value=45.00, cat=message.text.lower())))
    choise.insert(InlineKeyboardButton(text="50$", callback_data=select.new(value=50.00, cat=message.text.lower())))
    choise.insert(InlineKeyboardButton(text="65$", callback_data=select.new(value=65.00, cat=message.text.lower())))
    choise.insert(InlineKeyboardButton(text="75$", callback_data=select.new(value=75.00, cat=message.text.lower())))
    choise.insert(InlineKeyboardButton(text="All", callback_data=select.new(value=9999,  cat=message.text.lower())))
    await message.answer("Сhoose up to what price to look for", reply_markup= choise)


@dp.callback_query_handler(text_contains="selection")
async def process_selection (call:CallbackQuery):
    await call.answer(cache_time=60)
    data = call.data.split(":")
    await load_cat(data[2], float(data[1]), call.message)


@dp.message_handler(Text(equals="Sale"))
async def get_cleareance(message: types.Message):
    # await load_cat("sale", message)
    await create_inline_keyboard(message)


@dp.message_handler(Text(equals="Beauty"))
async def get_beauty(message: types.Message):
    await create_inline_keyboard(message)


@dp.message_handler(Text(equals="Panties"))
async def get_panties(message: types.Message):
    await create_inline_keyboard(message)


@dp.message_handler(Text(equals="Lingerie"))
async def get_lingerie(message: types.Message):
    await create_inline_keyboard(message)


@dp.message_handler(Text(equals="Swimsuits"))
async def get_swimsuits(message: types.Message):
    await create_inline_keyboard(message)


@dp.message_handler(Text(equals="Sport"))
async def get_sport(message: types.Message):
    await create_inline_keyboard(message)


@dp.message_handler(Text(equals="Sleep"))
async def get_sleep(message: types.Message):
    await create_inline_keyboard(message)


@dp.message_handler(Text(equals="Accessories"))
async def get_accessories(message: types.Message):
    await create_inline_keyboard(message)


@dp.message_handler(Text(equals="All Brands We love"))
async def get_al_brands_we_love(message: types.Message):
    await create_inline_keyboard(message)


@dp.message_handler(Text(equals="Gifts"))
async def get_gifts(message: types.Message):
    await create_inline_keyboard(message)


@dp.message_handler(Text(equals="Bras"))
async def get_gifts(message: types.Message):
    await create_inline_keyboard(message)


def main():
    executor.start_polling(dp)


if __name__ == "__main__":
    main()

#
