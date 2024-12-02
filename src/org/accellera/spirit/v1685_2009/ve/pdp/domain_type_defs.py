from collections.abc import Iterable
from dataclasses import dataclass, field

from org.accellera.spirit.v1685_2009.ve.pdp.domain_type_def import (
    DomainTypeDef,
)

__NAMESPACE__ = (
    "http://www.accellera.org/XMLSchema/SPIRIT/1685-2009-VE/AMS-1.0"
)


@dataclass(slots=True)
class DomainTypeDefs:
    """The group of domain type definitions.

    If no match to a viewName is found then the default language types
    are to be used. See the User Guide for these default types.

    :ivar domain_type_def: Definition of a single domain type definition
        that can relate to multiple views.
    """

    class Meta:
        name = "domainTypeDefs"
        namespace = (
            "http://www.accellera.org/XMLSchema/SPIRIT/1685-2009-VE/AMS-1.0"
        )

    domain_type_def: Iterable[DomainTypeDef] = field(
        default_factory=list,
        metadata={
            "name": "domainTypeDef",
            "type": "Element",
            "min_occurs": 1,
        },
    )
