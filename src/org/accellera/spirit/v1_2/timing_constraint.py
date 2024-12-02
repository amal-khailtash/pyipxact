from dataclasses import dataclass, field
from typing import Optional

from org.accellera.spirit.v1_2.delay import Delay
from org.accellera.spirit.v1_2.delay_value_type import DelayValueType
from org.accellera.spirit.v1_2.edge_value_type import EdgeValueType

__NAMESPACE__ = "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.2"


@dataclass(slots=True)
class TimingConstraint:
    """Defines a timing constraint for the associated signal.

    The constraint is relative to the clock specified by the clockName
    attribute. The clockEdge indicates which clock edge the constraint
    is associated with (default is rising edge). The delayType attribute
    can be specified to further refine the constraint.

    :ivar percent_of_period: Defines a delay constraint value which is
        defined as a percentage of the corresponding clock cycle time.
    :ivar delay: Defines an absolute delay constraint value. The units
        attribute can be used to specify units if needed. The default
        units are ns.
    :ivar clock_edge:
    :ivar delay_type:
    :ivar clock_name:
    """

    class Meta:
        name = "timingConstraint"
        namespace = "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.2"

    percent_of_period: Optional[float] = field(
        default=None,
        metadata={
            "name": "percentOfPeriod",
            "type": "Element",
            "min_inclusive": 0.0,
            "max_inclusive": 100.0,
        },
    )
    delay: Optional[Delay] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    clock_edge: Optional[EdgeValueType] = field(
        default=None,
        metadata={
            "name": "clockEdge",
            "type": "Attribute",
            "namespace": "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.2",
        },
    )
    delay_type: Optional[DelayValueType] = field(
        default=None,
        metadata={
            "name": "delayType",
            "type": "Attribute",
            "namespace": "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.2",
        },
    )
    clock_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "clockName",
            "type": "Attribute",
            "namespace": "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.2",
            "required": True,
        },
    )
