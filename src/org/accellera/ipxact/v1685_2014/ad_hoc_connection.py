from collections.abc import Iterable
from dataclasses import dataclass, field
from typing import Optional

from org.accellera.ipxact.v1685_2014.complex_tied_value_type import (
    ComplexTiedValueType,
)
from org.accellera.ipxact.v1685_2014.description import Description
from org.accellera.ipxact.v1685_2014.display_name import DisplayName
from org.accellera.ipxact.v1685_2014.external_port_reference import (
    ExternalPortReference,
)
from org.accellera.ipxact.v1685_2014.is_present import IsPresent
from org.accellera.ipxact.v1685_2014.part_select import PartSelect
from org.accellera.ipxact.v1685_2014.vendor_extensions import VendorExtensions

__NAMESPACE__ = "http://www.accellera.org/XMLSchema/IPXACT/1685-2014"


@dataclass(slots=True)
class AdHocConnection:
    """
    Represents an ad-hoc connection between component ports.

    :ivar name: Unique name
    :ivar display_name:
    :ivar description:
    :ivar is_present:
    :ivar tied_value: The logic value of this connection. The value can
        be an unsigned longint expression or open or default. Only valid
        for ports of style wire.
    :ivar port_references: Liist of internal and external port
        references involved in the adhocConnection
    :ivar vendor_extensions:
    :ivar id:
    """

    class Meta:
        name = "adHocConnection"
        namespace = "http://www.accellera.org/XMLSchema/IPXACT/1685-2014"

    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
            "white_space": "collapse",
            "pattern": r"\i[\p{L}\p{N}\.\-:_]*",
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
    is_present: Optional[IsPresent] = field(
        default=None,
        metadata={
            "name": "isPresent",
            "type": "Element",
        },
    )
    tied_value: Optional[ComplexTiedValueType] = field(
        default=None,
        metadata={
            "name": "tiedValue",
            "type": "Element",
        },
    )
    port_references: Optional["AdHocConnection.PortReferences"] = field(
        default=None,
        metadata={
            "name": "portReferences",
            "type": "Element",
            "required": True,
        },
    )
    vendor_extensions: Optional[VendorExtensions] = field(
        default=None,
        metadata={
            "name": "vendorExtensions",
            "type": "Element",
        },
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )

    @dataclass(slots=True)
    class PortReferences:
        """
        :ivar internal_port_reference: Defines a reference to a port on
            a component contained within the design.
        :ivar external_port_reference:
        """

        internal_port_reference: Iterable[
            "AdHocConnection.PortReferences.InternalPortReference"
        ] = field(
            default_factory=list,
            metadata={
                "name": "internalPortReference",
                "type": "Element",
                "min_occurs": 1,
            },
        )
        external_port_reference: Iterable[ExternalPortReference] = field(
            default_factory=list,
            metadata={
                "name": "externalPortReference",
                "type": "Element",
                "min_occurs": 1,
                "sequence": 1,
            },
        )

        @dataclass(slots=True)
        class InternalPortReference:
            """
            :ivar is_present:
            :ivar part_select:
            :ivar component_ref: A reference to the instanceName element
                of a component in this design.
            :ivar port_ref: A port on the on the referenced component
                from componentRef.
            :ivar id:
            """

            is_present: Optional[IsPresent] = field(
                default=None,
                metadata={
                    "name": "isPresent",
                    "type": "Element",
                },
            )
            part_select: Optional[PartSelect] = field(
                default=None,
                metadata={
                    "name": "partSelect",
                    "type": "Element",
                },
            )
            component_ref: Optional[str] = field(
                default=None,
                metadata={
                    "name": "componentRef",
                    "type": "Attribute",
                    "required": True,
                },
            )
            port_ref: Optional[str] = field(
                default=None,
                metadata={
                    "name": "portRef",
                    "type": "Attribute",
                    "required": True,
                    "white_space": "collapse",
                    "pattern": r"\i[\p{L}\p{N}\.\-:_]*",
                },
            )
            id: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Attribute",
                    "namespace": "http://www.w3.org/XML/1998/namespace",
                },
            )
