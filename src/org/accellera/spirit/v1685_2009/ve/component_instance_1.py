from dataclasses import dataclass, field
from typing import Optional

from org.accellera.spirit.v1685_2009.ve.configurable_element_values import (
    ConfigurableElementValues,
)
from org.accellera.spirit.v1685_2009.ve.description import Description
from org.accellera.spirit.v1685_2009.ve.display_name import DisplayName
from org.accellera.spirit.v1685_2009.ve.instance_name import InstanceName
from org.accellera.spirit.v1685_2009.ve.library_ref_type import LibraryRefType
from org.accellera.spirit.v1685_2009.ve.vendor_extensions import (
    VendorExtensions,
)

__NAMESPACE__ = "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1685-2009"


@dataclass(slots=True)
class ComponentInstance1:
    """Component instance element.

    The instance name is contained in the unique-value instanceName
    attribute.

    :ivar instance_name:
    :ivar display_name:
    :ivar description:
    :ivar component_ref: References a component to be found in an
        external library.  The four attributes define the VLNV of the
        referenced element.
    :ivar configurable_element_values:
    :ivar vendor_extensions:
    """

    class Meta:
        name = "componentInstance"
        namespace = (
            "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1685-2009"
        )

    instance_name: Optional[InstanceName] = field(
        default=None,
        metadata={
            "name": "instanceName",
            "type": "Element",
            "required": True,
        },
    )
    display_name: Optional[DisplayName] = field(
        default=None,
        metadata={
            "name": "displayName",
            "type": "Element",
        },
    )
    description: Optional[Description] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    component_ref: Optional[LibraryRefType] = field(
        default=None,
        metadata={
            "name": "componentRef",
            "type": "Element",
            "required": True,
        },
    )
    configurable_element_values: Optional[ConfigurableElementValues] = field(
        default=None,
        metadata={
            "name": "configurableElementValues",
            "type": "Element",
        },
    )
    vendor_extensions: Optional[VendorExtensions] = field(
        default=None,
        metadata={
            "name": "vendorExtensions",
            "type": "Element",
        },
    )