from __future__ import annotations

import itertools
from collections.abc import Callable, Iterator
from typing import Any, Literal, Self

import constants
import models.memory
from models.entities.entity import Entity


def return_true(_: Entity) -> Literal[True]:
    return True


class EntityList:
    def __init__(self, memory: models.memory.Memory, address: int) -> None:
        self._memory = memory
        self.address = address

    def __bool__(self) -> bool:
        return bool(self.address)

    def __hash__(self) -> int:
        return hash(self.address)

    def __eq__(self, other: Any) -> bool:
        return isinstance(other, EntityList) and self.address == other.address

    def __getitem__(self, index: int) -> Entity:
        return Entity(self._memory, self.get_entity_address(index))

    def __iter__(self) -> Iterator[Entity]:
        return self.iter_entities()

    def _iter_entities(
        self,
        identity_address: int,
        offset: int,
        filter: Callable[[Entity], bool] | None = return_true
    ) -> Iterator[Entity]:
        while identity_address := self._memory.read_ulonglong(identity_address + offset):
            entity = Entity.from_identity_address(self._memory, identity_address)
            if entity and filter(entity):
                yield entity

    @classmethod
    def from_index(cls, memory: models.memory.Memory, index: int) -> Self:
        address = memory.read_ulonglong(memory.entity_lists_address + index * constants.UNSIGNED_LONG_LONG_SIZE)
        return cls(memory, address)

    def get_entity(self, entity_index: int) -> Entity:
        return self[entity_index]

    def get_entity_address(self, entity_index: int) -> int:
        return self._memory.read_ulonglong(self.get_identity_address(entity_index))

    def get_identity_address(self, entity_index: int) -> int:
        return self.address + entity_index * constants.IDENTITY_SIZE

    def iter_entities(
        self,
        filter: Callable[[Entity], bool] | None = return_true,
        limit: int | None = None
    ) -> Iterator[Entity]:
        def iter_entities() -> Iterator[Entity]:
            identity_address = self.get_identity_address(0)
            return self._iter_entities(identity_address, self._memory.m_pNext, filter)

        return itertools.islice(iter_entities(), limit)

    def iter_entities_by_class(
        self,
        class_name: str,
        filter: Callable[[Entity], bool] | None = return_true,
        limit: int | None = None
    ) -> Iterator[Entity]:
        def iter_entities_by_class() -> Iterator[Entity]:
            identity_address = self.get_identity_address(0)

            while identity_address:
                entity = Entity.from_identity_address(self._memory, identity_address)
                if entity and entity.class_name == class_name:
                    yield entity
                    yield from self._iter_entities(identity_address, self._memory.m_pPrevByClass, filter)
                    yield from self._iter_entities(identity_address, self._memory.m_pNextByClass, filter)
                    break

                identity_address = self._memory.read_ulonglong(identity_address + self._memory.m_pNext)

        return itertools.islice(iter_entities_by_class(), limit)
