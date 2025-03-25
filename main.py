import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.filters import Command

TOKEN = "BOT_TOKEN_HERE"
WALLET_ADDRESS = "UQBYenI3ANZIOXN5gpzcoEK7__yy6y1EhspbGn6pMfTMpvRO"
TELEGRAM_USERNAME = "@wdrxxx"

bot = Bot(token=TOKEN)
dp = Dispatcher()

def main_menu():
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="A", callback_data="menu_a"), InlineKeyboardButton(text="B", callback_data="menu_b")]
    ])
    return keyboard

def submenu_a():
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="A-1", callback_data="submenu_a1")],
        [InlineKeyboardButton(text="A-2", callback_data="submenu_a2")],
        [InlineKeyboardButton(text="⬅️ Go Back", callback_data="go_back")]
    ])
    return keyboard

def submenu_b():
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="B-1", callback_data="submenu_b1")],
        [InlineKeyboardButton(text="B-2", callback_data="submenu_b2")],
        [InlineKeyboardButton(text="Go Back", callback_data="go_back")]
    ])
    return keyboard

@dp.message(Command("wallet"))
@dp.message(lambda message: message.text.lower() == "wallet")
async def send_wallet(message: types.Message):
    await message.answer(WALLET_ADDRESS)

@dp.message(Command("tg"))
@dp.message(lambda message: message.text.lower() == "tg")
async def send_tg(message: types.Message):
    await message.answer(TELEGRAM_USERNAME)

@dp.message(Command("menu"))
@dp.message(lambda message: message.text.lower() == "menu")
async def show_menu(message: types.Message):
    await message.answer("Main Menu:", reply_markup=main_menu())

@dp.callback_query(lambda call: call.data in ["menu_a", "menu_b"])
async def process_menu(call: types.CallbackQuery):
    if call.data == "menu_a":
        await call.message.edit_text("Submenu A:", reply_markup=submenu_a())
    elif call.data == "menu_b":
        await call.message.edit_text("Submenu B:", reply_markup=submenu_b())

@dp.callback_query(lambda call: call.data in ["submenu_a1", "submenu_a2"])
async def process_submenu_a(call: types.CallbackQuery):
    await call.answer(f"You selected {call.data.upper()}.")

@dp.callback_query(lambda call: call.data in ["submenu_b1", "submenu_b2"])
async def process_submenu_a(call: types.CallbackQuery):
    await call.answer(f"You selected {call.data.upper()}.")

@dp.callback_query(lambda call: call.data == "go_back")
async def go_back(call: types.CallbackQuery):
    await call.message.edit_text("Main Menu:", reply_markup=main_menu())

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
