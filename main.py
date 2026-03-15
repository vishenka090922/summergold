import asyncio
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import Command
from aiogram.utils.keyboard import InlineKeyboardBuilder

# ================= НАСТРОЙКИ (МЕНЯЙ ТУТ) =================
TOKEN = "8464569638:AAH03bPYRN-k6QXo8hTOXTPd4lPMIo1dv9s"
ADMIN_ID = 8014629371  # Твой ID (цифрами)
MY_NICK = "vishenka"  # Твой ник БЕЗ @
PAY_INFO = "89126616714 Тинькофф Тимофей "  # Твой номер/карта
# =========================================================

bot = Bot(token=TOKEN)
dp = Dispatcher()

def main_menu():
    builder = InlineKeyboardBuilder()
    builder.row(types.InlineKeyboardButton(text="🛒 КУПИТЬ", callback_data="buy_menu"))
    builder.row(types.InlineKeyboardButton(text="💰 ПРОДАТЬ", callback_data="sell_menu"))
    builder.row(types.InlineKeyboardButton(text="⭐️ ОТЗЫВЫ", url="https://t.me/твой_канал"))
    builder.row(types.InlineKeyboardButton(text="👨‍💻 САППОРТ", callback_data="support"))
    return builder.as_markup()

@dp.message(Command("start"))
async def start(message: types.Message):
    await message.answer(
        f"<b>💰 STANDOFF GOLD EXCHANGE</b>\n\n"
        f"📥 <b>Скупаем:</b> по 0.55₽\n"
        f"📤 <b>Продаем:</b> по 0.65₽\n\n"
        f"<i>Выбирай раздел:</i>",
        parse_mode="HTML",
        reply_markup=main_menu()
    )

@dp.callback_query(F.data == "buy_menu")
async def buy_menu(callback: types.CallbackQuery):
    builder = InlineKeyboardBuilder()
    builder.row(types.InlineKeyboardButton(text="Купить 100г", callback_data="buy_100"))
    builder.row(types.InlineKeyboardButton(text="Купить 500г", callback_data="buy_500"))
    builder.row(types.InlineKeyboardButton(text="⬅️ НАЗАД", callback_data="back"))
    await callback.message.edit_text(
        "<b>🛒 ПОКУПКА (0.65₽)</b>\n\n• 100г — 65₽\n• 500г — 325₽",
        parse_mode="HTML",
        reply_markup=builder.as_markup()
    )

@dp.callback_query(F.data == "sell_menu")
async def sell_menu(callback: types.CallbackQuery):
    builder = InlineKeyboardBuilder()
    builder.row(types.InlineKeyboardButton(text="🤝 ПРОДАТЬ ГОЛДУ", url=f"https://t.me/{MY_NICK}"))
    builder.row(types.InlineKeyboardButton(text="⬅️ НАЗАД", callback_data="back"))
    await callback.message.edit_text(
        "<b>💰 ПРОДАЖА (0.55₽)</b>\n\nСкупаем от 100г. Выплаты на Qiwi/Карту.",
        parse_mode="HTML",
        reply_markup=builder.as_markup()
    )

@dp.callback_query(F.data == "buy_100")
async def buy_100(callback: types.CallbackQuery):
    await callback.message.answer(
        f"⚠️ <b>ОПЛАТА ЗАКАЗА</b>\n\nСумма: 65₽\nНомер: <code>{PAY_INFO}</code>\n\n"
        f"<i>После оплаты скинь чек: @{MY_NICK}</i>",
        parse_mode="HTML"
    )
    await bot.send_message(ADMIN_ID, f"🚀 ЗАКАЗ: @{callback.from_user.username} хочет купить 100г")

@dp.callback_query(F.data == "back")
async def back(callback: types.CallbackQuery):
    await callback.message.edit_text(
        "Вы вернулись в меню:",
        reply_markup=main_menu()
    )

async def main():
    print("🚀 БОТ ЗАПУЩЕН!")
    await dp.start_polling(bot)

if name == "main":
    asyncio.run(main())
