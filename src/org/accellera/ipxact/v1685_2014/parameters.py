from collections.abc import Iterable
from dataclasses import dataclass, field

from org.accellera.ipxact.v1685_2014.parameter import Parameter

__NAMESPACE__ = "http://www.accellera.org/XMLSchema/IPXACT/1685-2014"


@dataclass(slots=True)
class Parameters:
    """
    A collection of parameters and associated value assertions.
    """

    class Meta:
        name = "parameters"
        namespace = "http://www.accellera.org/XMLSchema/IPXACT/1685-2014"

    parameter: Iterable[Parameter] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 1,
        },
    )