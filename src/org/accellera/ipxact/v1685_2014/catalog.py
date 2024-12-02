from dataclasses import dataclass, field
from typing import Optional

from org.accellera.ipxact.v1685_2014.description import Description
from org.accellera.ipxact.v1685_2014.ipxact_files_type import IpxactFilesType
from org.accellera.ipxact.v1685_2014.vendor_extensions import VendorExtensions

__NAMESPACE__ = "http://www.accellera.org/XMLSchema/IPXACT/1685-2014"


@dataclass(slots=True)
class Catalog:
    """
    :ivar vendor: Name of the vendor who supplies this file.
    :ivar library: Name of the logical library this element belongs to.
    :ivar name: The name of the object.
    :ivar version: Indicates the version of the named element.
    :ivar description:
    :ivar catalogs:
    :ivar bus_definitions:
    :ivar abstraction_definitions:
    :ivar components:
    :ivar abstractors:
    :ivar designs:
    :ivar design_configurations:
    :ivar generator_chains:
    :ivar vendor_extensions:
    """

    class Meta:
        name = "catalog"
        namespace = "http://www.accellera.org/XMLSchema/IPXACT/1685-2014"

    vendor: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    library: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    version: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    description: Optional[Description] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    catalogs: Optional[IpxactFilesType] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    bus_definitions: Optional[IpxactFilesType] = field(
        default=None,
        metadata={
            "name": "busDefinitions",
            "type": "Element",
        },
    )
    abstraction_definitions: Optional[IpxactFilesType] = field(
        default=None,
        metadata={
            "name": "abstractionDefinitions",
            "type": "Element",
        },
    )
    components: Optional[IpxactFilesType] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    abstractors: Optional[IpxactFilesType] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    designs: Optional[IpxactFilesType] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    design_configurations: Optional[IpxactFilesType] = field(
        default=None,
        metadata={
            "name": "designConfigurations",
            "type": "Element",
        },
    )
    generator_chains: Optional[IpxactFilesType] = field(
        default=None,
        metadata={
            "name": "generatorChains",
            "type": "Element",
        },
    )
    vendor_extensions: Optional[VendorExtensions] = field(
        default=None,
        metadata={
            "name": "vendorExtensions",
            "type": "Element",
        },
    )
