from models.entities.player import Player
from models.memory import Memory


class LocalPlayer(Player):
    def __init__(self, memory: Memory, address: int, controller_address: int | None = None) -> None:
        super().__init__(memory, address, controller_address)
        self.is_shooting = False

    ...  # set_flash_alpha
