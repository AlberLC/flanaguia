from functools import cached_property
from typing import Self

from models.entities.entity import Entity
from models.enums import Team
from models.memory import Memory


class Player(Entity):
    def __init__(self, memory: Memory, address: int, controller_address: int | None = None) -> None:
        if not controller_address:
            controller_handle_address = memory.read_ulonglong(address + memory.m_hController)
            controller_address = memory.get_entity_address_from_handle_address(controller_handle_address)

        super().__init__(memory, address)
        self.controller_address = controller_address

    @classmethod
    def from_controller_address(cls, memory: Memory, controller_address: int) -> Self | None:
        handle_address = memory.read_ulonglong(controller_address + memory.m_hPawn)
        if address := memory.get_entity_address_from_handle_address(handle_address):
            return cls(memory, address, controller_address)

    def glow(self, color: tuple[int, int, int] | None = None) -> None:
        if not color:
            ...

        super().glow(color)

    ...

    ...
