from collections.abc import Iterator

from models.aim_target import AimTarget
from models.memory import Memory
from models.entities.local_player import LocalPlayer
from models.entities.player import Player

AIMBOT_MAX_DISTANCE = 2


def iter_players() -> Iterator[Player]:
    for entity in memory.full_entity_list.iter_entities_by_class('cs_player_controller'):
        player_ = Player.from_controller_address(memory, entity.address)

        if player_ and player_.team is not local_player.team:
            yield player_


memory = Memory()
local_player_address = memory.read_ulonglong(memory.client_address + memory.dwLocalPlayerPawn)
local_player = LocalPlayer(memory, local_player_address)

while True:
    closest_target = AimTarget(distance=float('inf'))

    for player in iter_players():
        player.glow()

        if player.health:
            target = local_player.get_angular_target(player)
            if target and target.distance < closest_target.distance:
                closest_target = target

    if closest_target and closest_target.distance <= AIMBOT_MAX_DISTANCE:
        local_player.aim_at(closest_target.position)
