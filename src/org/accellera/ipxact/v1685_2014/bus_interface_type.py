from collections.abc import Iterable, Mapping
from dataclasses import dataclass, field
from typing import Optional

from org.accellera.ipxact.v1685_2014.abstraction_types import AbstractionTypes
from org.accellera.ipxact.v1685_2014.addr_space_ref_type import (
    AddrSpaceRefType,
)
from org.accellera.ipxact.v1685_2014.bits_in_lau import BitsInLau
from org.accellera.ipxact.v1685_2014.complex_bit_steering_expression import (
    ComplexBitSteeringExpression,
)
from org.accellera.ipxact.v1685_2014.configurable_library_ref_type import (
    ConfigurableLibraryRefType,
)
from org.accellera.ipxact.v1685_2014.description import Description
from org.accellera.ipxact.v1685_2014.display_name import DisplayName
from org.accellera.ipxact.v1685_2014.endianess_type import EndianessType
from org.accellera.ipxact.v1685_2014.file_set_ref import FileSetRef
from org.accellera.ipxact.v1685_2014.group import Group
from org.accellera.ipxact.v1685_2014.is_present import IsPresent
from org.accellera.ipxact.v1685_2014.memory_map_ref import MemoryMapRef
from org.accellera.ipxact.v1685_2014.monitor_interface_mode import (
    MonitorInterfaceMode,
)
from org.accellera.ipxact.v1685_2014.parameters import Parameters
from org.accellera.ipxact.v1685_2014.signed_longint_expression import (
    SignedLongintExpression,
)
from org.accellera.ipxact.v1685_2014.transparent_bridge import (
    TransparentBridge,
)
from org.accellera.ipxact.v1685_2014.unsigned_longint_expression import (
    UnsignedLongintExpression,
)
from org.accellera.ipxact.v1685_2014.unsigned_positive_longint_expression import (
    UnsignedPositiveLongintExpression,
)
from org.accellera.ipxact.v1685_2014.vendor_extensions import VendorExtensions

__NAMESPACE__ = "http://www.accellera.org/XMLSchema/IPXACT/1685-2014"


@dataclass(slots=True)
class BusInterfaceType:
    """
    Type definition for a busInterface in a component.

    :ivar name: Unique name
    :ivar display_name:
    :ivar description:
    :ivar is_present:
    :ivar bus_type: The bus type of this interface. Refers to bus
        definition using vendor, library, name, version attributes along
        with any configurable element values needed to configure this
        interface.
    :ivar abstraction_types:
    :ivar master: If this element is present, the bus interface can
        serve as a master.  This element encapsulates additional
        information related to its role as master.
    :ivar slave: If this element is present, the bus interface can serve
        as a slave.
    :ivar system: If this element is present, the bus interface is a
        system interface, neither master nor slave, with a specific
        function on the bus.
    :ivar mirrored_slave: If this element is present, the bus interface
        represents a mirrored slave interface. All directional
        constraints on ports are reversed relative to the specification
        in the bus definition.
    :ivar mirrored_master: If this element is present, the bus interface
        represents a mirrored master interface. All directional
        constraints on ports are reversed relative to the specification
        in the bus definition.
    :ivar mirrored_system: If this element is present, the bus interface
        represents a mirrored system interface. All directional
        constraints on ports are reversed relative to the specification
        in the bus definition.
    :ivar monitor: Indicates that this is a (passive) monitor interface.
        All of the ports in the interface must be inputs. The type of
        interface to be monitored is specified with the required
        interfaceType attribute. The ipxact:group element must be
        specified if monitoring a system interface.
    :ivar connection_required: Indicates whether a connection to this
        interface is required for proper component functionality.
    :ivar bits_in_lau:
    :ivar bit_steering: Indicates whether bit steering should be used to
        map this interface onto a bus of different data width. Values
        are "on", "off" (defaults to "off").
    :ivar endianness: 'big': means the most significant element of any
        multi-element  data field is stored at the lowest memory
        address. 'little' means the least significant element of any
        multi-element data field is stored at the lowest memory address.
        If this element is not present the default is 'little' endian.
    :ivar parameters:
    :ivar vendor_extensions:
    :ivar other_attributes:
    """

    class Meta:
        name = "busInterfaceType"

    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2014",
            "required": True,
        },
    )
    display_name: Optional[DisplayName] = field(
        default=None,
        metadata={
            "name": "displayName",
            "type": "Element",
            "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2014",
        },
    )
    description: Optional[Description] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2014",
        },
    )
    is_present: Optional[IsPresent] = field(
        default=None,
        metadata={
            "name": "isPresent",
            "type": "Element",
            "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2014",
        },
    )
    bus_type: Optional[ConfigurableLibraryRefType] = field(
        default=None,
        metadata={
            "name": "busType",
            "type": "Element",
            "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2014",
            "required": True,
        },
    )
    abstraction_types: Optional[AbstractionTypes] = field(
        default=None,
        metadata={
            "name": "abstractionTypes",
            "type": "Element",
            "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2014",
        },
    )
    master: Optional["BusInterfaceType.Master"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2014",
        },
    )
    slave: Optional["BusInterfaceType.Slave"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2014",
        },
    )
    system: Optional["BusInterfaceType.System"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2014",
        },
    )
    mirrored_slave: Optional["BusInterfaceType.MirroredSlave"] = field(
        default=None,
        metadata={
            "name": "mirroredSlave",
            "type": "Element",
            "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2014",
        },
    )
    mirrored_master: Optional[object] = field(
        default=None,
        metadata={
            "name": "mirroredMaster",
            "type": "Element",
            "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2014",
        },
    )
    mirrored_system: Optional["BusInterfaceType.MirroredSystem"] = field(
        default=None,
        metadata={
            "name": "mirroredSystem",
            "type": "Element",
            "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2014",
        },
    )
    monitor: Optional["BusInterfaceType.Monitor"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2014",
        },
    )
    connection_required: Optional[bool] = field(
        default=None,
        metadata={
            "name": "connectionRequired",
            "type": "Element",
            "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2014",
        },
    )
    bits_in_lau: Optional[BitsInLau] = field(
        default=None,
        metadata={
            "name": "bitsInLau",
            "type": "Element",
            "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2014",
        },
    )
    bit_steering: Optional[ComplexBitSteeringExpression] = field(
        default=None,
        metadata={
            "name": "bitSteering",
            "type": "Element",
            "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2014",
        },
    )
    endianness: Optional[EndianessType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2014",
        },
    )
    parameters: Optional[Parameters] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2014",
        },
    )
    vendor_extensions: Optional[VendorExtensions] = field(
        default=None,
        metadata={
            "name": "vendorExtensions",
            "type": "Element",
            "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2014",
        },
    )
    other_attributes: Mapping[str, str] = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "##other",
        },
    )

    @dataclass(slots=True)
    class Master:
        """
        :ivar address_space_ref: If this master connects to an
            addressable bus, this element references the address space
            it maps to.
        """

        address_space_ref: Optional[
            "BusInterfaceType.Master.AddressSpaceRef"
        ] = field(
            default=None,
            metadata={
                "name": "addressSpaceRef",
                "type": "Element",
                "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2014",
            },
        )

        @dataclass(slots=True)
        class AddressSpaceRef(AddrSpaceRefType):
            """
            :ivar base_address: Base of an address space.
            """

            base_address: Optional[SignedLongintExpression] = field(
                default=None,
                metadata={
                    "name": "baseAddress",
                    "type": "Element",
                    "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2014",
                },
            )

    @dataclass(slots=True)
    class Slave:
        """
        :ivar memory_map_ref:
        :ivar transparent_bridge:
        :ivar file_set_ref_group: This reference is used to point the
            filesets that are associated with this slave port. Depending
            on the slave port function, there may be completely
            different software drivers associated with the different
            ports.
        """

        memory_map_ref: Optional[MemoryMapRef] = field(
            default=None,
            metadata={
                "name": "memoryMapRef",
                "type": "Element",
                "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2014",
            },
        )
        transparent_bridge: Iterable[TransparentBridge] = field(
            default_factory=list,
            metadata={
                "name": "transparentBridge",
                "type": "Element",
                "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2014",
            },
        )
        file_set_ref_group: Iterable[
            "BusInterfaceType.Slave.FileSetRefGroup"
        ] = field(
            default_factory=list,
            metadata={
                "name": "fileSetRefGroup",
                "type": "Element",
                "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2014",
            },
        )

        @dataclass(slots=True)
        class FileSetRefGroup:
            """
            :ivar group: Abritray name assigned to the collections of
                fileSets.
            :ivar file_set_ref:
            :ivar id:
            """

            group: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2014",
                },
            )
            file_set_ref: Iterable[FileSetRef] = field(
                default_factory=list,
                metadata={
                    "name": "fileSetRef",
                    "type": "Element",
                    "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2014",
                },
            )
            id: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Attribute",
                    "namespace": "http://www.w3.org/XML/1998/namespace",
                },
            )

    @dataclass(slots=True)
    class System:
        group: Optional[Group] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2014",
                "required": True,
            },
        )

    @dataclass(slots=True)
    class MirroredSlave:
        """
        :ivar base_addresses: Represents a set of remap base addresses.
        """

        base_addresses: Optional[
            "BusInterfaceType.MirroredSlave.BaseAddresses"
        ] = field(
            default=None,
            metadata={
                "name": "baseAddresses",
                "type": "Element",
                "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2014",
            },
        )

        @dataclass(slots=True)
        class BaseAddresses:
            """
            :ivar remap_address: Base of an address block, expressed as
                the number of bitsInLAU from the containing
                busInterface. The state attribute indicates the name of
                the remap state for which this address is valid.
            :ivar range: The address range of mirrored slave, expressed
                as the number of bitsInLAU from the containing
                busInterface.
            """

            remap_address: Iterable[
                "BusInterfaceType.MirroredSlave.BaseAddresses.RemapAddress"
            ] = field(
                default_factory=list,
                metadata={
                    "name": "remapAddress",
                    "type": "Element",
                    "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2014",
                    "min_occurs": 1,
                },
            )
            range: Optional[UnsignedPositiveLongintExpression] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2014",
                    "required": True,
                },
            )

            @dataclass(slots=True)
            class RemapAddress(UnsignedLongintExpression):
                """
                :ivar state: Name of the state in which this remapped
                    address range is valid
                :ivar id:
                """

                state: Optional[str] = field(
                    default=None,
                    metadata={
                        "type": "Attribute",
                    },
                )
                id: Optional[str] = field(
                    default=None,
                    metadata={
                        "type": "Attribute",
                        "namespace": "http://www.w3.org/XML/1998/namespace",
                    },
                )

    @dataclass(slots=True)
    class MirroredSystem:
        group: Optional[Group] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2014",
                "required": True,
            },
        )

    @dataclass(slots=True)
    class Monitor:
        """
        :ivar group: Indicates which system interface is being
            monitored. Name must match a group name present on one or
            more ports in the corresonding bus definition.
        :ivar interface_mode:
        """

        group: Optional[Group] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2014",
            },
        )
        interface_mode: Optional[MonitorInterfaceMode] = field(
            default=None,
            metadata={
                "name": "interfaceMode",
                "type": "Attribute",
                "required": True,
            },
        )
