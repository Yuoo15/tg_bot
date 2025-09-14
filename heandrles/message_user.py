from aiogram.types import Message, CallbackQuery
from aiogram import Router, F
from keyboards.inline import categor, item
router = Router()
@router.message(F.text == 'Каталог')
async def catalog(message: Message):
    await message.answer('Выберите каталог', reply_markup=await categor())

@router.callback_query(F.data.startwith('category_'))
async def category(call: CallbackQuery):
    await call.answer()
    await call.message.answer('выерите', reply_markup=await item(call.data.split('_')[1]))

