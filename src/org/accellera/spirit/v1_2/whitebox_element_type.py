from dataclasses import dataclass, field
from typing import Optional

from org.accellera.spirit.v1_2.whitebox_element_type_whitebox_type import (
    WhiteboxElementTypeWhiteboxType,
)

__NAMESPACE__ = "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.2"


@dataclass(slots=True)
class WhiteboxElementType:
    """
    Defines a white box reference point within the component.

    :ivar name: Indicates the name of the white box element. This name
        is referenced from the whiteboxElementRef inside of a view.
    :ivar whitebox_type: Indicates the type of the element. The pin and
        signal types refer to elements within the HDL description. The
        register type refers to a register in the memory map. The
        interface type refers to a bus interface in a lower level
        component definition.
    :ivar driveable: If true, indicates that the white box element can
        be driven (e.g. have a new value forced into it).
    :ivar description: Description of the white box element.
    :ivar register_ref: Indicates the name of the register associated
        with this white box element. The name must refer to a
        spirit:register defined within this component. When specified,
        the whiteboxType must be 'register'.
    """

    class Meta:
        name = "whiteboxElementType"

    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.2",
            "required": True,
        },
    )
    whitebox_type: Optional[WhiteboxElementTypeWhiteboxType] = field(
        default=None,
        metadata={
            "name": "whiteboxType",
            "type": "Element",
            "namespace": "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.2",
            "required": True,
        },
    )
    driveable: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.2",
        },
    )
    description: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.2",
        },
    )
    register_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "registerRef",
            "type": "Element",
            "namespace": "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.2",
        },
    )
