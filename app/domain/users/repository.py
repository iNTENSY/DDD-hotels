import uuid
from typing import Protocol

from app.domain.users.entity import Users


class IUserRepository(Protocol):
    async def create(self, domain: Users) -> Users: ...

    async def find_all(self, limit: int, offset: int) -> list[Users] | None: ...

    async def filter_by(self, **parameters) -> list[Users] | None: ...

    async def update(self, data: dict, id: uuid.UUID) -> Users: ...

    async def delete(self, **parameters) -> Users: ...
