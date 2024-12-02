from dataclasses import dataclass

from org.accellera.spirit.v1685_2009.ve.core.address_block_type import (
    AddressBlockType,
)

__NAMESPACE__ = "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1685-2009"


@dataclass(slots=True)
class AddressBlock(AddressBlockType):
    """
    This is a single contiguous block of memory inside a memory map.
    """

    class Meta:
        name = "addressBlock"
        namespace = (
            "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1685-2009"
        )
