from dataclasses import dataclass, field
from typing import Optional

from org.accellera.ipxact.v1685_2014.is_present import IsPresent
from org.accellera.ipxact.v1685_2014.module_parameter_type_usage_type import (
    ModuleParameterTypeUsageType,
)
from org.accellera.ipxact.v1685_2014.parameter_type import ParameterType

__NAMESPACE__ = "http://www.accellera.org/XMLSchema/IPXACT/1685-2014"


@dataclass(slots=True)
class ModuleParameterType(ParameterType):
    """
    Name value pair with data type information.

    :ivar is_present:
    :ivar data_type: The data type of the argument as pertains to the
        language. Example: "int", "double", "char *".
    :ivar usage_type: Indicates the type of the module parameter. Legal
        values are defined in the attribute enumeration list. Default
        value is 'nontyped'.
    """

    class Meta:
        name = "moduleParameterType"

    is_present: Optional[IsPresent] = field(
        default=None,
        metadata={
            "name": "isPresent",
            "type": "Element",
            "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2014",
        },
    )
    data_type: Optional[str] = field(
        default=None,
        metadata={
            "name": "dataType",
            "type": "Attribute",
        },
    )
    usage_type: ModuleParameterTypeUsageType = field(
        default=ModuleParameterTypeUsageType.NONTYPED,
        metadata={
            "name": "usageType",
            "type": "Attribute",
        },
    )
