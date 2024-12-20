from collections.abc import Iterator

import constants
from models.memory import Memory
from models.entities.local_player import LocalPlayer
from models.entities.player import Player


...


memory = Memory()
local_player_address = memory.read_ulonglong(memory.client_address + memory.dwLocalPlayerPawn)
local_player = LocalPlayer(memory, local_player_address)

while True:
    for player in ...:
        player.glow()
