from enum import Enum

__NAMESPACE__ = (
    "http://www.accellera.org/XMLSchema/SPIRIT/1685-2009-VE/CORE-1.0"
)


class PrefixValue(Enum):
    DECA = "deca"
    HECTO = "hecto"
    KILO = "kilo"
    MEGA = "mega"
    GIGA = "giga"
    TERA = "tera"
    PETA = "peta"
    EXA = "exa"
    ZETTA = "zetta"
    YOTTA = "yotta"
    DECI = "deci"
    CENTI = "centi"
    MILLI = "milli"
    MICRO = "micro"
    NANO = "nano"
    PICO = "pico"
    FEMTO = "femto"
    ATTO = "atto"
    ZEPTO = "zepto"
    YOCTO = "yocto"
