import pathlib

from models.enums import Bone

type FloatTuple16 = tuple[
    float, float, float, float, float, float, float, float, float, float, float, float, float, float, float, float
]

BONE_ARRAY_PADDING = 128
BONE_DATA_SIZE = 32
CONCRETE_ENTITY_LIST_PADDING = 16
CS_CLIENT_DLL_NAME = 'client.dll'
CS_PROCESS_NAME = 'cs2.exe'
ENTITY_LISTS = 64
FIRST_ACTIVE_ENTITY_PADDING = 512
FLOAT_SIZE = 4
IDENTITY_SIZE = 120
LIST_ENTITIES = 512
MAX_ENTITIES = LIST_ENTITIES * ENTITY_LISTS
MAX_PLAYERS = 64
MIN_SCREEN_Z = 0.001
UNSIGNED_LONG_LONG_SIZE = 8
WAIT_FOR_PROCESS_SLEEP_SECONDS = 10

ENDPOINTS = {
    'client_offsets': 'https://raw.githubusercontent.com/a2x/cs2-dumper/refs/heads/main/output/client_dll.json',
    'cs2_dumper_github_commits': 'https://api.github.com/repos/a2x/cs2-dumper/commits',
    'general_offsets': 'https://raw.githubusercontent.com/a2x/cs2-dumper/refs/heads/main/output/offsets.json'
}

CLIENT_OFFSETS_PATH = pathlib.Path('markdown_resources/offsets/client_offsets.json')
GENERAL_OFFSETS_PATH = pathlib.Path('markdown_resources/offsets/general_offsets.json')
LAST_UPDATE_DATE_PATH = pathlib.Path('markdown_resources/offsets/last_update_date.txt')

REQUIRED_OFFSET_CLASSES = {'CBasePlayerController', 'CCSPlayerBase_CameraServices', 'CCSWeaponBaseVData',
                           'CEntityIdentity', 'CEntityInstance', 'CGameSceneNode', 'CGlowProperty',
                           'CPlayer_ObserverServices', 'CSkeletonInstance', 'C_AttributeContainer', 'C_BaseEntity',
                           'C_BaseModelEntity', 'C_BasePlayerPawn', 'C_CSPlayerPawn', 'C_CSPlayerPawnBase',
                           'C_EconEntity', 'C_EconItemView', 'C_SmokeGrenadeProjectile', 'EntitySpottedState_t'}

SKELETON = {
    'base': {
        Bone.PELVIS: 0,
        Bone.VERTEBRA_4: 1,
        Bone.VERTEBRA_3: 2,
        Bone.VERTEBRA_2: 3,
        Bone.VERTEBRA_1: 4,
        Bone.NECK: 5,
        Bone.HEAD: 6,
        Bone.LEFT_SHOULDER: 8,
        Bone.LEFT_ELBOW: 9,
        Bone.LEFT_WRIST: 10,
        Bone.LEFT_HAND: 11,
        Bone.RIGHT_SHOULDER: 13,
        Bone.RIGHT_ELBOW: 14,
        Bone.RIGHT_WRIST: 15,
        Bone.RIGHT_HAND: 16,
        Bone.LEFT_HIP: 22,
        Bone.LEFT_KNEE: 23,
        Bone.LEFT_ANKLE: 24,
        Bone.RIGHT_HIP: 25,
        Bone.RIGHT_KNEE: 26,
        Bone.RIGHT_ANKLE: 27
    },
    'counter_terrorist': {
        Bone.LEFT_FOOT: 104,
        Bone.RIGHT_FOOT: 109
    },
    'terrorist': {
        Bone.LEFT_FOOT: 98,
        Bone.RIGHT_FOOT: 101
    }
}