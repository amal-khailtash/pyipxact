from dataclasses import dataclass

from org.accellera.ipxact.v1685_2022.qualified_expression import (
    QualifiedExpression,
)

__NAMESPACE__ = "http://www.accellera.org/XMLSchema/IPXACT/1685-2022"


@dataclass(slots=True)
class DefaultValue(QualifiedExpression):
    """
    Default value for a wire port.
    """

    class Meta:
        name = "defaultValue"
        namespace = "http://www.accellera.org/XMLSchema/IPXACT/1685-2022"
