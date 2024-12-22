import pathlib

type FloatTuple16 = tuple[
    float, float, float, float, float, float, float, float, float, float, float, float, float, float, float, float
]

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
