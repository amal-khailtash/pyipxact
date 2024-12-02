from collections.abc import Iterable
from dataclasses import dataclass, field
from typing import Optional

from org.accellera.spirit.v1_5.abstractor_bus_interface_type import (
    AbstractorBusInterfaceType,
)
from org.accellera.spirit.v1_5.abstractor_generators import (
    AbstractorGenerators,
)
from org.accellera.spirit.v1_5.abstractor_mode_type import AbstractorModeType
from org.accellera.spirit.v1_5.abstractor_model_type import AbstractorModelType
from org.accellera.spirit.v1_5.choices import Choices
from org.accellera.spirit.v1_5.description import Description
from org.accellera.spirit.v1_5.file_sets import FileSets
from org.accellera.spirit.v1_5.library_ref_type import LibraryRefType
from org.accellera.spirit.v1_5.parameters import Parameters
from org.accellera.spirit.v1_5.vendor_extensions import VendorExtensions

__NAMESPACE__ = "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.5"


@dataclass(slots=True)
class AbstractorType:
    """
    Abstractor-specific extension to abstractorType.

    :ivar vendor: Name of the vendor who supplies this file.
    :ivar library: Name of the logical library this element belongs to.
    :ivar name: The name of the object.
    :ivar version: Indicates the version of the named element.
    :ivar abstractor_mode: Define the mode for the interfaces on this
        abstractor. For master the first interface connects to the
        master, the second connects to the mirroredMaster For slave the
        first interface connects to the mirroredSlave the second
        connects to the slave For direct the first interface connects to
        the master, the second connects to the slave For system the
        first interface connects to the system, the second connects to
        the mirroredSystem. For system the group attribute is required
    :ivar bus_type: The bus type of both interfaces. Refers to bus
        definition using vendor, library, name, version attributes.
    :ivar abstractor_interfaces: The interfaces supported by this
        abstractor
    :ivar model: Model information.
    :ivar abstractor_generators: Generator list is tools-specific.
    :ivar choices:
    :ivar file_sets:
    :ivar description:
    :ivar parameters:
    :ivar vendor_extensions:
    """

    class Meta:
        name = "abstractorType"

    vendor: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.5",
            "required": True,
        },
    )
    library: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.5",
            "required": True,
        },
    )
    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.5",
            "required": True,
        },
    )
    version: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.5",
            "required": True,
        },
    )
    abstractor_mode: Optional["AbstractorType.AbstractorMode"] = field(
        default=None,
        metadata={
            "name": "abstractorMode",
            "type": "Element",
            "namespace": "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.5",
            "required": True,
        },
    )
    bus_type: Optional[LibraryRefType] = field(
        default=None,
        metadata={
            "name": "busType",
            "type": "Element",
            "namespace": "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.5",
            "required": True,
        },
    )
    abstractor_interfaces: Optional["AbstractorType.AbstractorInterfaces"] = (
        field(
            default=None,
            metadata={
                "name": "abstractorInterfaces",
                "type": "Element",
                "namespace": "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.5",
                "required": True,
            },
        )
    )
    model: Optional[AbstractorModelType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.5",
        },
    )
    abstractor_generators: Optional[AbstractorGenerators] = field(
        default=None,
        metadata={
            "name": "abstractorGenerators",
            "type": "Element",
            "namespace": "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.5",
        },
    )
    choices: Optional[Choices] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.5",
        },
    )
    file_sets: Optional[FileSets] = field(
        default=None,
        metadata={
            "name": "fileSets",
            "type": "Element",
            "namespace": "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.5",
        },
    )
    description: Optional[Description] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.5",
        },
    )
    parameters: Optional[Parameters] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.5",
        },
    )
    vendor_extensions: Optional[VendorExtensions] = field(
        default=None,
        metadata={
            "name": "vendorExtensions",
            "type": "Element",
            "namespace": "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.5",
        },
    )

    @dataclass(slots=True)
    class AbstractorMode:
        """
        :ivar value:
        :ivar group: Define the system group if the mode is set to
            system
        """

        value: Optional[AbstractorModeType] = field(
            default=None,
            metadata={
                "required": True,
            },
        )
        group: Optional[str] = field(
            default=None,
            metadata={
                "type": "Attribute",
                "namespace": "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.5",
            },
        )

    @dataclass(slots=True)
    class AbstractorInterfaces:
        """
        :ivar abstractor_interface: An abstractor must have exactly 2
            Interfaces.
        """

        abstractor_interface: Iterable[AbstractorBusInterfaceType] = field(
            default_factory=list,
            metadata={
                "name": "abstractorInterface",
                "type": "Element",
                "namespace": "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.5",
                "min_occurs": 2,
                "max_occurs": 2,
            },
        )
