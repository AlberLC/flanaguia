from dataclasses import dataclass

from models.enums import Bone


@dataclass
class Config:
    bones: tuple[Bone, ...] = (Bone.PELVIS, Bone.NECK, Bone.HEAD, Bone.LEFT_SHOULDER, Bone.LEFT_ELBOW, Bone.LEFT_WRIST,
                               Bone.LEFT_HAND, Bone.RIGHT_SHOULDER, Bone.RIGHT_ELBOW, Bone.RIGHT_WRIST, Bone.RIGHT_HAND,
                               Bone.LEFT_HIP, Bone.LEFT_KNEE, Bone.LEFT_ANKLE, Bone.LEFT_FOOT, Bone.RIGHT_HIP,
                               Bone.RIGHT_KNEE, Bone.RIGHT_ANKLE, Bone.RIGHT_FOOT)
    font_size: int = 20
    aimbot_max_distance: float = float('inf')
    aimbot_button: str | None = None
    flash_alpha: int = 255
