from aiogram.types import (InlineKeyboardButton, InlineKeyboardMarkup)
from data.reg import get_Cotegories, get_car_id
from aiogram.utils.keyboard import InlineKeyboardBuilder
catalog = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Кроссовки', callback_data='sneak')],
    [InlineKeyboardButton(text='Назад', callback_data='back')]
])

async def categor():
    all_cat = await get_Cotegories()
    builder = InlineKeyboardBuilder()
    for i in all_cat:
        builder.add(InlineKeyboardButton(text=i.name, callback_data=f"category_{i.id}"))
    builder.add(InlineKeyboardButton(text='Вернуться в главное меню', callback_data='back'))
    return builder.adjust(2).as_markup()

async def item(category_id):
    all_cat = await get_car_id(category_id)
    builder = InlineKeyboardBuilder()
    for i in all_cat:
        builder.add(InlineKeyboardButton(text=i.name, callback_data=f"item_{i.id}"))
    builder.add(InlineKeyboardButton(text='Вернуться в главное меню', callback_data='back'))
    return builder.adjust(2).as_markup()