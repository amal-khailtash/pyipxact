from collections.abc import Iterable
from dataclasses import dataclass, field

from org.accellera.ipxact.v1685_2014.ipxact_file_type import IpxactFileType

__NAMESPACE__ = "http://www.accellera.org/XMLSchema/IPXACT/1685-2014"


@dataclass(slots=True)
class IpxactFilesType:
    """
    Contains a list of IP-XACT files to include.
    """

    class Meta:
        name = "ipxactFilesType"

    ipxact_file: Iterable[IpxactFileType] = field(
        default_factory=list,
        metadata={
            "name": "ipxactFile",
            "type": "Element",
            "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2014",
            "min_occurs": 1,
        },
    )
