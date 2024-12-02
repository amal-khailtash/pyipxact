from collections.abc import Iterable
from dataclasses import dataclass, field

from org.accellera.ipxact.v1685_2022.port_slice_type import PortSliceType

__NAMESPACE__ = "http://www.accellera.org/XMLSchema/IPXACT/1685-2022"


@dataclass(slots=True)
class PortSlicesType:
    """Each slice specifies the HDL path for part of the parent IP-XACT object.

    The slices must be concatenated to calculate the entire path. If
    there is only one slice, it is assumed to be the path for the entire
    IP-XACT object.

    :ivar slice: The HDL path for a slice of the IP-XACT object.
    """

    class Meta:
        name = "portSlicesType"

    slice: Iterable[PortSliceType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2022",
            "min_occurs": 1,
        },
    )
