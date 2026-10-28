from app.api.models import EventSchema
from app.db import events, database


async def post(payload: EventSchema):
    query = events.insert().values(
        title=payload.title,
        city=payload.city,
        price_usd=payload.price_usd,
        seats_left=payload.seats_left,
    )
    return await database.execute(query=query)


async def get(id: int):
    query = events.select().where(id == events.c.id)
    return await database.fetch_one(query=query)


async def get_all():
    query = events.select()
    return await database.fetch_all(query=query)


async def put(id: int, payload: EventSchema):
    query = (
        events
        .update()
        .where(id == events.c.id)
        .values(
            title=payload.title,
            city=payload.city,
            price_usd=payload.price_usd,
            seats_left=payload.seats_left,
        )
        .returning(events.c.id)
    )
    return await database.execute(query=query)


async def delete(id: int):
    query = events.delete().where(id == events.c.id)
    return await database.execute(query=query)
