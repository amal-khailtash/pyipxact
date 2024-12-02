from dataclasses import dataclass

from org.accellera.spirit.v1_5.generator_type import GeneratorType

__NAMESPACE__ = "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.5"


@dataclass(slots=True)
class Generator(GeneratorType):
    """
    Specifies a set of generators.
    """

    class Meta:
        name = "generator"
        namespace = "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.5"
