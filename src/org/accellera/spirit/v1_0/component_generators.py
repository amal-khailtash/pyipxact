from collections.abc import Iterable
from dataclasses import dataclass, field

from org.accellera.spirit.v1_0.component_generator import ComponentGenerator

__NAMESPACE__ = "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.0"


@dataclass(slots=True)
class ComponentGenerators:
    """
    List of component generators.
    """

    class Meta:
        name = "componentGenerators"
        namespace = "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.0"

    component_generator: Iterable[ComponentGenerator] = field(
        default_factory=list,
        metadata={
            "name": "componentGenerator",
            "type": "Element",
        },
    )