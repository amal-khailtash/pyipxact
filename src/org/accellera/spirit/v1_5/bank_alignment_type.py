from enum import Enum

__NAMESPACE__ = "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.5"


class BankAlignmentType(Enum):
    """
    'serial' or 'parallel' bank alignment.
    """

    SERIAL = "serial"
    PARALLEL = "parallel"