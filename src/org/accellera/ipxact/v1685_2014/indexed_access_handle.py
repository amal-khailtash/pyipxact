from collections.abc import Iterable
from dataclasses import dataclass, field
from typing import Optional

from org.accellera.ipxact.v1685_2014.path_segment_type import PathSegmentType
from org.accellera.ipxact.v1685_2014.unsigned_int_expression import (
    UnsignedIntExpression,
)

__NAMESPACE__ = "http://www.accellera.org/XMLSchema/IPXACT/1685-2014"


@dataclass(slots=True)
class IndexedAccessHandle:
    """
    :ivar view_ref: A list of views this accessHandle is applicable to.
        Note this element is optional, if it is not present the
        accessHandle applies to all views.
    :ivar indices: For a multi dimensional IP-XACT object, indices can
        be specified to select the element the accessHandle applies to.
        This is an index into a multi-dimensional array and follows
        C-semantics for indexing.
    :ivar path_segments: An ordered list of pathSegment elements. When
        concatenated with a desired separator the elements in this form
        a HDL path for the parent slice into the referenced view.
    :ivar id:
    """

    class Meta:
        name = "indexedAccessHandle"

    view_ref: Iterable["IndexedAccessHandle.ViewRef"] = field(
        default_factory=list,
        metadata={
            "name": "viewRef",
            "type": "Element",
            "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2014",
        },
    )
    indices: Optional["IndexedAccessHandle.Indices"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2014",
        },
    )
    path_segments: Optional["IndexedAccessHandle.PathSegments"] = field(
        default=None,
        metadata={
            "name": "pathSegments",
            "type": "Element",
            "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2014",
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

    @dataclass(slots=True)
    class ViewRef:
        value: str = field(
            default="",
            metadata={
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

    @dataclass(slots=True)
    class Indices:
        """
        :ivar index: An index into the IP-XACT object.
        """

        index: Iterable[UnsignedIntExpression] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2014",
                "min_occurs": 1,
            },
        )

    @dataclass(slots=True)
    class PathSegments:
        path_segment: Iterable[PathSegmentType] = field(
            default_factory=list,
            metadata={
                "name": "pathSegment",
                "type": "Element",
                "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2014",
                "min_occurs": 1,
            },
        )
