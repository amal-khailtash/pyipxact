from dataclasses import dataclass, field
from typing import Optional

from org.accellera.spirit.v1_1.name_value_pair_type import NameValuePairType

__NAMESPACE__ = "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.1"


@dataclass(slots=True)
class NameValueTypeType(NameValuePairType):
    """
    Name value pair with data type information.

    :ivar data_type: The data type of the argumen as pertains to the
        language. Example: "int", "double", "char *".
    """

    class Meta:
        name = "nameValueTypeType"

    data_type: Optional[str] = field(
        default=None,
        metadata={
            "name": "dataType",
            "type": "Attribute",
            "namespace": "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.1",
        },
    )
