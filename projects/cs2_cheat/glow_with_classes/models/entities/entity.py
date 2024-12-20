from __future__ import annotations

import struct
from functools import cached_property
from typing import Any

import models.memory


class Entity:
    def __init__(self, memory: models.memory.Memory, address: int) -> None:
        self._memory = memory
        self.address = address

    def __bool__(self) -> bool:
        return bool(self.address)

    def __hash__(self) -> int:
        return hash(self.address)

    def __eq__(self, other: Any) -> bool:
        return isinstance(other, Entity) and self.address == other.address

    def __str__(self) -> str:
        return str(self.class_name)

    ...

    def glow(self, color: tuple[int, int, int] | None = None) -> None:
        if color:
            color_bytes = struct.pack('4B', *color, 255)
            self._memory.write_bytes(
                self.address + self._memory.m_Glow + self._memory.m_glowColorOverride,
                color_bytes,
                len(color_bytes)
            )

        self._memory.write_bool(self.address + self._memory.m_Glow + self._memory.m_bGlowing, True)

    @cached_property
    def identity_address(self) -> int:
        return self._memory.read_ulonglong(self.address + self._memory.m_pEntity)
