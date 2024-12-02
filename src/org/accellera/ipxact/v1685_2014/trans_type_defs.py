from collections.abc import Iterable
from dataclasses import dataclass, field

from org.accellera.ipxact.v1685_2014.trans_type_def import TransTypeDef

__NAMESPACE__ = "http://www.accellera.org/XMLSchema/IPXACT/1685-2014"


@dataclass(slots=True)
class TransTypeDefs:
    """The group of transactional type definitions.

    If no match to a viewName is found then the default language types
    are to be used. See the User Guide for these default types.
    """

    class Meta:
        name = "transTypeDefs"
        namespace = "http://www.accellera.org/XMLSchema/IPXACT/1685-2014"

    trans_type_def: Iterable[TransTypeDef] = field(
        default_factory=list,
        metadata={
            "name": "transTypeDef",
            "type": "Element",
            "min_occurs": 1,
        },
    )
