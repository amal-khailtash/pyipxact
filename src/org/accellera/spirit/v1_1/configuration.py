from collections.abc import Iterable
from dataclasses import dataclass, field

from org.accellera.spirit.v1_1.configurable_element import ConfigurableElement

__NAMESPACE__ = "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.1"


@dataclass(slots=True)
class Configuration:
    """
    All configuration information for a contained component or channel instance.
    """

    class Meta:
        name = "configuration"
        namespace = "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.1"

    configurable_element: Iterable[ConfigurableElement] = field(
        default_factory=list,
        metadata={
            "name": "configurableElement",
            "type": "Element",
        },
    )
