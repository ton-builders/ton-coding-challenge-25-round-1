import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.filters import Command

API_KEY = "BOT_TOKEN_HERE"
WALLET_ID = "UQBPvTVcmD3IU7KAMiVx6DIa2d-8-LIzLHQlLsUE7MMA4FKa"
TG_HANDLE = "@dyshko"

bot_instance = Bot(token=API_KEY)
dispatcher = Dispatcher()

def generate_keyboard(layout):
    return InlineKeyboardMarkup(inline_keyboard=layout)

def get_main_keyboard():
    return generate_keyboard([
        [InlineKeyboardButton(text="A", callback_data="opt_1"), InlineKeyboardButton(text="B", callback_data="opt_2")]
    ])

def get_submenu_one():
    return generate_keyboard([
        [InlineKeyboardButton(text="A1", callback_data="choice_a_1")],
        [InlineKeyboardButton(text="A2", callback_data="choice_a_2")],
        [InlineKeyboardButton(text="🔙 Back", callback_data="back")]
    ])

def get_submenu_two():
    return generate_keyboard([
        [InlineKeyboardButton(text="B1", callback_data="choice_b_1")],
        [InlineKeyboardButton(text="B2", callback_data="choice_b_2")],
        [InlineKeyboardButton(text="🔙 Back", callback_data="back")]
    ])

@dispatcher.message(Command("wallet"))
@dispatcher.message(lambda msg: msg.text.lower() == "wallet")
async def send_wallet_info(msg: types.Message):
    await msg.answer(WALLET_ID)

@dispatcher.message(Command("tg"))
@dispatcher.message(lambda msg: msg.text.lower() == "tg")
async def send_contact_info(msg: types.Message):
    await msg.answer(TG_HANDLE)

@dispatcher.message(Command("menu"))
@dispatcher.message(lambda msg: msg.text.lower() == "menu")
async def display_main_menu(msg: types.Message):
    await msg.answer("Select an option:", reply_markup=get_main_keyboard())

@dispatcher.callback_query(lambda query: query.data in ["opt_1", "opt_2"])
async def handle_menu_selection(query: types.CallbackQuery):
    if query.data == "opt_1":
        await query.message.edit_text("This is submenu of A:", reply_markup=get_submenu_one())
    else:
        await query.message.edit_text("This is submenu of B:", reply_markup=get_submenu_two())

@dispatcher.callback_query(lambda query: query.data in ["choice_a_1", "choice_a_2", "choice_b_1", "choice_b_2"])
async def handle_submenu_selection(query: types.CallbackQuery):
    await query.answer(f"You chose {query.data.replace('_', ' ').upper()}.")

@dispatcher.callback_query(lambda query: query.data == "back")
async def navigate_back(query: types.CallbackQuery):
    await query.message.edit_text("Select an option:", reply_markup=get_main_keyboard())

async def run_bot():
    await dispatcher.start_polling(bot_instance)

if __name__ == "__main__":
    asyncio.run(run_bot())