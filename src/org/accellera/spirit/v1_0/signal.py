from dataclasses import dataclass

from org.accellera.spirit.v1_0.signal_type import SignalType

__NAMESPACE__ = "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.0"


@dataclass(slots=True)
class Signal(SignalType):
    """
    Describes signal charateristics.
    """

    class Meta:
        name = "signal"
        namespace = "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.0"