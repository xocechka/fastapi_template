from db.base_class import Base
from db.session import SessionLocal, engine
from security.auth.db import engine as async_engine


async def create_tables():
    async with async_engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

    Base.metadata.create_all(bind=engine)


async def init_db() -> None:
    await create_tables()
