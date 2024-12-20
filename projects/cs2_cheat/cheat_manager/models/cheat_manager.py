from collections.abc import Iterator

import keyboard
import mouse

from models.aim_target import AimTarget
from models.config import Config
from models.entities.local_player import LocalPlayer
from models.entities.player import Player
from models.memory import Memory


class CheatManager:
    def __init__(self, config: Config) -> None:
        self._config = config
        self._memory = Memory()
        local_player_address = self._memory.read_ulonglong(self._memory.client_address + self._memory.dwLocalPlayerPawn)
        self._local_player = LocalPlayer(self._memory, local_player_address)
        self._button_is_pressed = False

        self._create_button_hook()

    def _create_button_hook(self) -> None:
        def on_button(event: mouse.ButtonEvent | mouse.MoveEvent | mouse.WheelEvent | keyboard.KeyboardEvent) -> None:
            # noinspection PyUnresolvedReferences
            match event:
                case (
                mouse.ButtonEvent(event_type=mouse.DOWN | mouse.DOUBLE, button=self._config.aimbot_button)
                |
                keyboard.KeyboardEvent(event_type=keyboard.KEY_DOWN, name=self._config.aimbot_button)
                ):
                    self._button_is_pressed = True
                case (
                mouse.ButtonEvent(event_type=mouse.UP, button=self._config.aimbot_button)
                |
                keyboard.KeyboardEvent(event_type=keyboard.KEY_UP, name=self._config.aimbot_button)
                ):
                    self._button_is_pressed = False

        def on_mouse_press() -> None:
            self._local_player.is_shooting = True

        def on_mouse_release() -> None:
            self._local_player.is_shooting = False

        match self._config.aimbot_button:
            case mouse.LEFT | mouse.RIGHT | mouse.MIDDLE | mouse.X | mouse.X2:
                mouse.hook(on_button)
            case str(key):
                keyboard.hook_key(key, on_button)

        mouse.on_button(on_mouse_press, buttons=(mouse.LEFT,), types=(mouse.DOWN,))
        mouse.on_double_click(on_mouse_press)
        mouse.on_button(on_mouse_release, buttons=(mouse.LEFT,), types=(mouse.UP,))

    def _iter_players(self) -> Iterator[Player]:
        for entity in self._memory.full_entity_list.iter_entities_by_class('cs_player_controller'):
            player_ = Player.from_controller_address(self._memory, entity.address)

            if player_ and player_.team is not self._local_player.team:
                yield player_

    def run(self) -> None:
        while True:
            closest_target = AimTarget(distance=float('inf'))

            for player in self._iter_players():
                player.glow()

                if player.health:
                    target = self._local_player.get_angular_target(player)
                    if target and target.distance < closest_target.distance:
                        closest_target = target

            if (
                ...
                closest_target
                and
                closest_target.distance <= self._config.aimbot_max_distance
            ):
                self._local_player.aim_at(closest_target.position)
