from data.modules import async_ssesion
from data.modules import User, Item, Category
from sqlalchemy import select
async def set_user(tg_id):
    async with async_ssesion() as session:
        user = await session.scalar(select(User).where(User.tg_id == tg_id))
        if not user:
            session.add(User(tg_id = tg_id))
            await session.commit()

async def get_Cotegories():
    async with async_ssesion() as session:
        return await session.scalars(select(Category))

async def get_car_id(item_id):
    async with async_ssesion() as session:
        return await session.scalars(select(Item).where(Item.Category == item_id))