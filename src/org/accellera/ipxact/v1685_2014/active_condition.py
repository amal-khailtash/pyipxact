from dataclasses import dataclass

from org.accellera.ipxact.v1685_2014.unsigned_bit_expression import (
    UnsignedBitExpression,
)

__NAMESPACE__ = "http://www.accellera.org/XMLSchema/IPXACT/1685-2014"


@dataclass(slots=True)
class ActiveCondition(UnsignedBitExpression):
    """Expression that determines whether the enclosing element responds to read or
    write accesses to its specified address location.

    The expression can include dynamic values referencing register/field
    values and component states.  If it evaluates to true, then the
    enclosing register can be accessed per its mapping and access
    specification.  If it evaluates to false, the enclosing
    register/field cannot be accessed.  If a register does not include
    an activeCondition or alternateRegister(s), then the register is
    uncondiitionally accessible.  If a register does not include an
    activeCondition, but does include alternateRegister(s), then the
    condition that determines which is accessible is considered
    unspecified.
    """

    class Meta:
        name = "activeCondition"
        namespace = "http://www.accellera.org/XMLSchema/IPXACT/1685-2014"
