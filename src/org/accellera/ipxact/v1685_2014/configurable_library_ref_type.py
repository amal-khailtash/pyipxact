from dataclasses import dataclass, field
from typing import Optional

from org.accellera.ipxact.v1685_2014.configurable_element_values import (
    ConfigurableElementValues,
)

__NAMESPACE__ = "http://www.accellera.org/XMLSchema/IPXACT/1685-2014"


@dataclass(slots=True)
class ConfigurableLibraryRefType:
    """Base IP-XACT document reference type for configurable top-level objects.

    Contains vendor, library, name and version attributes along with
    configurable element values.
    """

    class Meta:
        name = "configurableLibraryRefType"

    configurable_element_values: Optional[ConfigurableElementValues] = field(
        default=None,
        metadata={
            "name": "configurableElementValues",
            "type": "Element",
            "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2014",
        },
    )
    vendor: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    library: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    version: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )