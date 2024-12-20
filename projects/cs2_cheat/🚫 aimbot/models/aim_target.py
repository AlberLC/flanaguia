from dataclasses import dataclass

from models.vector import Vector


@dataclass
class AimTarget:
    position: Vector | None = None
    distance: float | None = None

    def __bool__(self) -> bool:
        return bool(self.position and self.distance)
