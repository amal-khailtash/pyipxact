from dataclasses import dataclass, field
from typing import Optional

from org.accellera.ipxact.v1685_2022.unresolved_string_expression import (
    UnresolvedStringExpression,
)

__NAMESPACE__ = "http://www.accellera.org/XMLSchema/IPXACT/1685-2022"


@dataclass(slots=True)
class PathSegmentType(UnresolvedStringExpression):
    """Identifies one level of hierarchy in the view specifed by viewNameRef.

    This is a simple name and optionally some indices into a multi
    dimensional element.
    """

    class Meta:
        name = "pathSegmentType"

    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )
