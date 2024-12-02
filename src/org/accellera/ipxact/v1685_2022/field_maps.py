from collections.abc import Iterable
from dataclasses import dataclass, field

from org.accellera.ipxact.v1685_2022.field_map import FieldMap

__NAMESPACE__ = "http://www.accellera.org/XMLSchema/IPXACT/1685-2022"


@dataclass(slots=True)
class FieldMaps:
    """
    Listing of maps between component port slices and field slices.
    """

    class Meta:
        name = "fieldMaps"
        namespace = "http://www.accellera.org/XMLSchema/IPXACT/1685-2022"

    field_map: Iterable[FieldMap] = field(
        default_factory=list,
        metadata={
            "name": "fieldMap",
            "type": "Element",
            "min_occurs": 1,
        },
    )
