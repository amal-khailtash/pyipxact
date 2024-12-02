from dataclasses import dataclass

from org.accellera.spirit.v1685_2009.ve.core.generator_type import (
    GeneratorType,
)

__NAMESPACE__ = "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1685-2009"


@dataclass(slots=True)
class Generator(GeneratorType):
    """
    Specifies a set of generators.
    """

    class Meta:
        name = "generator"
        namespace = (
            "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1685-2009"
        )
