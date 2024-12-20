from models.cheat_manager import CheatManager
from models.config import Config

config = Config(
    aimbot_button='alt',
    aimbot_max_distance=3
)

CheatManager(config).run()
