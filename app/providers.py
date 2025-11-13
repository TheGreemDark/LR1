from typing import AsyncGenerator
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import sessionmaker

from app.repositories.user_repository import UserRepository
from app.services.user_service import UserService

async def get_session() -> AsyncGenerator[AsyncSession, None]:
    from app.main import async_session_factory
    async with async_session_factory() as session:
        yield session

async def get_db_session() -> AsyncGenerator[AsyncSession, None]:
    """Поставщик сессии базы данных"""
    async for session in get_session():
        yield session

async def get_user_repository(db_session: AsyncSession) -> UserRepository:
    """Поставщик UserRepository"""
    repository = UserRepository()
    repository.session = db_session
    return repository

async def get_user_service(user_repository: UserRepository) -> UserService:
    """Поставщик UserService"""
    return UserService(user_repository)
