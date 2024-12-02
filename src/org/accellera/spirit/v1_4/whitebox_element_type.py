from dataclasses import dataclass, field
from typing import Optional

from org.accellera.spirit.v1_4.parameters import Parameters
from org.accellera.spirit.v1_4.vendor_extensions import VendorExtensions
from org.accellera.spirit.v1_4.whitebox_element_type_whitebox_type import (
    WhiteboxElementTypeWhiteboxType,
)

__NAMESPACE__ = "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.4"


@dataclass(slots=True)
class WhiteboxElementType:
    """
    Defines a white box reference point within the component.

    :ivar name: Unique name
    :ivar display_name: Element name for display purposes. Typically a
        few words providing a more detailed and/or user-friendly name
        than the spirit:name.
    :ivar description: Full description string, typically for
        documentation
    :ivar whitebox_type: Indicates the type of the element. The pin and
        signal types refer to elements within the HDL description. The
        register type refers to a register in the memory map. The
        interface type refers to a bus interface in a lower level
        component definition.
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
            "namespace": "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.4",
            "required": True,
        },
    )
    display_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "displayName",
            "type": "Element",
            "namespace": "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.4",
        },
    )
    description: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.4",
        },
    )
    whitebox_type: Optional[WhiteboxElementTypeWhiteboxType] = field(
        default=None,
        metadata={
            "name": "whiteboxType",
            "type": "Element",
            "namespace": "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.4",
            "required": True,
        },
    )
    driveable: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.4",
        },
    )
    register_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "registerRef",
            "type": "Element",
            "namespace": "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.4",
        },
    )
    parameters: Optional[Parameters] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.4",
        },
    )
    vendor_extensions: Optional[VendorExtensions] = field(
        default=None,
        metadata={
            "name": "vendorExtensions",
            "type": "Element",
            "namespace": "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.4",
        },
    )
