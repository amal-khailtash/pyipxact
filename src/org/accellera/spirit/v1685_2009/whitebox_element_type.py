from dataclasses import dataclass, field
from typing import Optional

from org.accellera.spirit.v1685_2009.description import Description
from org.accellera.spirit.v1685_2009.display_name import DisplayName
from org.accellera.spirit.v1685_2009.parameters import Parameters
from org.accellera.spirit.v1685_2009.vendor_extensions import VendorExtensions
from org.accellera.spirit.v1685_2009.whitebox_element_type_whitebox_type import (
    WhiteboxElementTypeWhiteboxType,
)

__NAMESPACE__ = "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1685-2009"


@dataclass(slots=True)
class WhiteboxElementType:
    """
    Defines a white box reference point within the component.

    :ivar name: Unique name
    :ivar display_name:
    :ivar description:
    :ivar whitebox_type: Indicates the type of the element. The pin and
        signal types refer to elements within the HDL description. The
        register type refers to a register in the memory map. The
        interface type refers to a group of signals addressed as a
        single unit.
    :ivar driveable: If true, indicates that the white box element can
        be driven (e.g. have a new value forced into it).
    :ivar register_ref: Indicates the name of the register associated
        with this white box element. The name should be a full
        hierarchical path from the memory map to the register, using '/'
        as a hierarchy separator.  When specified, the whiteboxType must
        be 'register'.
    :ivar parameters:
    :ivar vendor_extensions:
    """

    class Meta:
        name = "whiteboxElementType"

    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1685-2009",
            "required": True,
        },
    )
    display_name: Optional[DisplayName] = field(
        default=None,
        metadata={
            "name": "displayName",
            "type": "Element",
            "namespace": "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1685-2009",
        },
    )
    description: Optional[Description] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1685-2009",
        },
    )
    whitebox_type: Optional[WhiteboxElementTypeWhiteboxType] = field(
        default=None,
        metadata={
            "name": "whiteboxType",
            "type": "Element",
            "namespace": "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1685-2009",
            "required": True,
        },
    )
    driveable: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1685-2009",
        },
    )
    register_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "registerRef",
            "type": "Element",
            "namespace": "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1685-2009",
        },
    )
    parameters: Optional[Parameters] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1685-2009",
        },
    )
    vendor_extensions: Optional[VendorExtensions] = field(
        default=None,
        metadata={
            "name": "vendorExtensions",
            "type": "Element",
            "namespace": "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1685-2009",
        },
    )
