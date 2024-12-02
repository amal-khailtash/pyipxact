from collections.abc import Iterable
from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.2"


@dataclass(slots=True)
class WhiteboxElementRefType:
    """Reference to a whiteboxElement within a view.

    The 'name' attribute must refer to a whiteboxElement defined within
    this component.

    :ivar whitebox_path: The whiteboxPath elements (as a set) define the
        name(s) needed to define the entire white box element in this
        view.
    :ivar name:
    """

    class Meta:
        name = "whiteboxElementRefType"

    whitebox_path: Iterable["WhiteboxElementRefType.WhiteboxPath"] = field(
        default_factory=list,
        metadata={
            "name": "whiteboxPath",
            "type": "Element",
            "namespace": "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.2",
            "min_occurs": 1,
        },
    )
    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.2",
            "required": True,
        },
    )

    @dataclass(slots=True)
    class WhiteboxPath:
        """
        :ivar path_name: The view specific name for a portion of the
            white box element.
        :ivar left: Indicates the left bound value for the associated
            path name.
        :ivar right: Indicates the right bound values for the associated
            path name.
        """

        path_name: Optional[str] = field(
            default=None,
            metadata={
                "name": "pathName",
                "type": "Element",
                "namespace": "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.2",
                "required": True,
            },
        )
        left: Optional[int] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.2",
            },
        )
        right: Optional[int] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.2",
            },
        )
