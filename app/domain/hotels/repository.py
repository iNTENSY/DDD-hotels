import uuid
from typing import Protocol

from app.domain.hotels.entity import Hotels


class IHotelRepository(Protocol):
    async def create(self, domain: Hotels) -> None: ...

    async def find_all(self, limit: int, offset: int) -> list[Hotels] | None: ...

    async def filter_by(self, **parameters) -> list[Hotels] | None: ...

    async def update(self, data: dict, id: uuid.UUID) -> Hotels: ...

    async def delete(self, **parameters) -> Hotels: ...
