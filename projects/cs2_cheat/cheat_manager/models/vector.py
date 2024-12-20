from __future__ import annotations

import math
import struct
from collections.abc import Iterator
from typing import Any, Self

import constants
from models.memory import Memory


class Vector:
    SIZE = 3 * constants.FLOAT_SIZE

    def __init__(self, x: float, y: float, z: float) -> None:
        self.x = x
        self.y = y
        self.z = z

    def __add__(self, other: Any) -> Self:
        if not isinstance(other, type(self)):
            return NotImplemented

        return type(self)(self.x + other.x, self.y + other.y, self.z + other.z)

    def __eq__(self, other: Any) -> bool:
        return isinstance(other, type(self)) and vars(self) == vars(other)

    def __iter__(self) -> Iterator[float]:
        yield from vars(self).values()

    def __mul__(self, number: int | float) -> Self:
        self.x *= number
        self.y *= number
        self.z *= number

        return self

    def __rmul__(self, number: int | float) -> Self:
        return self * number

    def __str__(self) -> str:
        return f'Vector({self.x}, {self.y}, {self.z})'

    def __sub__(self, other: Any) -> Self:
        if not isinstance(other, type(self)):
            return NotImplemented

        return type(self)(self.x - other.x, self.y - other.y, self.z - other.z)

    def __truediv__(self, number: int | float) -> Self:
        self.x /= number
        self.y /= number
        self.z /= number

        return self

    def __rtruediv__(self, number: int | float) -> Self:
        return self / number

    def angles_to_direction(self) -> Self:
        x = math.cos(math.radians(self.x)) * math.cos(math.radians(self.y))
        y = math.cos(math.radians(self.x)) * math.sin(math.radians(self.y))
        z = -math.sin(math.radians(self.x))
        return Vector(x, y, z)

    def direction_to_angles(self) -> Self:
        return type(self)(
            math.degrees(math.atan2(-self.z, math.hypot(self.x, self.y))),
            math.degrees(math.atan2(self.y, self.x)),
            0.0
        )

    def distance(self, other: Vector) -> float:
        return (other - self).magnitude

    @classmethod
    def from_address(cls, memory: Memory, address: int) -> Self:
        coordinates = struct.unpack('3f', memory.read_bytes(address, Vector.SIZE))
        return cls(*coordinates)

    @property
    def is_in_origin(self) -> bool:
        return all(math.isclose(coordinate, 0, abs_tol=0.01) for coordinate in self)

    @property
    def magnitude(self) -> float:
        return math.hypot(*self)

    def normalize(self) -> Self:
        return self / self.magnitude

    def world_to_screen(
        self,
        view_matrix: constants.FloatTuple16,
        screen_size: tuple[int, int]
    ) -> tuple[int, int] | None:
        z = self.x * view_matrix[12] + self.y * view_matrix[13] + self.z * view_matrix[14] + view_matrix[15]

        if z < constants.MIN_SCREEN_Z:
            return

        x = self.x * view_matrix[0] + self.y * view_matrix[1] + self.z * view_matrix[2] + view_matrix[3]
        y = self.x * view_matrix[4] + self.y * view_matrix[5] + self.z * view_matrix[6] + view_matrix[7]

        central_x = screen_size[0] / 2
        central_y = screen_size[1] / 2

        screen_x = round(central_x + (central_x * x / z))
        screen_y = round(central_y - (central_y * y / z))

        return screen_x, screen_y
