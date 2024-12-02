from dataclasses import dataclass, field
from typing import Optional

from org.accellera.ipxact.v1685_2014.indices_type import IndicesType

__NAMESPACE__ = "http://www.accellera.org/XMLSchema/IPXACT/1685-2014"


@dataclass(slots=True)
class PathSegmentType:
    """Identifies one level of hierarchy in the view specifed by viewNameRef.

    This is a simple name and optionally some indices into a multi
    dimensional element.

    :ivar path_segment_name: One section of a HDL path
    :ivar indices: Specifies a multi-dimensional index into
        pathSegementName
    :ivar id:
    """

    class Meta:
        name = "pathSegmentType"

    path_segment_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "pathSegmentName",
            "type": "Element",
            "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2014",
            "required": True,
        },
    )
    indices: Optional[IndicesType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2014",
        },
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )
