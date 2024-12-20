from collections.abc import Iterator

import constants
from models.memory import Memory
from models.entities.local_player import LocalPlayer
from models.entities.player import Player


def iter_players() -> Iterator[Player]:
    for i in range(1, constants.MAX_PLAYERS):
        entity = memory.get_entity_from_entity_index(i)
        if not entity:
            continue

        player_ = Player.from_controller_address(memory, entity.address)

        if player_ and player_.team is not local_player.team:
            yield player_


memory = Memory()
local_player_address = memory.read_ulonglong(memory.client_address + memory.dwLocalPlayerPawn)
local_player = LocalPlayer(memory, local_player_address)

while True:
    for player in iter_players():
        player.glow()
