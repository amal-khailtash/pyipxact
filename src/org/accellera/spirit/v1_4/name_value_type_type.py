from dataclasses import dataclass, field
from typing import Optional

from org.accellera.spirit.v1_4.name_value_pair_type import NameValuePairType
from org.accellera.spirit.v1_4.name_value_type_type_usage_type import (
    NameValueTypeTypeUsageType,
)

__NAMESPACE__ = "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.4"


@dataclass(slots=True)
class NameValueTypeType(NameValuePairType):
    """
    Name value pair with data type information.

    :ivar data_type: The data type of the argument as pertains to the
        language. Example: "int", "double", "char *".
    :ivar usage_type: Indicates the type of the model parameter. Legal
        values are defined in the attribute enumeration list. Default
        value is 'nontyped'.
    """

    class Meta:
        name = "nameValueTypeType"

    data_type: Optional[str] = field(
        default=None,
        metadata={
            "name": "dataType",
            "type": "Attribute",
            "namespace": "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.4",
        },
    )
    usage_type: NameValueTypeTypeUsageType = field(
        default=NameValueTypeTypeUsageType.NONTYPED,
        metadata={
            "name": "usageType",
            "type": "Attribute",
            "namespace": "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.4",
        },
    )
