from dataclasses import dataclass

from org.accellera.spirit.v1685_2009.instance_generator_type import (
    InstanceGeneratorType,
)

__NAMESPACE__ = "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1685-2009"


@dataclass(slots=True)
class AbstractorGenerator(InstanceGeneratorType):
    """Specifies a set of abstractor generators.

    The scope attribute applies to abstractor generators and specifies
    whether the generator should be run for each instance of the entity
    (or module) or just once for all instances of the entity.
    """

    class Meta:
        name = "abstractorGenerator"
        namespace = (
            "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1685-2009"
        )
