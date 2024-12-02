from dataclasses import dataclass, field
from typing import Optional

from org.accellera.spirit.v1_2.configuration import Configuration
from org.accellera.spirit.v1_2.instance_name import InstanceName
from org.accellera.spirit.v1_2.library_ref_type import LibraryRefType
from org.accellera.spirit.v1_2.vendor_extensions import VendorExtensions

__NAMESPACE__ = "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.2"


@dataclass(slots=True)
class ComponentInstance:
    """Component instance element.

    The instance name is contained in the unique-value instanceName
    attribute.

    :ivar instance_name:
    :ivar component_ref: References a component to be found in an
        external library.  The name attribute gives the name of the
        component and the version attribute speicifies which version of
        the component to use.
    :ivar configuration:
    :ivar vendor_extensions:
    """

    class Meta:
        name = "componentInstance"
        namespace = "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.2"

    instance_name: Optional[InstanceName] = field(
        default=None,
        metadata={
            "name": "instanceName",
            "type": "Element",
            "required": True,
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
    configuration: Optional[Configuration] = field(
        default=None,
        metadata={
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
