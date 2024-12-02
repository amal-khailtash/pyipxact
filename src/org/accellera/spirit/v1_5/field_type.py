from collections.abc import Iterable, Mapping
from dataclasses import dataclass, field
from typing import Optional

from org.accellera.spirit.v1_5.access import Access
from org.accellera.spirit.v1_5.description import Description
from org.accellera.spirit.v1_5.display_name import DisplayName
from org.accellera.spirit.v1_5.enumerated_values import EnumeratedValues
from org.accellera.spirit.v1_5.field_type_modified_write_value import (
    FieldTypeModifiedWriteValue,
)
from org.accellera.spirit.v1_5.field_type_read_action import (
    FieldTypeReadAction,
)
from org.accellera.spirit.v1_5.format_type import FormatType
from org.accellera.spirit.v1_5.parameters import Parameters
from org.accellera.spirit.v1_5.range_type_type import RangeTypeType
from org.accellera.spirit.v1_5.resolve_type import ResolveType
from org.accellera.spirit.v1_5.testable_test_constraint import (
    TestableTestConstraint,
)
from org.accellera.spirit.v1_5.vendor_extensions import VendorExtensions
from org.accellera.spirit.v1_5.volatile import Volatile
from org.accellera.spirit.v1_5.write_value_constraint_type import (
    WriteValueConstraintType,
)

__NAMESPACE__ = "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.5"


@dataclass(slots=True)
class FieldType:
    """
    A field within a register.

    :ivar name: Unique name
    :ivar display_name:
    :ivar description:
    :ivar bit_offset: Offset of this field's bit 0 from bit 0 of the
        register.
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
    :ivar parameters:
    :ivar vendor_extensions:
    :ivar id:
    """

    class Meta:
        name = "fieldType"

    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.5",
            "required": True,
        },
    )
    display_name: Optional[DisplayName] = field(
        default=None,
        metadata={
            "name": "displayName",
            "type": "Element",
            "namespace": "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.5",
        },
    )
    description: Optional[Description] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.5",
        },
    )
    bit_offset: Optional[int] = field(
        default=None,
        metadata={
            "name": "bitOffset",
            "type": "Element",
            "namespace": "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.5",
            "required": True,
        },
    )
    type_identifier: Optional[str] = field(
        default=None,
        metadata={
            "name": "typeIdentifier",
            "type": "Element",
            "namespace": "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.5",
        },
    )
    bit_width: Optional["FieldType.BitWidth"] = field(
        default=None,
        metadata={
            "name": "bitWidth",
            "type": "Element",
            "namespace": "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.5",
            "required": True,
        },
    )
    volatile: Optional[Volatile] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.5",
        },
    )
    access: Optional[Access] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.5",
        },
    )
    enumerated_values: Optional[EnumeratedValues] = field(
        default=None,
        metadata={
            "name": "enumeratedValues",
            "type": "Element",
            "namespace": "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.5",
        },
    )
    modified_write_value: Optional[FieldTypeModifiedWriteValue] = field(
        default=None,
        metadata={
            "name": "modifiedWriteValue",
            "type": "Element",
            "namespace": "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.5",
        },
    )
    write_value_constraint: Optional[WriteValueConstraintType] = field(
        default=None,
        metadata={
            "name": "writeValueConstraint",
            "type": "Element",
            "namespace": "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.5",
        },
    )
    read_action: Optional[FieldTypeReadAction] = field(
        default=None,
        metadata={
            "name": "readAction",
            "type": "Element",
            "namespace": "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.5",
        },
    )
    testable: Optional["FieldType.Testable"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.5",
        },
    )
    parameters: Optional[Parameters] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.5",
        },
    )
    vendor_extensions: Optional[VendorExtensions] = field(
        default=None,
        metadata={
            "name": "vendorExtensions",
            "type": "Element",
            "namespace": "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.5",
        },
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.5",
        },
    )

    @dataclass(slots=True)
    class BitWidth:
        value: Optional[int] = field(
            default=None,
            metadata={
                "required": True,
            },
        )
        format: FormatType = field(
            default=FormatType.LONG,
            metadata={
                "type": "Attribute",
                "namespace": "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.5",
            },
        )
        resolve: ResolveType = field(
            default=ResolveType.IMMEDIATE,
            metadata={
                "type": "Attribute",
                "namespace": "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.5",
            },
        )
        id: Optional[str] = field(
            default=None,
            metadata={
                "type": "Attribute",
                "namespace": "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.5",
            },
        )
        dependency: Optional[str] = field(
            default=None,
            metadata={
                "type": "Attribute",
                "namespace": "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.5",
            },
        )
        any_attributes: Mapping[str, str] = field(
            default_factory=dict,
            metadata={
                "type": "Attributes",
                "namespace": "##any",
            },
        )
        choice_ref: Optional[str] = field(
            default=None,
            metadata={
                "name": "choiceRef",
                "type": "Attribute",
                "namespace": "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.5",
            },
        )
        order: Optional[float] = field(
            default=None,
            metadata={
                "type": "Attribute",
                "namespace": "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.5",
            },
        )
        config_groups: Iterable[str] = field(
            default_factory=list,
            metadata={
                "name": "configGroups",
                "type": "Attribute",
                "namespace": "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.5",
                "tokens": True,
            },
        )
        bit_string_length: Optional[int] = field(
            default=None,
            metadata={
                "name": "bitStringLength",
                "type": "Attribute",
                "namespace": "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.5",
            },
        )
        minimum: Optional[str] = field(
            default=None,
            metadata={
                "type": "Attribute",
                "namespace": "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.5",
            },
        )
        maximum: Optional[str] = field(
            default=None,
            metadata={
                "type": "Attribute",
                "namespace": "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.5",
            },
        )
        range_type: RangeTypeType = field(
            default=RangeTypeType.FLOAT,
            metadata={
                "name": "rangeType",
                "type": "Attribute",
                "namespace": "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.5",
            },
        )
        prompt: Optional[str] = field(
            default=None,
            metadata={
                "type": "Attribute",
                "namespace": "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.5",
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
                "namespace": "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.5",
            },
        )
