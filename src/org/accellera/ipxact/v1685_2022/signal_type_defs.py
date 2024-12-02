from collections.abc import Iterable
from dataclasses import dataclass, field

from org.accellera.ipxact.v1685_2022.signal_type_def import SignalTypeDef

__NAMESPACE__ = "http://www.accellera.org/XMLSchema/IPXACT/1685-2022"


@dataclass(slots=True)
class SignalTypeDefs:
    """
    The group of signal type definitions.
    """

    class Meta:
        name = "signalTypeDefs"
        namespace = "http://www.accellera.org/XMLSchema/IPXACT/1685-2022"

    signal_type_def: Iterable[SignalTypeDef] = field(
        default_factory=list,
        metadata={
            "name": "signalTypeDef",
            "type": "Element",
            "min_occurs": 1,
        },
    )
