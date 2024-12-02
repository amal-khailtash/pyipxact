from enum import Enum

__NAMESPACE__ = (
    "http://www.accellera.org/XMLSchema/SPIRIT/1685-2009-VE/AMS-1.0"
)


class SignalType1(Enum):
    """
    The signal type of a component port.
    """

    CONTINUOUS_CONSERVATIVE = "continuous-conservative"
    CONTINUOUS_NON_CONSERVATIVE = "continuous-non-conservative"
    DISCRETE = "discrete"
