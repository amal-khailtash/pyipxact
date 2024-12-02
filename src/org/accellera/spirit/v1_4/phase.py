from dataclasses import dataclass, field
from typing import Optional

from org.accellera.spirit.v1_4.phase_scope_type import PhaseScopeType

__NAMESPACE__ = "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.4"


@dataclass(slots=True)
class Phase:
    """This is an non-negative floating point number that is used to sequence when
    a generator is run.

    The generators are run in order starting with zero. There may be
    multiple generators with the same phase number. In this case, the
    order should not matter with respect to other generators at the same
    phase. If no phase number is given the generator will be considered
    in the "last" phase and these generators will be run in the order in
    which they are encountered while processing generator elements.
    """

    class Meta:
        name = "phase"
        namespace = "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.4"

    value: Optional[float] = field(
        default=None,
        metadata={
            "required": True,
        },
    )
    scope: PhaseScopeType = field(
        default=PhaseScopeType.GLOBAL,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.4",
        },
    )
