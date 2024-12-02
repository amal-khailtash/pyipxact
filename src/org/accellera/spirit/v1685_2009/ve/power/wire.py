from collections.abc import Iterable
from dataclasses import dataclass, field
from typing import Optional

from org.accellera.spirit.v1685_2009.ve.power.combinational_paths import (
    CombinationalPaths,
)
from org.accellera.spirit.v1685_2009.ve.power.domain_type_defs import (
    DomainTypeDefs,
)
from org.accellera.spirit.v1685_2009.ve.power.driver_2 import Driver2
from org.accellera.spirit.v1685_2009.ve.power.register_count import (
    RegisterCount,
)
from org.accellera.spirit.v1685_2009.ve.power.signal_type_defs import (
    SignalTypeDefs,
)
from org.accellera.spirit.v1685_2009.ve.power.wire_power_defs import (
    WirePowerDefs,
)

__NAMESPACE__ = "http://www.accellera.org/XMLSchema/SPIRIT/1685-2009-VE"


@dataclass(slots=True)
class Wire:
    """
    Wire port extension.
    """

    class Meta:
        name = "wire"
        namespace = "http://www.accellera.org/XMLSchema/SPIRIT/1685-2009-VE"

    driver: Iterable[Driver2] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.accellera.org/XMLSchema/SPIRIT/1685-2009-VE/CORE-1.0",
        },
    )
    domain_type_defs: Optional[DomainTypeDefs] = field(
        default=None,
        metadata={
            "name": "domainTypeDefs",
            "type": "Element",
            "namespace": "http://www.accellera.org/XMLSchema/SPIRIT/1685-2009-VE/AMS-1.0",
        },
    )
    signal_type_defs: Optional[SignalTypeDefs] = field(
        default=None,
        metadata={
            "name": "signalTypeDefs",
            "type": "Element",
            "namespace": "http://www.accellera.org/XMLSchema/SPIRIT/1685-2009-VE/AMS-1.0",
        },
    )
    register_count: Optional[RegisterCount] = field(
        default=None,
        metadata={
            "name": "registerCount",
            "type": "Element",
            "namespace": "http://www.accellera.org/XMLSchema/SPIRIT/1685-2009-VE/PDP-1.0",
        },
    )
    combinational_paths: Optional[CombinationalPaths] = field(
        default=None,
        metadata={
            "name": "combinationalPaths",
            "type": "Element",
            "namespace": "http://www.accellera.org/XMLSchema/SPIRIT/1685-2009-VE/PDP-1.0",
        },
    )
    wire_power_defs: Optional[WirePowerDefs] = field(
        default=None,
        metadata={
            "name": "wirePowerDefs",
            "type": "Element",
            "namespace": "http://www.accellera.org/XMLSchema/SPIRIT/1685-2009-VE/POWER-1.0",
        },
    )
