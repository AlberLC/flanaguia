import time

import pymem
from pymem.ressources.structure import MODULEINFO

import constants
from models.entities.entity import Entity
from models.entities.entity_list import EntityList
from models.offsets import Offsets


class Memory(Offsets, pymem.Pymem):
    def __init__(self, update_offsets=False) -> None:
        super().__init__(update_offsets)
        self.open_process_from_name(constants.CS_PROCESS_NAME)
        self.client_address = self._ensure_module_info(constants.CS_CLIENT_DLL_NAME).lpBaseOfDll
        game_entity_system_address = self.read_ulonglong(self.client_address + self.dwGameEntitySystem)
        self.entity_lists_address = game_entity_system_address + constants.CONCRETE_ENTITY_LIST_PADDING
        self.entity_lists: list[EntityList | None] = [None] * constants.ENTITY_LISTS
        self.entity_lists[0] = EntityList(self, self.read_ulonglong(self.entity_lists_address))

    def _ensure_module_info(self, dll_name: str) -> MODULEINFO:
        while not (address := pymem.process.module_from_name(self.process_handle, dll_name)):
            time.sleep(constants.WAIT_FOR_PROCESS_SLEEP_SECONDS)

        return address

    @property
    def full_entity_list(self) -> EntityList:
        return EntityList(self, self.read_ulonglong(self.entity_lists_address + constants.FIRST_ACTIVE_ENTITY_PADDING))

    def get_entity_address_from_handle_address(self, handle_address: int) -> int | None:
        entity_index = self.get_entity_index_from_handle_address(handle_address)
        return self.get_entity_address_from_entity_index(entity_index)

    def get_entity_address_from_entity_index(self, entity_index: int) -> int | None:
        if not (entity_list := self.get_entity_list_from_entity_index(entity_index)):
            return

        subindex = self.get_entity_subindex_from_entity_index(entity_index)
        return entity_list.get_entity_address(subindex)

    def get_entity_from_entity_index(self, entity_index: int) -> Entity | None:
        if not (entity_list := self.get_entity_list_from_entity_index(entity_index)):
            return

        subindex = self.get_entity_subindex_from_entity_index(entity_index)
        return entity_list.get_entity(subindex)

    @staticmethod
    def get_entity_index_from_handle_address(handle_address: int) -> int:
        return handle_address & constants.MAX_ENTITIES - 1  # 0x7fff 0b111111111111111

    def get_entity_list_from_entity_index(self, entity_index: int) -> EntityList:
        entity_list_index = self.get_entity_list_index_from_entity_index(entity_index)

        if not (entity_list := self.entity_lists[entity_list_index]):
            entity_list = EntityList.from_index(self, entity_list_index)
            self.entity_lists[entity_list_index] = entity_list

        return entity_list

    @staticmethod
    def get_entity_list_index_from_entity_index(entity_index: int) -> int:
        return entity_index // constants.LIST_ENTITIES

    @staticmethod
    def get_entity_subindex_from_entity_index(entity_index: int) -> int:
        return entity_index % constants.LIST_ENTITIES

    def open_process_from_name(self, process_name: str, exact_match=False, ignore_case=True) -> None:
        while True:
            try:
                super().open_process_from_name(process_name, exact_match, ignore_case)
            except pymem.exception.ProcessNotFound:
                time.sleep(constants.WAIT_FOR_PROCESS_SLEEP_SECONDS)
            else:
                break
