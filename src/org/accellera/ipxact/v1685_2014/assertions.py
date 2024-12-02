from collections.abc import Iterable
from dataclasses import dataclass, field

from org.accellera.ipxact.v1685_2014.assertion import Assertion

__NAMESPACE__ = "http://www.accellera.org/XMLSchema/IPXACT/1685-2014"


@dataclass(slots=True)
class Assertions:
    """
    List of assertions about allowed parameter values.
    """

    class Meta:
        name = "assertions"
        namespace = "http://www.accellera.org/XMLSchema/IPXACT/1685-2014"

    assertion: Iterable[Assertion] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
