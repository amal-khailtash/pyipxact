from collections.abc import Iterable
from dataclasses import dataclass, field

from org.accellera.spirit.v1_5.service_type_def import ServiceTypeDef

__NAMESPACE__ = "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.5"


@dataclass(slots=True)
class ServiceTypeDefs:
    """The group of type definitions.

    If no match to a viewName is found then the default language types
    are to be used. See the User Guide for these default types.
    """

    class Meta:
        name = "serviceTypeDefs"
        namespace = "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.5"

    service_type_def: Iterable[ServiceTypeDef] = field(
        default_factory=list,
        metadata={
            "name": "serviceTypeDef",
            "type": "Element",
            "min_occurs": 1,
        },
    )
