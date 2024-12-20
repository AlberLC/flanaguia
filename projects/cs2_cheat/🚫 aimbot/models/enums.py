from enum import Enum, auto


class Bone(Enum):
    PELVIS = auto()
    VERTEBRA_4 = auto()
    VERTEBRA_3 = auto()
    VERTEBRA_2 = auto()
    VERTEBRA_1 = auto()
    NECK = auto()
    HEAD = auto()
    LEFT_SHOULDER = auto()
    LEFT_ELBOW = auto()
    LEFT_WRIST = auto()
    LEFT_HAND = auto()
    RIGHT_SHOULDER = auto()
    RIGHT_ELBOW = auto()
    RIGHT_WRIST = auto()
    RIGHT_HAND = auto()
    LEFT_HIP = auto()
    LEFT_KNEE = auto()
    LEFT_ANKLE = auto()
    LEFT_FOOT = auto()
    RIGHT_HIP = auto()
    RIGHT_KNEE = auto()
    RIGHT_ANKLE = auto()
    RIGHT_FOOT = auto()


class Team(Enum):
    SPECTATOR = auto()
    TERRORIST = auto()
    COUNTER_TERRORIST = auto()
