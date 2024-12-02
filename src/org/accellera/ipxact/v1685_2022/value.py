from dataclasses import dataclass

from org.accellera.ipxact.v1685_2022.string_expression import StringExpression

__NAMESPACE__ = "http://www.accellera.org/XMLSchema/IPXACT/1685-2022"


@dataclass(slots=True)
class Value(StringExpression):
    """
    The value of the parameter.
    """

    class Meta:
        name = "value"
        namespace = "http://www.accellera.org/XMLSchema/IPXACT/1685-2022"
