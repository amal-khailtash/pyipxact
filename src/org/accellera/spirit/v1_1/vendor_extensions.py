from collections.abc import Iterable
from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.1"


@dataclass(slots=True)
class VendorExtensions:
    """
    Container for vendor specific extensions.

    :ivar any_element: Accepts any element(s) the content provider wants
        to put here, including elements from the SPIRIT namespace.
    """

    class Meta:
        name = "vendorExtensions"
        namespace = "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.1"

    any_element: Iterable[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        },
    )