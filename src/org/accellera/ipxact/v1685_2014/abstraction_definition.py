from collections.abc import Iterable
from dataclasses import dataclass, field
from typing import Optional

from org.accellera.ipxact.v1685_2014.abstraction_def_port_constraints_type import (
    AbstractionDefPortConstraintsType,
)
from org.accellera.ipxact.v1685_2014.assertions import Assertions
from org.accellera.ipxact.v1685_2014.description import Description
from org.accellera.ipxact.v1685_2014.direction import Direction
from org.accellera.ipxact.v1685_2014.display_name import DisplayName
from org.accellera.ipxact.v1685_2014.is_present import IsPresent
from org.accellera.ipxact.v1685_2014.kind import Kind
from org.accellera.ipxact.v1685_2014.library_ref_type import LibraryRefType
from org.accellera.ipxact.v1685_2014.on_master_initiative import (
    OnMasterInitiative,
)
from org.accellera.ipxact.v1685_2014.on_slave_initiative import (
    OnSlaveInitiative,
)
from org.accellera.ipxact.v1685_2014.on_system_initiative import (
    OnSystemInitiative,
)
from org.accellera.ipxact.v1685_2014.parameters import Parameters
from org.accellera.ipxact.v1685_2014.presence import Presence
from org.accellera.ipxact.v1685_2014.protocol import Protocol
from org.accellera.ipxact.v1685_2014.requires_driver import RequiresDriver
from org.accellera.ipxact.v1685_2014.unsigned_bit_vector_expression import (
    UnsignedBitVectorExpression,
)
from org.accellera.ipxact.v1685_2014.unsigned_positive_int_expression import (
    UnsignedPositiveIntExpression,
)
from org.accellera.ipxact.v1685_2014.vendor_extensions import VendorExtensions

__NAMESPACE__ = "http://www.accellera.org/XMLSchema/IPXACT/1685-2014"


@dataclass(slots=True)
class AbstractionDefinition:
    """
    Define the ports and other information of a particular abstraction of the bus.

    :ivar vendor: Name of the vendor who supplies this file.
    :ivar library: Name of the logical library this element belongs to.
    :ivar name: The name of the object.
    :ivar version: Indicates the version of the named element.
    :ivar bus_type: Reference to the busDefinition that this
        abstractionDefinition implements.
    :ivar extends: Optional name of abstraction type that this
        abstraction definition is compatible with. This abstraction
        definition may change the definitions of ports in the existing
        abstraction definition and add new ports, the ports in the
        original abstraction are not deleted but may be marked illegal
        to disallow their use. This abstraction definition may only
        extend another abstraction definition if the bus type of this
        abstraction definition extends the bus type of the extended
        abstraction definition
    :ivar ports: This is a list of logical ports defined by the bus.
    :ivar description:
    :ivar parameters:
    :ivar assertions:
    :ivar vendor_extensions:
    :ivar id:
    """

    class Meta:
        name = "abstractionDefinition"
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
    bus_type: Optional[LibraryRefType] = field(
        default=None,
        metadata={
            "name": "busType",
            "type": "Element",
            "required": True,
        },
    )
    extends: Optional[LibraryRefType] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    ports: Optional["AbstractionDefinition.Ports"] = field(
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
    parameters: Optional[Parameters] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    assertions: Optional[Assertions] = field(
        default=None,
        metadata={
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
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )

    @dataclass(slots=True)
    class Ports:
        port: Iterable["AbstractionDefinition.Ports.Port"] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "min_occurs": 1,
            },
        )

        @dataclass(slots=True)
        class Port:
            """
            :ivar is_present:
            :ivar logical_name: The assigned name of this port in bus
                specifications.
            :ivar display_name:
            :ivar description:
            :ivar wire: A port that carries logic or an array of logic
                values
            :ivar transactional: A port that carries complex information
                modeled at a high level of abstraction.
            :ivar vendor_extensions:
            :ivar id:
            """

            is_present: Optional[IsPresent] = field(
                default=None,
                metadata={
                    "name": "isPresent",
                    "type": "Element",
                },
            )
            logical_name: Optional[str] = field(
                default=None,
                metadata={
                    "name": "logicalName",
                    "type": "Element",
                    "required": True,
                },
            )
            display_name: Optional[DisplayName] = field(
                default=None,
                metadata={
                    "name": "displayName",
                    "type": "Element",
                },
            )
            description: Optional[Description] = field(
                default=None,
                metadata={
                    "type": "Element",
                },
            )
            wire: Optional["AbstractionDefinition.Ports.Port.Wire"] = field(
                default=None,
                metadata={
                    "type": "Element",
                },
            )
            transactional: Optional[
                "AbstractionDefinition.Ports.Port.Transactional"
            ] = field(
                default=None,
                metadata={
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
            id: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Attribute",
                    "namespace": "http://www.w3.org/XML/1998/namespace",
                },
            )

            @dataclass(slots=True)
            class Wire:
                """
                :ivar qualifier: The type of information this port
                    carries A wire port can carry both address and data,
                    but may not mix this with a clock or reset
                :ivar on_system: Defines constraints for this port when
                    present in a system bus interface with a matching
                    group name.
                :ivar on_master: Defines constraints for this port when
                    present in a master bus interface.
                :ivar on_slave: Defines constraints for this port when
                    present in a slave bus interface.
                :ivar default_value: Indicates the default value for
                    this wire port.
                :ivar requires_driver:
                """

                qualifier: Optional[
                    "AbstractionDefinition.Ports.Port.Wire.Qualifier"
                ] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                    },
                )
                on_system: Iterable[
                    "AbstractionDefinition.Ports.Port.Wire.OnSystem"
                ] = field(
                    default_factory=list,
                    metadata={
                        "name": "onSystem",
                        "type": "Element",
                    },
                )
                on_master: Optional[
                    "AbstractionDefinition.Ports.Port.Wire.OnMaster"
                ] = field(
                    default=None,
                    metadata={
                        "name": "onMaster",
                        "type": "Element",
                    },
                )
                on_slave: Optional[
                    "AbstractionDefinition.Ports.Port.Wire.OnSlave"
                ] = field(
                    default=None,
                    metadata={
                        "name": "onSlave",
                        "type": "Element",
                    },
                )
                default_value: Optional[UnsignedBitVectorExpression] = field(
                    default=None,
                    metadata={
                        "name": "defaultValue",
                        "type": "Element",
                    },
                )
                requires_driver: Optional[RequiresDriver] = field(
                    default=None,
                    metadata={
                        "name": "requiresDriver",
                        "type": "Element",
                    },
                )

                @dataclass(slots=True)
                class Qualifier:
                    """
                    :ivar is_address: If this element is present, the
                        port contains address information.
                    :ivar is_data: If this element is present, the port
                        contains data information.
                    :ivar is_clock: If this element is present, the port
                        contains only clock information.
                    :ivar is_reset: Is this element is present, the port
                        contains only reset information.
                    """

                    is_address: Optional[bool] = field(
                        default=None,
                        metadata={
                            "name": "isAddress",
                            "type": "Element",
                        },
                    )
                    is_data: Optional[bool] = field(
                        default=None,
                        metadata={
                            "name": "isData",
                            "type": "Element",
                        },
                    )
                    is_clock: Optional[bool] = field(
                        default=None,
                        metadata={
                            "name": "isClock",
                            "type": "Element",
                        },
                    )
                    is_reset: Optional[bool] = field(
                        default=None,
                        metadata={
                            "name": "isReset",
                            "type": "Element",
                        },
                    )

                @dataclass(slots=True)
                class OnSystem:
                    """
                    :ivar group: Used to group system ports into
                        different groups within a common bus.
                    :ivar presence:
                    :ivar width: Number of bits required to represent
                        this port. Absence of this element indicates
                        unconstrained number of bits, i.e. the component
                        will define the number of bits in this port. The
                        logical numbering of the port starts at 0 to
                        width-1.
                    :ivar direction: If this element is present, the
                        direction of this port is restricted to the
                        specified value. The direction is relative to
                        the non-mirrored interface.
                    :ivar mode_constraints: Specifies default
                        constraints for the enclosing wire type port. If
                        the mirroredModeConstraints element is not
                        defined, then these constraints applied to this
                        port when it appears in a 'mode' bus interface
                        or a mirrored-'mode' bus interface. Otherwise
                        they only apply when the port appears in a
                        'mode' bus interface.
                    :ivar mirrored_mode_constraints: Specifies default
                        constraints for the enclosing wire type port
                        when it appears in a mirrored-'mode' bus
                        interface.
                    :ivar id:
                    """

                    group: Optional[str] = field(
                        default=None,
                        metadata={
                            "type": "Element",
                            "required": True,
                        },
                    )
                    presence: Optional[Presence] = field(
                        default=None,
                        metadata={
                            "type": "Element",
                        },
                    )
                    width: Optional[UnsignedPositiveIntExpression] = field(
                        default=None,
                        metadata={
                            "type": "Element",
                        },
                    )
                    direction: Optional[Direction] = field(
                        default=None,
                        metadata={
                            "type": "Element",
                        },
                    )
                    mode_constraints: Optional[
                        AbstractionDefPortConstraintsType
                    ] = field(
                        default=None,
                        metadata={
                            "name": "modeConstraints",
                            "type": "Element",
                        },
                    )
                    mirrored_mode_constraints: Optional[
                        AbstractionDefPortConstraintsType
                    ] = field(
                        default=None,
                        metadata={
                            "name": "mirroredModeConstraints",
                            "type": "Element",
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
                class OnMaster:
                    """
                    :ivar presence:
                    :ivar width: Number of bits required to represent
                        this port. Absence of this element indicates
                        unconstrained number of bits, i.e. the component
                        will define the number of bits in this port. The
                        logical numbering of the port starts at 0 to
                        width-1.
                    :ivar direction: If this element is present, the
                        direction of this port is restricted to the
                        specified value. The direction is relative to
                        the non-mirrored interface.
                    :ivar mode_constraints: Specifies default
                        constraints for the enclosing wire type port. If
                        the mirroredModeConstraints element is not
                        defined, then these constraints applied to this
                        port when it appears in a 'mode' bus interface
                        or a mirrored-'mode' bus interface. Otherwise
                        they only apply when the port appears in a
                        'mode' bus interface.
                    :ivar mirrored_mode_constraints: Specifies default
                        constraints for the enclosing wire type port
                        when it appears in a mirrored-'mode' bus
                        interface.
                    """

                    presence: Optional[Presence] = field(
                        default=None,
                        metadata={
                            "type": "Element",
                        },
                    )
                    width: Optional[UnsignedPositiveIntExpression] = field(
                        default=None,
                        metadata={
                            "type": "Element",
                        },
                    )
                    direction: Optional[Direction] = field(
                        default=None,
                        metadata={
                            "type": "Element",
                        },
                    )
                    mode_constraints: Optional[
                        AbstractionDefPortConstraintsType
                    ] = field(
                        default=None,
                        metadata={
                            "name": "modeConstraints",
                            "type": "Element",
                        },
                    )
                    mirrored_mode_constraints: Optional[
                        AbstractionDefPortConstraintsType
                    ] = field(
                        default=None,
                        metadata={
                            "name": "mirroredModeConstraints",
                            "type": "Element",
                        },
                    )

                @dataclass(slots=True)
                class OnSlave:
                    """
                    :ivar presence:
                    :ivar width: Number of bits required to represent
                        this port. Absence of this element indicates
                        unconstrained number of bits, i.e. the component
                        will define the number of bits in this port. The
                        logical numbering of the port starts at 0 to
                        width-1.
                    :ivar direction: If this element is present, the
                        direction of this port is restricted to the
                        specified value. The direction is relative to
                        the non-mirrored interface.
                    :ivar mode_constraints: Specifies default
                        constraints for the enclosing wire type port. If
                        the mirroredModeConstraints element is not
                        defined, then these constraints applied to this
                        port when it appears in a 'mode' bus interface
                        or a mirrored-'mode' bus interface. Otherwise
                        they only apply when the port appears in a
                        'mode' bus interface.
                    :ivar mirrored_mode_constraints: Specifies default
                        constraints for the enclosing wire type port
                        when it appears in a mirrored-'mode' bus
                        interface.
                    """

                    presence: Optional[Presence] = field(
                        default=None,
                        metadata={
                            "type": "Element",
                        },
                    )
                    width: Optional[UnsignedPositiveIntExpression] = field(
                        default=None,
                        metadata={
                            "type": "Element",
                        },
                    )
                    direction: Optional[Direction] = field(
                        default=None,
                        metadata={
                            "type": "Element",
                        },
                    )
                    mode_constraints: Optional[
                        AbstractionDefPortConstraintsType
                    ] = field(
                        default=None,
                        metadata={
                            "name": "modeConstraints",
                            "type": "Element",
                        },
                    )
                    mirrored_mode_constraints: Optional[
                        AbstractionDefPortConstraintsType
                    ] = field(
                        default=None,
                        metadata={
                            "name": "mirroredModeConstraints",
                            "type": "Element",
                        },
                    )

            @dataclass(slots=True)
            class Transactional:
                """
                :ivar qualifier: The type of information this port
                    carries A transactional port can carry both address
                    and data information.
                :ivar on_system: Defines constraints for this port when
                    present in a system bus interface with a matching
                    group name.
                :ivar on_master: Defines constraints for this port when
                    present in a master bus interface.
                :ivar on_slave: Defines constraints for this port when
                    present in a slave bus interface.
                """

                qualifier: Optional[
                    "AbstractionDefinition.Ports.Port.Transactional.Qualifier"
                ] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                    },
                )
                on_system: Iterable[
                    "AbstractionDefinition.Ports.Port.Transactional.OnSystem"
                ] = field(
                    default_factory=list,
                    metadata={
                        "name": "onSystem",
                        "type": "Element",
                    },
                )
                on_master: Optional[
                    "AbstractionDefinition.Ports.Port.Transactional.OnMaster"
                ] = field(
                    default=None,
                    metadata={
                        "name": "onMaster",
                        "type": "Element",
                    },
                )
                on_slave: Optional[
                    "AbstractionDefinition.Ports.Port.Transactional.OnSlave"
                ] = field(
                    default=None,
                    metadata={
                        "name": "onSlave",
                        "type": "Element",
                    },
                )

                @dataclass(slots=True)
                class Qualifier:
                    """
                    :ivar is_address: If this element is present, the
                        port contains address information.
                    :ivar is_data: If this element is present, the port
                        contains data information.
                    """

                    is_address: Optional[bool] = field(
                        default=None,
                        metadata={
                            "name": "isAddress",
                            "type": "Element",
                        },
                    )
                    is_data: Optional[bool] = field(
                        default=None,
                        metadata={
                            "name": "isData",
                            "type": "Element",
                        },
                    )

                @dataclass(slots=True)
                class OnSystem:
                    """
                    :ivar group: Used to group system ports into
                        different groups within a common bus.
                    :ivar presence:
                    :ivar initiative: If this element is present, the
                        type of access is restricted to the specified
                        value.
                    :ivar kind:
                    :ivar bus_width: If this element is present, the
                        width must match
                    :ivar protocol: If this element is present, the name
                        must match
                    :ivar id:
                    """

                    group: Optional[str] = field(
                        default=None,
                        metadata={
                            "type": "Element",
                            "required": True,
                        },
                    )
                    presence: Optional[Presence] = field(
                        default=None,
                        metadata={
                            "type": "Element",
                        },
                    )
                    initiative: Optional[OnSystemInitiative] = field(
                        default=None,
                        metadata={
                            "type": "Element",
                        },
                    )
                    kind: Optional[Kind] = field(
                        default=None,
                        metadata={
                            "type": "Element",
                        },
                    )
                    bus_width: Optional[UnsignedPositiveIntExpression] = field(
                        default=None,
                        metadata={
                            "name": "busWidth",
                            "type": "Element",
                        },
                    )
                    protocol: Optional[Protocol] = field(
                        default=None,
                        metadata={
                            "type": "Element",
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
                class OnMaster:
                    """
                    :ivar presence:
                    :ivar initiative: If this element is present, the
                        type of access is restricted to the specified
                        value.
                    :ivar kind:
                    :ivar bus_width: If this element is present, the
                        width must match
                    :ivar protocol: If this element is present, the name
                        must match
                    """

                    presence: Optional[Presence] = field(
                        default=None,
                        metadata={
                            "type": "Element",
                        },
                    )
                    initiative: Optional[OnMasterInitiative] = field(
                        default=None,
                        metadata={
                            "type": "Element",
                        },
                    )
                    kind: Optional[Kind] = field(
                        default=None,
                        metadata={
                            "type": "Element",
                        },
                    )
                    bus_width: Optional[UnsignedPositiveIntExpression] = field(
                        default=None,
                        metadata={
                            "name": "busWidth",
                            "type": "Element",
                        },
                    )
                    protocol: Optional[Protocol] = field(
                        default=None,
                        metadata={
                            "type": "Element",
                        },
                    )

                @dataclass(slots=True)
                class OnSlave:
                    """
                    :ivar presence:
                    :ivar initiative: If this element is present, the
                        type of access is restricted to the specified
                        value.
                    :ivar kind:
                    :ivar bus_width: If this element is present, the
                        width must match
                    :ivar protocol: If this element is present, the name
                        must match
                    """

                    presence: Optional[Presence] = field(
                        default=None,
                        metadata={
                            "type": "Element",
                        },
                    )
                    initiative: Optional[OnSlaveInitiative] = field(
                        default=None,
                        metadata={
                            "type": "Element",
                        },
                    )
                    kind: Optional[Kind] = field(
                        default=None,
                        metadata={
                            "type": "Element",
                        },
                    )
                    bus_width: Optional[UnsignedPositiveIntExpression] = field(
                        default=None,
                        metadata={
                            "name": "busWidth",
                            "type": "Element",
                        },
                    )
                    protocol: Optional[Protocol] = field(
                        default=None,
                        metadata={
                            "type": "Element",
                        },
                    )
