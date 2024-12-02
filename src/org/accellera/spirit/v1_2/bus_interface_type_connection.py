from enum import Enum

__NAMESPACE__ = "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.2"


class BusInterfaceTypeConnection(Enum):
    """
    :cvar REQUIRED: A bus instance is automatically chosen and the
        connection is made.  Component addition fails if a suitable bus
        is not available.
    :cvar EXPLICIT: Connection of this bus interface is not made until
        the user explicitly requests connection.
    """

    REQUIRED = "required"
    EXPLICIT = "explicit"
