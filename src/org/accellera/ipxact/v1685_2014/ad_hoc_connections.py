from collections.abc import Iterable
from dataclasses import dataclass, field

from org.accellera.ipxact.v1685_2014.ad_hoc_connection import AdHocConnection

__NAMESPACE__ = "http://www.accellera.org/XMLSchema/IPXACT/1685-2014"


@dataclass(slots=True)
class AdHocConnections:
    """Defines the set of ad-hoc connections in a design.

    An ad-hoc connection represents a connection between two component
    pins which were not connected as a result of interface connections
    (i.e.the pin to pin connection was made explicitly and is
    represented explicitly).
    """

    class Meta:
        name = "adHocConnections"
        namespace = "http://www.accellera.org/XMLSchema/IPXACT/1685-2014"

    ad_hoc_connection: Iterable[AdHocConnection] = field(
        default_factory=list,
        metadata={
            "name": "adHocConnection",
            "type": "Element",
            "min_occurs": 1,
        },
    )
