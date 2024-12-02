from collections.abc import Iterable, Mapping
from dataclasses import dataclass, field
from typing import Optional

from org.accellera.spirit.v1_2.bus_def_signal_constraint_sets import (
    BusDefSignalConstraintSets,
)
from org.accellera.spirit.v1_2.choice_style_value import ChoiceStyleValue
from org.accellera.spirit.v1_2.choices import Choices
from org.accellera.spirit.v1_2.direction_value import DirectionValue
from org.accellera.spirit.v1_2.format_type import FormatType
from org.accellera.spirit.v1_2.library_ref_type import LibraryRefType
from org.accellera.spirit.v1_2.on_master_value import OnMasterValue
from org.accellera.spirit.v1_2.on_slave_value import OnSlaveValue
from org.accellera.spirit.v1_2.on_system_value import OnSystemValue
from org.accellera.spirit.v1_2.range_type_type import RangeTypeType
from org.accellera.spirit.v1_2.requires_driver import RequiresDriver
from org.accellera.spirit.v1_2.vendor_extensions import VendorExtensions

__NAMESPACE__ = "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.2"


@dataclass(slots=True)
class BusDefinition:
    """
    Defines the signals and high-level function of a bus.

    :ivar vendor: Name of the vendor who supplies this file.
    :ivar library: Name of the logical library this element belongs to.
    :ivar name: The name of the object.
    :ivar version:
    :ivar direct_connection: This element indicates that a master
        interface may be directly connected to a slave interface (under
        certain conditions) for busses of this type.
    :ivar extends: Optional name of bus type that this bus definition is
        compatible with. This bus definition may change the definitions
        of signals in the existing bus definition and add new signals,
        the signals in the original bus are not deleted but may be
        marked illegal to disallow their use.
    :ivar max_masters: Indicates the maximum number of masters this bus
        supports.  If this element is not present, the number of masters
        allowed is unbounded.
    :ivar max_slaves: Indicates the maximum number of slaves this bus
        supports.  If the element is not present, the number of slaves
        allowed is unbounded.
    :ivar signals: This is a list of logical signals defined by the bus.
    :ivar choices:
    :ivar bus_def_parameters: Container element for parameters defined
        for a bus definition.
    :ivar vendor_extensions:
    """

    class Meta:
        name = "busDefinition"
        namespace = "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.2"

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
    direct_connection: bool = field(
        default=False,
        metadata={
            "name": "directConnection",
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
    max_masters: Optional[int] = field(
        default=None,
        metadata={
            "name": "maxMasters",
            "type": "Element",
        },
    )
    max_slaves: Optional[int] = field(
        default=None,
        metadata={
            "name": "maxSlaves",
            "type": "Element",
        },
    )
    signals: Optional["BusDefinition.Signals"] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    choices: Optional[Choices] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    bus_def_parameters: Optional["BusDefinition.BusDefParameters"] = field(
        default=None,
        metadata={
            "name": "busDefParameters",
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

    @dataclass(slots=True)
    class Signals:
        signal: Iterable["BusDefinition.Signals.Signal"] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "min_occurs": 1,
            },
        )

        @dataclass(slots=True)
        class Signal:
            """
            :ivar logical_name: The assigned name of this signal in bus
                specifications.
            :ivar is_address: If this element is present, the signal
                contains address information.
            :ivar is_data: If this element is present, the signal
                contains data information.
            :ivar is_clock: If this element is present, the signal
                contains only clock information.
            :ivar is_reset: Is this element is present, the signal
                contains only reset information.
            :ivar requires_driver:
            :ivar on_system: Defines constraints for this signal when
                present in a system bus interface with a matching group
                name.
            :ivar on_master: Defines constraints for this signal when
                present in a master bus interface.
            :ivar on_slave: Defines constraints for this signal when
                present in a slave bus interface.
            :ivar default_value: Default value for the signal when used
                as an input and it ends up  being unconnected. Ignored
                for signals that require a singleShot or clock type
                driver. This value may be overridden by a defaultValue
                on a component pin.
            :ivar bus_def_signal_constraint_sets:
            :ivar vendor_extensions:
            """

            logical_name: Optional[str] = field(
                default=None,
                metadata={
                    "name": "logicalName",
                    "type": "Element",
                    "required": True,
                },
            )
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
            requires_driver: Optional[RequiresDriver] = field(
                default=None,
                metadata={
                    "name": "requiresDriver",
                    "type": "Element",
                },
            )
            on_system: Iterable["BusDefinition.Signals.Signal.OnSystem"] = (
                field(
                    default_factory=list,
                    metadata={
                        "name": "onSystem",
                        "type": "Element",
                    },
                )
            )
            on_master: Optional["BusDefinition.Signals.Signal.OnMaster"] = (
                field(
                    default=None,
                    metadata={
                        "name": "onMaster",
                        "type": "Element",
                    },
                )
            )
            on_slave: Optional["BusDefinition.Signals.Signal.OnSlave"] = field(
                default=None,
                metadata={
                    "name": "onSlave",
                    "type": "Element",
                },
            )
            default_value: Optional[
                "BusDefinition.Signals.Signal.DefaultValue"
            ] = field(
                default=None,
                metadata={
                    "name": "defaultValue",
                    "type": "Element",
                },
            )
            bus_def_signal_constraint_sets: Optional[
                BusDefSignalConstraintSets
            ] = field(
                default=None,
                metadata={
                    "name": "busDefSignalConstraintSets",
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

            @dataclass(slots=True)
            class OnSystem:
                """
                :ivar group: Used to group system signals into different
                    groups within a common bus.
                :ivar bit_width: Number of bits required to represent
                    this signal. Absence of this element indicates
                    unconstrained number of bits, i.e. the component
                    will define the number of bits in this signal.
                :ivar direction: If this element is present, the
                    direction of this signal is restricted to the
                    specified value. The direction is relative to the
                    non-mirrored interface. Use the value 'illegal' to
                    indicate that this signal cannot appear in the
                    interface.
                """

                group: Optional[str] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "required": True,
                    },
                )
                bit_width: Optional[int] = field(
                    default=None,
                    metadata={
                        "name": "bitWidth",
                        "type": "Element",
                    },
                )
                direction: Optional[OnSystemValue] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                    },
                )

            @dataclass(slots=True)
            class OnMaster:
                """
                :ivar bit_width: Number of bits required to represent
                    this signal. Absence of this element indicates
                    unconstrained number of bits, i.e. the component
                    will define the number of bits in this signal.
                :ivar direction: If this element is present, the
                    direction of this signal is restricted to the
                    specified value. The direction is relative to the
                    non-mirrored interface. Use the value 'illegal' to
                    indicate that this signal cannot appear in the
                    interface.
                """

                bit_width: Optional[int] = field(
                    default=None,
                    metadata={
                        "name": "bitWidth",
                        "type": "Element",
                    },
                )
                direction: Optional[OnMasterValue] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                    },
                )

            @dataclass(slots=True)
            class OnSlave:
                """
                :ivar bit_width: Number of bits required to represent
                    this signal. Absence of this element indicates
                    unconstrained number of bits, i.e. the component
                    will define the number of bits in this signal.
                :ivar direction: If this element is present, the
                    direction of this signal is restricted to the
                    specified value. The direction is relative to the
                    non-mirrored interface. Use the value 'illegal' to
                    indicate that this signal cannot appear in the
                    interface.
                """

                bit_width: Optional[int] = field(
                    default=None,
                    metadata={
                        "name": "bitWidth",
                        "type": "Element",
                    },
                )
                direction: Optional[OnSlaveValue] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                    },
                )

            @dataclass(slots=True)
            class DefaultValue:
                """
                :ivar value: The value of a signal. 1 or 0 for single
                    bit signals, unsigned numeric otherwise.
                """

                value: Optional[str] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "required": True,
                        "pattern": r"-?((0x)|(0X)|#)?[0-9a-fA-F]*[kmgtKMGT]?",
                    },
                )

    @dataclass(slots=True)
    class BusDefParameters:
        """
        :ivar bus_def_parameter: Defines a parameter which can be
            specified on a bus interface. The parameter is fully
            described on the bus definition and then instantiated on the
            bus interface. Setting 'consistent' to true implies that the
            parameter must have the same value on the corresponding bus
            interface parameters on both sides of connected interfaces.
        """

        bus_def_parameter: Iterable[
            "BusDefinition.BusDefParameters.BusDefParameter"
        ] = field(
            default_factory=list,
            metadata={
                "name": "busDefParameter",
                "type": "Element",
                "min_occurs": 1,
            },
        )

        @dataclass(slots=True)
        class BusDefParameter:
            value: str = field(
                default="",
                metadata={
                    "required": True,
                },
            )
            consistent: bool = field(
                default=False,
                metadata={
                    "type": "Attribute",
                    "namespace": "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.2",
                },
            )
            name: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Attribute",
                    "namespace": "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.2",
                    "required": True,
                },
            )
            minimum: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Attribute",
                    "namespace": "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.2",
                },
            )
            maximum: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Attribute",
                    "namespace": "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.2",
                },
            )
            range_type: RangeTypeType = field(
                default=RangeTypeType.FLOAT,
                metadata={
                    "name": "rangeType",
                    "type": "Attribute",
                    "namespace": "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.2",
                },
            )
            order: Optional[float] = field(
                default=None,
                metadata={
                    "type": "Attribute",
                    "namespace": "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.2",
                },
            )
            choice_ref: Optional[str] = field(
                default=None,
                metadata={
                    "name": "choiceRef",
                    "type": "Attribute",
                    "namespace": "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.2",
                },
            )
            choice_style: Optional[ChoiceStyleValue] = field(
                default=None,
                metadata={
                    "name": "choiceStyle",
                    "type": "Attribute",
                    "namespace": "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.2",
                },
            )
            direction: Optional[DirectionValue] = field(
                default=None,
                metadata={
                    "type": "Attribute",
                    "namespace": "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.2",
                },
            )
            config_groups: Iterable[str] = field(
                default_factory=list,
                metadata={
                    "name": "configGroups",
                    "type": "Attribute",
                    "namespace": "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.2",
                    "tokens": True,
                },
            )
            format: Optional[FormatType] = field(
                default=None,
                metadata={
                    "type": "Attribute",
                    "namespace": "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.2",
                },
            )
            prompt: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Attribute",
                    "namespace": "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.2",
                },
            )
            any_attributes: Mapping[str, str] = field(
                default_factory=dict,
                metadata={
                    "type": "Attributes",
                    "namespace": "##any",
                },
            )
