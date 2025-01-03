import struct
from functools import cached_property
from typing import Self

import constants
from models.entities.entity import Entity
from models.enums import Bone, Team
from models.memory import Memory
from models.vector import Vector


class Player(Entity):
    def __init__(self, memory: Memory, address: int, controller_address: int | None = None) -> None:
        if not controller_address:
            controller_handle_address = memory.read_ulonglong(address + memory.m_hController)
            controller_address = memory.get_entity_address_from_handle_address(controller_handle_address)

        super().__init__(memory, address)
        self.controller_address = controller_address

    @cached_property
    def bone_array_address(self) -> int:
        return self._memory.read_ulonglong(
            self.scene_node_address + self._memory.m_modelState + constants.BONE_ARRAY_PADDING
        )

    @classmethod
    def from_controller_address(cls, memory: Memory, controller_address: int) -> Self | None:
        handle_address = memory.read_ulonglong(controller_address + memory.m_hPawn)
        if address := memory.get_entity_address_from_handle_address(handle_address):
            return cls(memory, address, controller_address)

    def get_bone_position(self, bone: Bone) -> Vector | None:
        if not self.bone_array_address:
            return

        bone_bytes = self._memory.read_bytes(
            self.bone_array_address + self.skeleton[bone] * constants.BONE_DATA_SIZE,
            Vector.SIZE
        )
        position = struct.unpack('3f', bone_bytes)

        if position != (0.0, 0.0, 0.0):
            return Vector(*position)

    def glow(self, color: tuple[int, int, int] | None = None) -> None:
        if not color:
            health = max(0, self.health)
            health = min(health, 100)

            if health <= 50:
                ratio = health / 50
                color = (255, int(ratio * 255), 0)
            else:
                ratio = (health - 50) / 50
                color = (255 - int(ratio * 255), 255, 0)

        super().glow(color)

    @property
    def health(self) -> int:
        return self._memory.read_int(self.address + self._memory.m_iHealth)

    @cached_property
    def skeleton(self) -> dict[Bone, int] | None:
        if self.team is Team.COUNTER_TERRORIST:
            return constants.SKELETON['base'] | constants.SKELETON['counter_terrorist']
        elif self.team is Team.TERRORIST:
            return constants.SKELETON['base'] | constants.SKELETON['terrorist']

    @cached_property
    def team(self) -> Team | None:
        if not self.controller_address:
            return

        try:
            return Team(self._memory.read_int(self.controller_address + self._memory.m_iTeamNum))
        except ValueError:
            pass

    @property
    def view_position(self) -> Vector:
        view_offsets = Vector.from_address(self._memory, self.address + self._memory.m_vecViewOffset)
        return self.floor_position + view_offsets
