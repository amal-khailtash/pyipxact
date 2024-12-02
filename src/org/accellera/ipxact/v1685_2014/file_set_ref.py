from dataclasses import dataclass, field
from typing import Optional

from org.accellera.ipxact.v1685_2014.is_present import IsPresent

__NAMESPACE__ = "http://www.accellera.org/XMLSchema/IPXACT/1685-2014"


@dataclass(slots=True)
class FileSetRef:
    """
    A reference to a fileSet.

    :ivar local_name: Refers to a fileSet defined within this
        description.
    :ivar is_present:
    :ivar id:
    """

    class Meta:
        name = "fileSetRef"
        namespace = "http://www.accellera.org/XMLSchema/IPXACT/1685-2014"

    local_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "localName",
            "type": "Element",
            "required": True,
        },
    )
    is_present: Optional[IsPresent] = field(
        default=None,
        metadata={
            "name": "isPresent",
            "type": "Element",
        },
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )
