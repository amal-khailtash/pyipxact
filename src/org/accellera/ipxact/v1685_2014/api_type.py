from enum import Enum

__NAMESPACE__ = "http://www.accellera.org/XMLSchema/IPXACT/1685-2014"


class ApiType(Enum):
    TGI_2009 = "TGI_2009"
    TGI_2014_BASE = "TGI_2014_BASE"
    TGI_2014_EXTENDED = "TGI_2014_EXTENDED"
    NONE = "none"
