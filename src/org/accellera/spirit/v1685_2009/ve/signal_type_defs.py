from collections.abc import Iterable
from dataclasses import dataclass, field

from org.accellera.spirit.v1685_2009.ve.signal_type_def import SignalTypeDef

__NAMESPACE__ = (
    "http://www.accellera.org/XMLSchema/SPIRIT/1685-2009-VE/AMS-1.0"
)


@dataclass(slots=True)
class SignalTypeDefs:
    """The group of signal type definitions.

    If no match to a viewName is found then the signal type defaults to
    discrete.

    :ivar signal_type_def: Definition of a single signal type definition
        that can relate to multiple views.
    """

    class Meta:
        name = "signalTypeDefs"
        namespace = (
            "http://www.accellera.org/XMLSchema/SPIRIT/1685-2009-VE/AMS-1.0"
        )

    signal_type_def: Iterable[SignalTypeDef] = field(
        default_factory=list,
        metadata={
            "name": "signalTypeDef",
            "type": "Element",
            "min_occurs": 1,
        },
    )
