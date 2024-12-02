from dataclasses import dataclass

from org.accellera.ipxact.v1685_2022.write_value_constraint_type import (
    WriteValueConstraintType,
)

__NAMESPACE__ = "http://www.accellera.org/XMLSchema/IPXACT/1685-2022"


@dataclass(slots=True)
class WriteValueConstraint(WriteValueConstraintType):
    """The legal values that may be written to a field.

    If not specified the legal values are not specified.
    """

    class Meta:
        name = "writeValueConstraint"
        namespace = "http://www.accellera.org/XMLSchema/IPXACT/1685-2022"
