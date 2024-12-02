from dataclasses import dataclass, field

from org.accellera.spirit.v1_2.instance_generator_type import (
    InstanceGeneratorType,
)

__NAMESPACE__ = "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.2"


@dataclass(slots=True)
class ComponentGenerator(InstanceGeneratorType):
    """Specifies a set of component generators.

    The scope attribute applies to component generators and specifies
    whether the generator should be run for each instance of the entity
    (or module) or just once for all instances of the entity.

    :ivar hidden: If this attribute is true then the generator should
        not be presented to the user, it may be part of a chain and has
        no useful meaning when invoked standalone.
    """

    class Meta:
        name = "componentGenerator"
        namespace = "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.2"

    hidden: bool = field(
        default=False,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.2",
        },
    )
