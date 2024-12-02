from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.0"


@dataclass(slots=True)
class ConfiguratorRef:
    """
    A reference to a configurator element.
    """

    class Meta:
        name = "configuratorRef"
        namespace = "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.0"

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )
