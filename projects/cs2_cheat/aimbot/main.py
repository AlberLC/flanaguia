from collections.abc import Iterator

from models.aim_target import AimTarget
from models.memory import Memory
from models.entities.local_player import LocalPlayer
from models.entities.player import Player

...


def iter_players() -> Iterator[Player]:
    for entity in memory.full_entity_list.iter_entities_by_class('cs_player_controller'):
        player_ = Player.from_controller_address(memory, entity.address)

        if player_ and player_.team is not local_player.team:
            yield player_


memory = Memory()
local_player_address = memory.read_ulonglong(memory.client_address + memory.dwLocalPlayerPawn)
local_player = LocalPlayer(memory, local_player_address)

while True:
    print(local_player.view_position)
    closest_target = AimTarget(distance=float('inf'))

    for player in iter_players():
        player.glow()

        ...

    ...
