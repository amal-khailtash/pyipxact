from dataclasses import dataclass, field

from org.accellera.ipxact.v1685_2014.parameter_base_type import (
    ParameterBaseType,
)
from org.accellera.ipxact.v1685_2014.parameter_type_resolve import (
    ParameterTypeResolve,
)

__NAMESPACE__ = "http://www.accellera.org/XMLSchema/IPXACT/1685-2014"


@dataclass(slots=True)
class ParameterType(ParameterBaseType):
    """
    :ivar resolve: Determines how a property value can be configured.
    """

    class Meta:
        name = "parameterType"

    resolve: ParameterTypeResolve = field(
        default=ParameterTypeResolve.IMMEDIATE,
        metadata={
            "type": "Attribute",
        },
    )
