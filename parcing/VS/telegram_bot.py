from config import token
import time
from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher.filters import Text
from aiogram.utils.markdown import hbold, hlink
import vs_config
import parcing_vs

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


async def load_cat(name_cat, message):
    await message.answer("Please waiting...")
    data = parcing_vs.get_data(name_cat)
    if not isinstance(data, list):
        await message.answer(data)
        return

    for item in data:
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
            time.sleep(0.8)

        except:
            await message.answer(card)


@dp.message_handler(Text(equals="Sale"))
async def get_cleareance(message: types.Message):
    await load_cat("sale", message)


@dp.message_handler(Text(equals="Beauty"))
async def get_beauty(message: types.Message):
    await load_cat("beauty", message)


@dp.message_handler(Text(equals="Panties"))
async def get_panties(message: types.Message):
    await load_cat("panties", message)


@dp.message_handler(Text(equals="Lingerie"))
async def get_lingerie(message: types.Message):
    await load_cat("lingerie", message)


@dp.message_handler(Text(equals="Swimsuits"))
async def get_swimsuits(message: types.Message):
    await load_cat("swimsuits", message)


@dp.message_handler(Text(equals="Sport"))
async def get_sport(message: types.Message):
    await load_cat("sport", message)


@dp.message_handler(Text(equals="Sleep"))
async def get_sleep(message: types.Message):
    await load_cat("sleep", message)


@dp.message_handler(Text(equals="Accessories"))
async def get_accessories(message: types.Message):
    await load_cat("accessories", message)


@dp.message_handler(Text(equals="All Brands We love"))
async def get_al_brands_we_love(message: types.Message):
    await load_cat("al_brands_we_love", message)


@dp.message_handler(Text(equals="Gifts"))
async def get_gifts(message: types.Message):
    await load_cat("gifts", message)


@dp.message_handler(Text(equals="Bras"))
async def get_gifts(message: types.Message):
    await load_cat("bras", message)




def main():
    executor.start_polling(dp)


if __name__ == "__main__":
    main()

#