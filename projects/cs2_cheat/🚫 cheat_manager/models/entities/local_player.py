import struct

from models.aim_target import AimTarget
from models.entities.player import Player
from models.enums import Bone
from models.memory import Memory
from models.vector import Vector


class LocalPlayer(Player):
    def __init__(self, memory: Memory, address: int, controller_address: int | None = None) -> None:
        super().__init__(memory, address, controller_address)
        self.is_shooting = False

    def aim_at(self, position: Vector) -> None:
        angles_to_target = (position - self.view_position).direction_to_angles()
        angles_difference = angles_to_target - self.view_angles
        self.view_angles += angles_difference

    def get_angular_target(self, player: Player) -> AimTarget | None:
        if player.skeleton and (position := player.get_bone_position(Bone.HEAD)):
            return AimTarget(position, ((position - self.view_position).direction_to_angles() - self.view_angles).magnitude)

    def set_flash_alpha(self, alpha: int | float) -> None:
        if self.address:
            self._memory.write_float(self.address + self._memory.m_flFlashMaxAlpha, float(alpha))

    @property
    def view_angles(self) -> Vector:
        return Vector.from_address(self._memory, self._memory.client_address + self._memory.dwViewAngles)

    @view_angles.setter
    def view_angles(self, value: Vector) -> None:
        angles = struct.pack('3f', *value)
        self._memory.write_bytes(self._memory.client_address + self._memory.dwViewAngles, angles, Vector.SIZE)
