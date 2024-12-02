from enum import Enum

__NAMESPACE__ = "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1685-2009"


class TestableTestConstraint(Enum):
    UNCONSTRAINED = "unconstrained"
    RESTORE = "restore"
    WRITE_AS_READ = "writeAsRead"
    READ_ONLY = "readOnly"
