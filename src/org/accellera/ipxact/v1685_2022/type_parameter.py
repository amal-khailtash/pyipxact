from dataclasses import dataclass

from org.accellera.ipxact.v1685_2022.module_parameter_type import (
    ModuleParameterType,
)

__NAMESPACE__ = "http://www.accellera.org/XMLSchema/IPXACT/1685-2022"


@dataclass(slots=True)
class TypeParameter(ModuleParameterType):
    """A typed parameter name value pair.

    The optional attribute dataType defines the type of the value and
    the usageType attribute indicates how the parameter is to be used.
    """

    class Meta:
        name = "typeParameter"
        namespace = "http://www.accellera.org/XMLSchema/IPXACT/1685-2022"