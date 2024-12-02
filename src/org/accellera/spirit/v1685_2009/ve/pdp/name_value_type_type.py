from dataclasses import dataclass, field
from typing import Optional

from org.accellera.spirit.v1685_2009.ve.pdp.name_value_pair_type_1 import (
    NameValuePairType1,
)
from org.accellera.spirit.v1685_2009.ve.pdp.name_value_type_type_usage_type import (
    NameValueTypeTypeUsageType,
)

__NAMESPACE__ = "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1685-2009"


@dataclass(slots=True)
class NameValueTypeType(NameValuePairType1):
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
            "namespace": "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1685-2009",
        },
    )
    usage_type: NameValueTypeTypeUsageType = field(
        default=NameValueTypeTypeUsageType.NONTYPED,
        metadata={
            "name": "usageType",
            "type": "Attribute",
            "namespace": "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1685-2009",
        },
    )
