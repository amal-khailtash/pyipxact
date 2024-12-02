from collections.abc import Iterable
from dataclasses import dataclass, field
from typing import Optional

from org.accellera.ipxact.v1685_2014.is_present import IsPresent
from org.accellera.ipxact.v1685_2014.slices_type import SlicesType

__NAMESPACE__ = "http://www.accellera.org/XMLSchema/IPXACT/1685-2014"


@dataclass(slots=True)
class WhiteboxElementRefType:
    """Reference to a whiteboxElement within a view.

    The 'name' attribute must refer to a whiteboxElement defined within
    this component.

    :ivar is_present:
    :ivar location: The contents of each location element can be used to
        specified one location (HDL Path) through the referenced
        whiteBoxElement is accessible.
    :ivar name: Reference to a whiteboxElement defined within this
        component.
    :ivar id:
    """

    class Meta:
        name = "whiteboxElementRefType"

    is_present: Optional[IsPresent] = field(
        default=None,
        metadata={
            "name": "isPresent",
            "type": "Element",
            "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2014",
        },
    )
    location: Iterable[SlicesType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2014",
            "min_occurs": 1,
        },
    )
    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )
