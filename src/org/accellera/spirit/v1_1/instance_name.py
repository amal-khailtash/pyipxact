from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.1"


@dataclass(slots=True)
class InstanceName:
    """
    An instance name assigned to subcomponent instances and contained channels,
    that is unique within the parent component.
    """

    class Meta:
        name = "instanceName"
        namespace = "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.1"

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )