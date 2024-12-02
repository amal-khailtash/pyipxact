from collections.abc import Iterable
from dataclasses import dataclass, field
from typing import Optional

from org.accellera.spirit.v1_2.path_element_type import PathElementType

__NAMESPACE__ = "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.2"


@dataclass(slots=True)
class PathSpecifier:
    """
    Defines one or more logical paths within a component.

    :ivar from_value: Defines a valid path starting point. This can be a
        clock, an input port, a sequential cell, or a clock or data out
        pin of a sequential cell. These do not have to be objects that
        are directly represented in the SPIRIT data model. Use the
        pathElement attribute to indicate the type of object referred to
        it if might be ambiguous.
    :ivar to: Defines a valid path ending point. This can be a clock, an
        output port, a sequential cell, or a clock or data in pin of a
        sequential cell. These do not have to be objects that are
        directly represented in the SPIRIT data model. Use the
        pathElement attribute to indicate the type of object referred to
        if it might be ambiguous. Defines a valid path ending point.
        This can be a clock, an output port, a sequential cell, or a
        clock or data in pin of a sequential cell. These do not have to
        be objects that are directly represented in the SPIRIT data
        model. Use the pathElement attribute to indicate the type of
        object referred to if it might be ambiguous.
    :ivar through: Defines a set of pins, ports, cells, or nets through
        which the desired path(s) must pass. These do not have to be
        objects that are directly represented in the SPIRIT data model.
        Use the pathElement attribute to indicate the type of object
        referred to if it might be ambiguous. Defines a set of pins,
        ports, cells, or nets through which the desired path(s) must
        pass. These do not have to be objects that are directly
        represented in the SPIRIT data model. Use the pathElement
        attribute to indicate the type of object referred to if it might
        be ambiguous.
    """

    class Meta:
        name = "pathSpecifier"
        namespace = "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.2"

    from_value: Iterable["PathSpecifier.From"] = field(
        default_factory=list,
        metadata={
            "name": "from",
            "type": "Element",
        },
    )
    to: Iterable["PathSpecifier.To"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    through: Iterable["PathSpecifier.Through"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )

    @dataclass(slots=True)
    class From:
        value: str = field(
            default="",
            metadata={
                "required": True,
            },
        )
        path_element: Optional[PathElementType] = field(
            default=None,
            metadata={
                "name": "pathElement",
                "type": "Attribute",
                "namespace": "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.2",
            },
        )

    @dataclass(slots=True)
    class To:
        value: str = field(
            default="",
            metadata={
                "required": True,
            },
        )
        path_element: Optional[PathElementType] = field(
            default=None,
            metadata={
                "name": "pathElement",
                "type": "Attribute",
                "namespace": "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.2",
            },
        )

    @dataclass(slots=True)
    class Through:
        value: str = field(
            default="",
            metadata={
                "required": True,
            },
        )
        path_element: Optional[PathElementType] = field(
            default=None,
            metadata={
                "name": "pathElement",
                "type": "Attribute",
                "namespace": "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.2",
            },
        )
