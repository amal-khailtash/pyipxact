from collections.abc import Iterable
from dataclasses import dataclass, field
from typing import Optional

from org.accellera.ipxact.v1685_2014.access import Access
from org.accellera.ipxact.v1685_2014.description import Description
from org.accellera.ipxact.v1685_2014.display_name import DisplayName
from org.accellera.ipxact.v1685_2014.enumerated_values import EnumeratedValues
from org.accellera.ipxact.v1685_2014.is_present import IsPresent
from org.accellera.ipxact.v1685_2014.modified_write_value_type import (
    ModifiedWriteValueType,
)
from org.accellera.ipxact.v1685_2014.non_indexed_leaf_access_handle import (
    NonIndexedLeafAccessHandle,
)
from org.accellera.ipxact.v1685_2014.parameters import Parameters
from org.accellera.ipxact.v1685_2014.read_action_type import ReadActionType
from org.accellera.ipxact.v1685_2014.reset import Reset
from org.accellera.ipxact.v1685_2014.testable_test_constraint import (
    TestableTestConstraint,
)
from org.accellera.ipxact.v1685_2014.unsigned_bit_expression import (
    UnsignedBitExpression,
)
from org.accellera.ipxact.v1685_2014.unsigned_int_expression import (
    UnsignedIntExpression,
)
from org.accellera.ipxact.v1685_2014.unsigned_positive_int_expression import (
    UnsignedPositiveIntExpression,
)
from org.accellera.ipxact.v1685_2014.vendor_extensions import VendorExtensions
from org.accellera.ipxact.v1685_2014.volatile import Volatile
from org.accellera.ipxact.v1685_2014.write_value_constraint_type import (
    WriteValueConstraintType,
)

__NAMESPACE__ = "http://www.accellera.org/XMLSchema/IPXACT/1685-2014"


@dataclass(slots=True)
class FieldType:
    """
    A field within a register.

    :ivar name: Unique name
    :ivar display_name:
    :ivar description:
    :ivar access_handles:
    :ivar is_present:
    :ivar bit_offset: Offset of this field's bit 0 from bit 0 of the
        register.
    :ivar resets:
    :ivar type_identifier: Identifier name used to indicate that
        multiple field elements contain the exact same information for
        the elements in the fieldDefinitionGroup.
    :ivar bit_width: Width of the field in bits.
    :ivar volatile: Indicates whether the data is volatile. The presumed
        value is 'false' if not present.
    :ivar access:
    :ivar enumerated_values:
    :ivar modified_write_value: If present this element describes the
        modification of field data caused by a write operation.
        'oneToClear' means that in a bitwise fashion each write data bit
        of a one will clear the corresponding bit in the field.
        'oneToSet' means that in a bitwise fashion each write data bit
        of a one will set the corresponding bit in the field.
        'oneToToggle' means that in a bitwise fashion each write data
        bit of a one will toggle the corresponding bit in the field.
        'zeroToClear' means that in a bitwise fashion each write data
        bit of a zero will clear the corresponding bit in the field.
        'zeroToSet' means that in a bitwise fashion each write data bit
        of a zero will set the corresponding bit in the field.
        'zeroToToggle' means that in a bitwise fashion each write data
        bit of a zero will toggle the corresponding bit in the field.
        'clear' means any write to this field clears the field. 'set'
        means any write to the field sets the field. 'modify' means any
        write to this field may modify that data. If this element is not
        present the write operation data is written.
    :ivar write_value_constraint: The legal values that may be written
        to a field. If not specified the legal values are not specified.
    :ivar read_action: A list of possible actions for a read to set the
        field after the read. 'clear' means that after a read the field
        is cleared. 'set' means that after a read the field is set.
        'modify' means after a read the field is modified. If not
        present the field value is not modified after a read.
    :ivar testable: Can the field be tested with an automated register
        test routine. The presumed value is true if not specified.
    :ivar reserved: Indicates that the field should be documented as
        reserved. The presumed value is 'false' if not present.
    :ivar parameters:
    :ivar vendor_extensions:
    :ivar id:
    :ivar field_id: A unique identifier within a component for a field.
    """

    class Meta:
        name = "fieldType"

    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2014",
            "required": True,
        },
    )
    display_name: Optional[DisplayName] = field(
        default=None,
        metadata={
            "name": "displayName",
            "type": "Element",
            "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2014",
        },
    )
    description: Optional[Description] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2014",
        },
    )
    access_handles: Optional["FieldType.AccessHandles"] = field(
        default=None,
        metadata={
            "name": "accessHandles",
            "type": "Element",
            "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2014",
        },
    )
    is_present: Optional[IsPresent] = field(
        default=None,
        metadata={
            "name": "isPresent",
            "type": "Element",
            "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2014",
        },
    )
    bit_offset: Optional[UnsignedIntExpression] = field(
        default=None,
        metadata={
            "name": "bitOffset",
            "type": "Element",
            "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2014",
            "required": True,
        },
    )
    resets: Optional["FieldType.Resets"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2014",
        },
    )
    type_identifier: Optional[str] = field(
        default=None,
        metadata={
            "name": "typeIdentifier",
            "type": "Element",
            "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2014",
        },
    )
    bit_width: Optional[UnsignedPositiveIntExpression] = field(
        default=None,
        metadata={
            "name": "bitWidth",
            "type": "Element",
            "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2014",
            "required": True,
        },
    )
    volatile: Optional[Volatile] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2014",
        },
    )
    access: Optional[Access] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2014",
        },
    )
    enumerated_values: Optional[EnumeratedValues] = field(
        default=None,
        metadata={
            "name": "enumeratedValues",
            "type": "Element",
            "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2014",
        },
    )
    modified_write_value: Optional["FieldType.ModifiedWriteValue"] = field(
        default=None,
        metadata={
            "name": "modifiedWriteValue",
            "type": "Element",
            "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2014",
        },
    )
    write_value_constraint: Optional[WriteValueConstraintType] = field(
        default=None,
        metadata={
            "name": "writeValueConstraint",
            "type": "Element",
            "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2014",
        },
    )
    read_action: Optional["FieldType.ReadAction"] = field(
        default=None,
        metadata={
            "name": "readAction",
            "type": "Element",
            "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2014",
        },
    )
    testable: Optional["FieldType.Testable"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2014",
        },
    )
    reserved: Optional[UnsignedBitExpression] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2014",
        },
    )
    parameters: Optional[Parameters] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2014",
        },
    )
    vendor_extensions: Optional[VendorExtensions] = field(
        default=None,
        metadata={
            "name": "vendorExtensions",
            "type": "Element",
            "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2014",
        },
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )
    field_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "fieldID",
            "type": "Attribute",
        },
    )

    @dataclass(slots=True)
    class AccessHandles:
        access_handle: Iterable[NonIndexedLeafAccessHandle] = field(
            default_factory=list,
            metadata={
                "name": "accessHandle",
                "type": "Element",
                "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2014",
                "min_occurs": 1,
            },
        )

    @dataclass(slots=True)
    class Resets:
        """
        :ivar reset: BitField reset value
        """

        reset: Iterable[Reset] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2014",
                "min_occurs": 1,
            },
        )

    @dataclass(slots=True)
    class ModifiedWriteValue:
        value: Optional[ModifiedWriteValueType] = field(
            default=None,
            metadata={
                "required": True,
            },
        )
        modify: Optional[str] = field(
            default=None,
            metadata={
                "type": "Attribute",
            },
        )

    @dataclass(slots=True)
    class ReadAction:
        value: Optional[ReadActionType] = field(
            default=None,
            metadata={
                "required": True,
            },
        )
        modify: Optional[str] = field(
            default=None,
            metadata={
                "type": "Attribute",
            },
        )

    @dataclass(slots=True)
    class Testable:
        """
        :ivar value:
        :ivar test_constraint: Constraint for an automated register test
            routine. 'unconstrained' (default) means may read and write
            all legal values. 'restore' means may read and write legal
            values but the value must be restored to the initially read
            value before accessing another register. 'writeAsRead' has
            limitations on testability where only the value read before
            a write may be written to the field. 'readOnly' has
            limitations on testability where values may only be read
            from the field.
        """

        value: Optional[bool] = field(
            default=None,
            metadata={
                "required": True,
            },
        )
        test_constraint: TestableTestConstraint = field(
            default=TestableTestConstraint.UNCONSTRAINED,
            metadata={
                "name": "testConstraint",
                "type": "Attribute",
            },
        )
