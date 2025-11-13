import os
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from litestar import Litestar
from litestar.di import Provide

from app.controllers.user_controller import UserController
from app.providers import get_db_session, get_user_repository, get_user_service

# Database configuration
DATABASE_URL = os.getenv("DATABASE_URL", "sqlite+aiosqlite:///mydb.sqlite3")

engine = create_async_engine(DATABASE_URL, echo=True)
async_session_factory = async_sessionmaker(
    engine, class_=AsyncSession, expire_on_commit=False
)

app = Litestar(
    route_handlers=[UserController],
    dependencies={
        "db_session": Provide(get_db_session),
        "user_repository": Provide(get_user_repository),
        "user_service": Provide(get_user_service),
    },
)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)