from collections.abc import Iterable
from dataclasses import dataclass, field

from org.accellera.spirit.v1685_2009.ve.ams.generator_type import GeneratorType
from org.accellera.spirit.v1685_2009.ve.ams.instance_generator_type_scope import (
    InstanceGeneratorTypeScope,
)

__NAMESPACE__ = "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1685-2009"


@dataclass(slots=True)
class InstanceGeneratorType(GeneratorType):
    """
    :ivar group: An identifier to specify the generator group. This is
        used by generator chains for selecting which generators to run.
    :ivar scope: The scope attribute applies to component generators and
        specifies whether the generator should be run for each instance
        of the entity (or module) or just once for all instances of the
        entity.
    """

    class Meta:
        name = "instanceGeneratorType"

    group: Iterable[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1685-2009",
        },
    )
    scope: InstanceGeneratorTypeScope = field(
        default=InstanceGeneratorTypeScope.INSTANCE,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1685-2009",
        },
    )
