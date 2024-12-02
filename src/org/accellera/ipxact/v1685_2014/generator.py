from dataclasses import dataclass

from org.accellera.ipxact.v1685_2014.generator_type import GeneratorType

__NAMESPACE__ = "http://www.accellera.org/XMLSchema/IPXACT/1685-2014"


@dataclass(slots=True)
class Generator(GeneratorType):
    """
    Specifies a set of generators.
    """

    class Meta:
        name = "generator"
        namespace = "http://www.accellera.org/XMLSchema/IPXACT/1685-2014"
