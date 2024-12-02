from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1685-2009"


@dataclass(slots=True)
class GeneratorRef:
    """
    A reference to a generator element.
    """

    class Meta:
        name = "generatorRef"
        namespace = (
            "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1685-2009"
        )

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )
