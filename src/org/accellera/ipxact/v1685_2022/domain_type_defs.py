from collections.abc import Iterable
from dataclasses import dataclass, field

from org.accellera.ipxact.v1685_2022.domain_type_def import DomainTypeDef

__NAMESPACE__ = "http://www.accellera.org/XMLSchema/IPXACT/1685-2022"


@dataclass(slots=True)
class DomainTypeDefs:
    """
    The group of domain type definitions.
    """

    class Meta:
        name = "domainTypeDefs"
        namespace = "http://www.accellera.org/XMLSchema/IPXACT/1685-2022"

    domain_type_def: Iterable[DomainTypeDef] = field(
        default_factory=list,
        metadata={
            "name": "domainTypeDef",
            "type": "Element",
            "min_occurs": 1,
        },
    )
