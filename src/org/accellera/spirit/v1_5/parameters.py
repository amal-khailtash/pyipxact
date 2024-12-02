from collections.abc import Iterable
from dataclasses import dataclass, field

from org.accellera.spirit.v1_5.parameter import Parameter

__NAMESPACE__ = "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.5"


@dataclass(slots=True)
class Parameters:
    """
    A collection of parameters.
    """

    class Meta:
        name = "parameters"
        namespace = "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.5"

    parameter: Iterable[Parameter] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 1,
        },
    )
