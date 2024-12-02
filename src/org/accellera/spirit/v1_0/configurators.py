from collections.abc import Iterable, Mapping
from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.0"


@dataclass(slots=True)
class Configurators:
    """Set of configurators on a configurable object.

    The contents of this container element are undefined for version 1.0
    of the SPIRIT schema. It is expected that the contents will be
    defined when the tight generator interface is available. In this
    release only 'default' configurators are supported.

    :ivar any_element: Accepts any element(s) the content provider wants
        to put here, including elements from the SPIRIT namespace.
    :ivar any_attributes:
    """

    class Meta:
        name = "configurators"
        namespace = "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.0"

    any_element: Iterable[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        },
    )
    any_attributes: Mapping[str, str] = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "##any",
        },
    )
