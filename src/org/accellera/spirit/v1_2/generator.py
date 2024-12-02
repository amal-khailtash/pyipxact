from dataclasses import dataclass

from org.accellera.spirit.v1_2.generator_type import GeneratorType

__NAMESPACE__ = "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.2"


@dataclass(slots=True)
class Generator(GeneratorType):
    """
    Specifies a set of generators.
    """

    class Meta:
        name = "generator"
        namespace = "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.2"
