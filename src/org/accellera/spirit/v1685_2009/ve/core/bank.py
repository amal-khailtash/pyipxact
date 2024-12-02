from dataclasses import dataclass

from org.accellera.spirit.v1685_2009.ve.core.address_bank_type import (
    AddressBankType,
)

__NAMESPACE__ = "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1685-2009"


@dataclass(slots=True)
class Bank(AddressBankType):
    """Represents a bank of memory made up of address blocks or other banks.

    It has a bankAlignment attribute indicating whether its blocks are
    aligned in 'parallel' (occupying adjacent bit fields) or 'serial'
    (occupying contiguous addresses). Its child blocks do not contain
    addresses or bit offsets.
    """

    class Meta:
        name = "bank"
        namespace = (
            "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1685-2009"
        )
