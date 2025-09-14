from aiogram import Router, F
from aiogram.filters import Command, CommandStart
from aiogram.types import Message
from keyboards.reply import main
import data.reg as rq
router = Router()

@router.message(CommandStart())
async def start(message:Message):
    await rq.set_user(message.from_user.id)
    await message.answer(f'Добро пожаловать в магазин кроссовок, {message.from_user.first_name}', reply_markup=main)

