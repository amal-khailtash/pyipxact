from dataclasses import dataclass

from org.accellera.ipxact.v1685_2014.parameter_type import ParameterType

__NAMESPACE__ = "http://www.accellera.org/XMLSchema/IPXACT/1685-2014"


@dataclass(slots=True)
class Parameter(ParameterType):
    """A name value pair.

    The name is specified by the name element.  The value is in the text
    content of the value element.  This value element supports all
    configurability attributes.
    """

    class Meta:
        name = "parameter"
        namespace = "http://www.accellera.org/XMLSchema/IPXACT/1685-2014"
