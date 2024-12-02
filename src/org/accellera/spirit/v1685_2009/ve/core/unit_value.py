from enum import Enum

__NAMESPACE__ = (
    "http://www.accellera.org/XMLSchema/SPIRIT/1685-2009-VE/CORE-1.0"
)


class UnitValue(Enum):
    SECOND = "second"
    AMPERE = "ampere"
    KELVIN = "kelvin"
    HERTZ = "hertz"
    JOULE = "joule"
    WATT = "watt"
    COULOMB = "coulomb"
    VOLT = "volt"
    FARAD = "farad"
    OHM = "ohm"
    SIEMENS = "siemens"
    HENRY = "henry"
    CELSIUS = "Celsius"
