from dataclasses import dataclass

from org.accellera.ipxact.v1685_2022.ve.complex_base_expression import (
    ComplexBaseExpression,
)

__NAMESPACE__ = "http://www.accellera.org/XMLSchema/IPXACT/1685-2022"


@dataclass(slots=True)
class StringUriexpression(ComplexBaseExpression):
    """
    IP-XACT URI, like a standard xs:anyURI except that it can contain environment
    variables in the ${ } form, to be replaced by their value to provide the
    underlying URI.
    """

    class Meta:
        name = "stringURIExpression"
