from collections.abc import Iterable
from dataclasses import dataclass, field
from typing import Optional

from org.accellera.spirit.v1_0.address_space_ref import AddressSpaceRef
from org.accellera.spirit.v1_0.address_spaces import AddressSpaces
from org.accellera.spirit.v1_0.bus_interfaces import BusInterfaces
from org.accellera.spirit.v1_0.channels import Channels
from org.accellera.spirit.v1_0.choices import Choices
from org.accellera.spirit.v1_0.component_generators import ComponentGenerators
from org.accellera.spirit.v1_0.component_instances import ComponentInstances
from org.accellera.spirit.v1_0.configurators import Configurators
from org.accellera.spirit.v1_0.file_sets import FileSets
from org.accellera.spirit.v1_0.hw_model import HwModel
from org.accellera.spirit.v1_0.interconnections import Interconnections
from org.accellera.spirit.v1_0.memory_maps import MemoryMaps
from org.accellera.spirit.v1_0.parameter import Parameter
from org.accellera.spirit.v1_0.remap_states import RemapStates
from org.accellera.spirit.v1_0.vendor_extensions import VendorExtensions

__NAMESPACE__ = "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.0"


@dataclass(slots=True)
class ComponentType:
    """
    Component-specific extension to componentType.

    :ivar vendor: Name of the vendor who supplies this file.
    :ivar library: Name of the logical library this component belongs
        to.  Note that a physical library may contain components from
        multiple logical libraries.  Logical libraries are displayes in
        component browser.
    :ivar name: The name of the object.  Must match the root name of the
        XML file and the directory name it or its version directory
        belongs to.
    :ivar version:
    :ivar bus_interfaces:
    :ivar channels:
    :ivar component_instances:
    :ivar interconnections:
    :ivar remap_states:
    :ivar address_spaces:
    :ivar memory_maps:
    :ivar hw_model:
    :ivar component_generators: Generator list is tools-specific.
    :ivar configurators:
    :ivar choices:
    :ivar file_sets:
    :ivar cpus: cpu's in the component
    :ivar parameter:
    :ivar vendor_extensions:
    """

    class Meta:
        name = "componentType"

    vendor: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.0",
            "required": True,
        },
    )
    library: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.0",
            "required": True,
        },
    )
    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.0",
            "required": True,
        },
    )
    version: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.0",
            "required": True,
        },
    )
    bus_interfaces: Optional[BusInterfaces] = field(
        default=None,
        metadata={
            "name": "busInterfaces",
            "type": "Element",
            "namespace": "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.0",
        },
    )
    channels: Optional[Channels] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.0",
        },
    )
    component_instances: Optional[ComponentInstances] = field(
        default=None,
        metadata={
            "name": "componentInstances",
            "type": "Element",
            "namespace": "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.0",
        },
    )
    interconnections: Optional[Interconnections] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.0",
        },
    )
    remap_states: Optional[RemapStates] = field(
        default=None,
        metadata={
            "name": "remapStates",
            "type": "Element",
            "namespace": "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.0",
        },
    )
    address_spaces: Optional[AddressSpaces] = field(
        default=None,
        metadata={
            "name": "addressSpaces",
            "type": "Element",
            "namespace": "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.0",
        },
    )
    memory_maps: Optional[MemoryMaps] = field(
        default=None,
        metadata={
            "name": "memoryMaps",
            "type": "Element",
            "namespace": "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.0",
        },
    )
    hw_model: Optional[HwModel] = field(
        default=None,
        metadata={
            "name": "hwModel",
            "type": "Element",
            "namespace": "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.0",
        },
    )
    component_generators: Optional[ComponentGenerators] = field(
        default=None,
        metadata={
            "name": "componentGenerators",
            "type": "Element",
            "namespace": "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.0",
        },
    )
    configurators: Optional[Configurators] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.0",
        },
    )
    choices: Optional[Choices] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.0",
        },
    )
    file_sets: Optional[FileSets] = field(
        default=None,
        metadata={
            "name": "fileSets",
            "type": "Element",
            "namespace": "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.0",
        },
    )
    cpus: Optional["ComponentType.Cpus"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.0",
        },
    )
    parameter: Iterable[Parameter] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.0",
        },
    )
    vendor_extensions: Optional[VendorExtensions] = field(
        default=None,
        metadata={
            "name": "vendorExtensions",
            "type": "Element",
            "namespace": "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.0",
        },
    )

    @dataclass(slots=True)
    class Cpus:
        """
        :ivar cpu: Describes a processor in this component.
        """

        cpu: Iterable["ComponentType.Cpus.Cpu"] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.0",
            },
        )

        @dataclass(slots=True)
        class Cpu:
            """
            :ivar name: The name of the cpu instance relative to the
                platform core.
            :ivar address_space_ref: Indicates which address space maps
                into this cpu.
            :ivar parameter: Data specific to the cpu.
            :ivar vendor_extensions:
            """

            name: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.0",
                    "required": True,
                },
            )
            address_space_ref: Iterable[AddressSpaceRef] = field(
                default_factory=list,
                metadata={
                    "name": "addressSpaceRef",
                    "type": "Element",
                    "namespace": "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.0",
                    "min_occurs": 1,
                },
            )
            parameter: Iterable[Parameter] = field(
                default_factory=list,
                metadata={
                    "type": "Element",
                    "namespace": "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.0",
                },
            )
            vendor_extensions: Optional[VendorExtensions] = field(
                default=None,
                metadata={
                    "name": "vendorExtensions",
                    "type": "Element",
                    "namespace": "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.0",
                },
            )
