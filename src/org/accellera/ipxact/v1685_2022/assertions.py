from collections.abc import Iterable
from dataclasses import dataclass, field

from org.accellera.ipxact.v1685_2022.assertion import Assertion

__NAMESPACE__ = "http://www.accellera.org/XMLSchema/IPXACT/1685-2022"


@dataclass(slots=True)
class Assertions:
    """
    List of assertions about allowed parameter values.
    """

    class Meta:
        name = "assertions"
        namespace = "http://www.accellera.org/XMLSchema/IPXACT/1685-2022"

    assertion: Iterable[Assertion] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )