from enum import Enum

__NAMESPACE__ = "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.1"


class UsageType(Enum):
    """
    Describes the usage of an address block.

    :cvar MEMORY: Denotes an address range that can be used for read-
        write or read-only data storage.
    :cvar REGISTER: Denotes an address block that is used to communicate
        with hardware.
    :cvar RESERVED: Denotes an address range that must remain
        unoccupied.
    """

    MEMORY = "memory"
    REGISTER = "register"
    RESERVED = "reserved"
