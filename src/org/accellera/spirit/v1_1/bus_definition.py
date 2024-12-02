from collections.abc import Iterable
from dataclasses import dataclass, field
from typing import Optional

from org.accellera.spirit.v1_1.bus_def_signal_constraint_sets import (
    BusDefSignalConstraintSets,
)
from org.accellera.spirit.v1_1.choices import Choices
from org.accellera.spirit.v1_1.default_value_strength import (
    DefaultValueStrength,
)
from org.accellera.spirit.v1_1.library_ref_type import LibraryRefType
from org.accellera.spirit.v1_1.on_master_value import OnMasterValue
from org.accellera.spirit.v1_1.on_slave_value import OnSlaveValue
from org.accellera.spirit.v1_1.on_system_value import OnSystemValue
from org.accellera.spirit.v1_1.requires_driver import RequiresDriver
from org.accellera.spirit.v1_1.vendor_extensions import VendorExtensions

__NAMESPACE__ = "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.1"


@dataclass(slots=True)
class BusDefinition:
    """
    Defines the signals and high-level function of a bus.

    :ivar vendor: Name of the vendor who supplies this file.
    :ivar library: Name of the logical library this component belongs
        to.  Note that a physical library may contain components from
        multiple logical libraries.  Logical libraries are displayes in
        component browser.
    :ivar name: The name of the object.  Must match the root name of the
        XML file and the directory name it or its version directory
        belongs to.
    :ivar version:
    :ivar direct_connection: When present this element indicates that a
        master interface may be directly connected to a slave interface
        (under certain conditions) for busses of this type.
    :ivar extends: Optional name of bus type that this bus definition is
        compatible with. This bus definition may change the definitions
        of signals in the existing bus definition and add new signals,
        the signals in the original bus are not deleted but may be
        marked illegal to disallow their use.
    :ivar max_masters: Indicates the maximum number of masters this bus
        supports.  Default value of zero means unbounded.
    :ivar max_slaves: Indicates the maximum number of slaves this bus
        supports.  Default value of zero means unbounded.
    :ivar signals: This is a list of logical signals defined by the bus.
    :ivar choices:
    :ivar vendor_extensions:
    """

    class Meta:
        name = "busDefinition"
        namespace = "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.1"

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
    direct_connection: Optional[bool] = field(
        default=None,
        metadata={
            "name": "directConnection",
            "type": "Element",
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
                contains clock information.
            :ivar is_reset: Is this element is present, the signal
                contains reset information.
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
                    will define th enumber of bits in this signal.
                :ivar direction: If this element is present, the
                    direction of this signal is restricted to the
                    specified value. The direction is relative to the
                    non-mirrored interface.
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
                    will define th enumber of bits in this signal.
                :ivar direction: If this element is present, the
                    direction of this signal is restricted to the
                    specified value. The direction is relative to the
                    non-mirrored interface.
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
                    will define th enumber of bits in this signal.
                :ivar direction: If this element is present, the
                    direction of this signal is restricted to the
                    specified value. The direction is relative to the
                    non-mirrored interface.
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
                :ivar strength: The strength of the signal. "strong"
                    (default) or "weak"
                :ivar value: The value of a signal. 1 or 0 for single
                    bit signals, unsigned numeric otherwise.
                """

                strength: Iterable[DefaultValueStrength] = field(
                    default_factory=list,
                    metadata={
                        "type": "Element",
                        "max_occurs": 2,
                    },
                )
                value: Optional[object] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                    },
                )
