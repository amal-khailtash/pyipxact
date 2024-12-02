from collections.abc import Iterable
from dataclasses import dataclass, field
from typing import Optional

from org.accellera.ipxact.v1685_2014.configurable_library_ref_type import (
    ConfigurableLibraryRefType,
)
from org.accellera.ipxact.v1685_2014.is_present import IsPresent
from org.accellera.ipxact.v1685_2014.part_select import PartSelect
from org.accellera.ipxact.v1685_2014.range import Range
from org.accellera.ipxact.v1685_2014.unsigned_positive_int_expression import (
    UnsignedPositiveIntExpression,
)
from org.accellera.ipxact.v1685_2014.view_ref import ViewRef

__NAMESPACE__ = "http://www.accellera.org/XMLSchema/IPXACT/1685-2014"


@dataclass(slots=True)
class AbstractionTypes:
    """
    :ivar abstraction_type: The abstraction type/level of this
        interface. Refers to abstraction definition using vendor,
        library, name, version attributes along with any configurable
        element values needed to configure this abstraction. Bus
        definition can be found through a reference in this file.
    """

    class Meta:
        name = "abstractionTypes"
        namespace = "http://www.accellera.org/XMLSchema/IPXACT/1685-2014"

    abstraction_type: Iterable["AbstractionTypes.AbstractionType"] = field(
        default_factory=list,
        metadata={
            "name": "abstractionType",
            "type": "Element",
            "min_occurs": 1,
        },
    )

    @dataclass(slots=True)
    class AbstractionType:
        """
        :ivar view_ref: A reference to a view name in the file for which
            this type applies.
        :ivar abstraction_ref: Provides the VLNV of the abstraction
            type.
        :ivar port_maps: Listing of maps between component ports and bus
            ports.
        :ivar id:
        """

        view_ref: Iterable[ViewRef] = field(
            default_factory=list,
            metadata={
                "name": "viewRef",
                "type": "Element",
            },
        )
        abstraction_ref: Optional[ConfigurableLibraryRefType] = field(
            default=None,
            metadata={
                "name": "abstractionRef",
                "type": "Element",
                "required": True,
            },
        )
        port_maps: Optional["AbstractionTypes.AbstractionType.PortMaps"] = (
            field(
                default=None,
                metadata={
                    "name": "portMaps",
                    "type": "Element",
                },
            )
        )
        id: Optional[str] = field(
            default=None,
            metadata={
                "type": "Attribute",
                "namespace": "http://www.w3.org/XML/1998/namespace",
            },
        )

        @dataclass(slots=True)
        class PortMaps:
            """
            :ivar port_map: Maps a component's port to a port in a bus
                description. This is the logical to physical mapping.
                The logical pin comes from the bus interface and the
                physical pin from the component.
            """

            port_map: Iterable[
                "AbstractionTypes.AbstractionType.PortMaps.PortMap"
            ] = field(
                default_factory=list,
                metadata={
                    "name": "portMap",
                    "type": "Element",
                    "min_occurs": 1,
                },
            )

            @dataclass(slots=True)
            class PortMap:
                """
                :ivar is_present:
                :ivar logical_port: Logical port from abstraction
                    definition
                :ivar physical_port: Physical port from this component
                :ivar logical_tie_off: Identifies a value to tie this
                    logical port to.
                :ivar is_informative: When true, indicates that this
                    portMap element is for information purpose only.
                :ivar id:
                :ivar invert: Indicates that the connection between the
                    logical and physical ports should include an
                    inversion.
                """

                is_present: Optional[IsPresent] = field(
                    default=None,
                    metadata={
                        "name": "isPresent",
                        "type": "Element",
                    },
                )
                logical_port: Optional[
                    "AbstractionTypes.AbstractionType.PortMaps.PortMap.LogicalPort"
                ] = field(
                    default=None,
                    metadata={
                        "name": "logicalPort",
                        "type": "Element",
                        "required": True,
                    },
                )
                physical_port: Optional[
                    "AbstractionTypes.AbstractionType.PortMaps.PortMap.PhysicalPort"
                ] = field(
                    default=None,
                    metadata={
                        "name": "physicalPort",
                        "type": "Element",
                    },
                )
                logical_tie_off: Optional[UnsignedPositiveIntExpression] = (
                    field(
                        default=None,
                        metadata={
                            "name": "logicalTieOff",
                            "type": "Element",
                        },
                    )
                )
                is_informative: Optional[bool] = field(
                    default=None,
                    metadata={
                        "name": "isInformative",
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
                invert: object = field(
                    default="false",
                    metadata={
                        "type": "Attribute",
                    },
                )

                @dataclass(slots=True)
                class LogicalPort:
                    """
                    :ivar name: Bus port name as specified inside the
                        abstraction definition
                    :ivar range:
                    """

                    name: Optional[str] = field(
                        default=None,
                        metadata={
                            "type": "Element",
                            "required": True,
                        },
                    )
                    range: Optional[Range] = field(
                        default=None,
                        metadata={
                            "type": "Element",
                        },
                    )

                @dataclass(slots=True)
                class PhysicalPort:
                    """
                    :ivar name: Component port name as specified inside
                        the model port section
                    :ivar part_select:
                    """

                    name: Optional[str] = field(
                        default=None,
                        metadata={
                            "type": "Element",
                            "required": True,
                            "white_space": "collapse",
                            "pattern": r"\i[\p{L}\p{N}\.\-:_]*",
                        },
                    )
                    part_select: Optional[PartSelect] = field(
                        default=None,
                        metadata={
                            "name": "partSelect",
                            "type": "Element",
                        },
                    )
