from collections.abc import Iterable
from dataclasses import dataclass, field
from typing import Optional

from org.accellera.spirit.v1_5.description import Description
from org.accellera.spirit.v1_5.display_name import DisplayName

__NAMESPACE__ = "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.5"


@dataclass(slots=True)
class AdHocConnection:
    """
    Represents an ad-hoc connection between component ports.

    :ivar name: Unique name
    :ivar display_name:
    :ivar description:
    :ivar internal_port_reference: Defines a reference to a port on a
        component contained within the design.
    :ivar external_port_reference: Defines a reference to a port on the
        component containing this design. The portRef attribute
        indicates the name of the port in the containing component.
    :ivar tied_value: The logic value of this connection. Only valid for
        ports of style wire.
    """

    class Meta:
        name = "adHocConnection"
        namespace = "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.5"

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
    internal_port_reference: Iterable[
        "AdHocConnection.InternalPortReference"
    ] = field(
        default_factory=list,
        metadata={
            "name": "internalPortReference",
            "type": "Element",
            "min_occurs": 1,
        },
    )
    external_port_reference: Iterable[
        "AdHocConnection.ExternalPortReference"
    ] = field(
        default_factory=list,
        metadata={
            "name": "externalPortReference",
            "type": "Element",
        },
    )
    tied_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "tiedValue",
            "type": "Attribute",
            "namespace": "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.5",
            "pattern": r"[+]?(0x|0X|#)?[0-9a-fA-F]+[kmgtKMGT]?",
        },
    )

    @dataclass(slots=True)
    class InternalPortReference:
        """
        :ivar component_ref: A reference to the instanceName element of
            a component in this design.
        :ivar port_ref: A port on the on the referenced component from
            componentRef.
        :ivar left: Left index of a vector.
        :ivar right: Right index of a vector.
        """

        component_ref: Optional[str] = field(
            default=None,
            metadata={
                "name": "componentRef",
                "type": "Attribute",
                "namespace": "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.5",
                "required": True,
            },
        )
        port_ref: Optional[str] = field(
            default=None,
            metadata={
                "name": "portRef",
                "type": "Attribute",
                "namespace": "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.5",
                "required": True,
                "white_space": "collapse",
                "pattern": r"\i[\p{L}\p{N}\.\-:_]*",
            },
        )
        left: Optional[int] = field(
            default=None,
            metadata={
                "type": "Attribute",
                "namespace": "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.5",
            },
        )
        right: Optional[int] = field(
            default=None,
            metadata={
                "type": "Attribute",
                "namespace": "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.5",
            },
        )

    @dataclass(slots=True)
    class ExternalPortReference:
        """
        :ivar port_ref: A port on the top level component.
        :ivar left: Left index of a vector.
        :ivar right: Right index of a vector.
        """

        port_ref: Optional[str] = field(
            default=None,
            metadata={
                "name": "portRef",
                "type": "Attribute",
                "namespace": "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.5",
                "required": True,
                "white_space": "collapse",
                "pattern": r"\i[\p{L}\p{N}\.\-:_]*",
            },
        )
        left: Optional[int] = field(
            default=None,
            metadata={
                "type": "Attribute",
                "namespace": "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.5",
            },
        )
        right: Optional[int] = field(
            default=None,
            metadata={
                "type": "Attribute",
                "namespace": "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.5",
            },
        )
