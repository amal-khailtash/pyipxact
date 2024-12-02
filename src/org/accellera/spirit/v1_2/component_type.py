from collections.abc import Iterable
from dataclasses import dataclass, field
from typing import Optional

from org.accellera.spirit.v1_2.address_space_ref import AddressSpaceRef
from org.accellera.spirit.v1_2.address_spaces import AddressSpaces
from org.accellera.spirit.v1_2.bus_interfaces import BusInterfaces
from org.accellera.spirit.v1_2.channels import Channels
from org.accellera.spirit.v1_2.choices import Choices
from org.accellera.spirit.v1_2.component_constraint_sets import (
    ComponentConstraintSets,
)
from org.accellera.spirit.v1_2.component_generators import ComponentGenerators
from org.accellera.spirit.v1_2.configurators import Configurators
from org.accellera.spirit.v1_2.file_sets import FileSets
from org.accellera.spirit.v1_2.memory_maps import MemoryMaps
from org.accellera.spirit.v1_2.model import Model
from org.accellera.spirit.v1_2.other_clocks import OtherClocks
from org.accellera.spirit.v1_2.parameter import Parameter
from org.accellera.spirit.v1_2.remap_states import RemapStates
from org.accellera.spirit.v1_2.vendor_extensions import VendorExtensions
from org.accellera.spirit.v1_2.whitebox_element_type import WhiteboxElementType

__NAMESPACE__ = "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.2"


@dataclass(slots=True)
class ComponentType:
    """
    Component-specific extension to componentType.

    :ivar vendor: Name of the vendor who supplies this file.
    :ivar library: Name of the logical library this element belongs to.
    :ivar name: The name of the object.
    :ivar version:
    :ivar bus_interfaces:
    :ivar channels:
    :ivar remap_states:
    :ivar address_spaces:
    :ivar memory_maps:
    :ivar model:
    :ivar component_generators: Generator list is tools-specific.
    :ivar configurators:
    :ivar choices:
    :ivar file_sets:
    :ivar whitebox_elements:
    :ivar cpus: cpu's in the component
    :ivar component_constraint_sets:
    :ivar other_clock_drivers: Defines a set of clock drivers that are
        not directly associated with an input signal of the component.
    :ivar parameter:
    :ivar vendor_extensions:
    """

    class Meta:
        name = "componentType"

    vendor: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.2",
            "required": True,
        },
    )
    library: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.2",
            "required": True,
        },
    )
    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.2",
            "required": True,
        },
    )
    version: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.2",
            "required": True,
        },
    )
    bus_interfaces: Optional[BusInterfaces] = field(
        default=None,
        metadata={
            "name": "busInterfaces",
            "type": "Element",
            "namespace": "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.2",
        },
    )
    channels: Optional[Channels] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.2",
        },
    )
    remap_states: Optional[RemapStates] = field(
        default=None,
        metadata={
            "name": "remapStates",
            "type": "Element",
            "namespace": "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.2",
        },
    )
    address_spaces: Optional[AddressSpaces] = field(
        default=None,
        metadata={
            "name": "addressSpaces",
            "type": "Element",
            "namespace": "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.2",
        },
    )
    memory_maps: Optional[MemoryMaps] = field(
        default=None,
        metadata={
            "name": "memoryMaps",
            "type": "Element",
            "namespace": "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.2",
        },
    )
    model: Optional[Model] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.2",
        },
    )
    component_generators: Optional[ComponentGenerators] = field(
        default=None,
        metadata={
            "name": "componentGenerators",
            "type": "Element",
            "namespace": "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.2",
        },
    )
    configurators: Optional[Configurators] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.2",
        },
    )
    choices: Optional[Choices] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.2",
        },
    )
    file_sets: Optional[FileSets] = field(
        default=None,
        metadata={
            "name": "fileSets",
            "type": "Element",
            "namespace": "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.2",
        },
    )
    whitebox_elements: Optional["ComponentType.WhiteboxElements"] = field(
        default=None,
        metadata={
            "name": "whiteboxElements",
            "type": "Element",
            "namespace": "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.2",
        },
    )
    cpus: Optional["ComponentType.Cpus"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.2",
        },
    )
    component_constraint_sets: Optional[ComponentConstraintSets] = field(
        default=None,
        metadata={
            "name": "componentConstraintSets",
            "type": "Element",
            "namespace": "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.2",
        },
    )
    other_clock_drivers: Optional[OtherClocks] = field(
        default=None,
        metadata={
            "name": "otherClockDrivers",
            "type": "Element",
            "namespace": "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.2",
        },
    )
    parameter: Iterable[Parameter] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.2",
        },
    )
    vendor_extensions: Optional[VendorExtensions] = field(
        default=None,
        metadata={
            "name": "vendorExtensions",
            "type": "Element",
            "namespace": "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.2",
        },
    )

    @dataclass(slots=True)
    class WhiteboxElements:
        whitebox_element: Iterable[WhiteboxElementType] = field(
            default_factory=list,
            metadata={
                "name": "whiteboxElement",
                "type": "Element",
                "namespace": "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.2",
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
                "namespace": "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.2",
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
                    "namespace": "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.2",
                    "required": True,
                },
            )
            address_space_ref: Iterable[AddressSpaceRef] = field(
                default_factory=list,
                metadata={
                    "name": "addressSpaceRef",
                    "type": "Element",
                    "namespace": "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.2",
                    "min_occurs": 1,
                },
            )
            parameter: Iterable[Parameter] = field(
                default_factory=list,
                metadata={
                    "type": "Element",
                    "namespace": "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.2",
                },
            )
            vendor_extensions: Optional[VendorExtensions] = field(
                default=None,
                metadata={
                    "name": "vendorExtensions",
                    "type": "Element",
                    "namespace": "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.2",
                },
            )
