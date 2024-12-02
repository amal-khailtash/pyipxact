from collections.abc import Iterable
from dataclasses import dataclass, field
from typing import Optional

from org.accellera.spirit.v1685_2009.ve.core.service_type_initiative import (
    ServiceTypeInitiative,
)
from org.accellera.spirit.v1685_2009.ve.core.vendor_extensions import (
    VendorExtensions,
)

__NAMESPACE__ = "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1685-2009"


@dataclass(slots=True)
class ServiceType:
    """
    The service that this transactional port can provide or requires.

    :ivar initiative: If this element is present, the type of access is
        restricted to the specified value.
    :ivar type_name: Defines the name of the transactional interface
        type.
    :ivar vendor_extensions:
    """

    class Meta:
        name = "serviceType"

    initiative: ServiceTypeInitiative = field(
        default=ServiceTypeInitiative.REQUIRES,
        metadata={
            "type": "Element",
            "namespace": "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1685-2009",
            "required": True,
        },
    )
    type_name: Iterable["ServiceType.TypeName"] = field(
        default_factory=list,
        metadata={
            "name": "typeName",
            "type": "Element",
            "namespace": "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1685-2009",
            "min_occurs": 1,
        },
    )
    vendor_extensions: Optional[VendorExtensions] = field(
        default=None,
        metadata={
            "name": "vendorExtensions",
            "type": "Element",
            "namespace": "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1685-2009",
        },
    )

    @dataclass(slots=True)
    class TypeName:
        """
        :ivar value:
        :ivar implicit: Defines that the typeName supplied for this
            service is implicit and a netlister should not declare this
            service in a language specific top-level netlist
        """

        value: str = field(
            default="",
            metadata={
                "required": True,
            },
        )
        implicit: bool = field(
            default=False,
            metadata={
                "type": "Attribute",
                "namespace": "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1685-2009",
            },
        )
