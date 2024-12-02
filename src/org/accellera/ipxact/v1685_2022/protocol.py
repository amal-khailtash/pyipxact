from dataclasses import dataclass, field
from typing import Optional

from org.accellera.ipxact.v1685_2022.payload import Payload
from org.accellera.ipxact.v1685_2022.protocol_type_type import ProtocolTypeType

__NAMESPACE__ = "http://www.accellera.org/XMLSchema/IPXACT/1685-2022"


@dataclass(slots=True)
class Protocol:
    """Defines the protocol type.

    Defaults to tlm_base_protocol_type for TLM sockets
    """

    class Meta:
        name = "protocol"
        namespace = "http://www.accellera.org/XMLSchema/IPXACT/1685-2022"

    protocol_type: Optional["Protocol.ProtocolType"] = field(
        default=None,
        metadata={
            "name": "protocolType",
            "type": "Element",
            "required": True,
        },
    )
    payload: Optional[Payload] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )

    @dataclass(slots=True)
    class ProtocolType:
        value: Optional[ProtocolTypeType] = field(
            default=None,
            metadata={
                "required": True,
            },
        )
        custom: Optional[str] = field(
            default=None,
            metadata={
                "type": "Attribute",
            },
        )
