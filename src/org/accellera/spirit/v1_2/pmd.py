from collections.abc import Iterable
from dataclasses import dataclass, field
from typing import Optional

from org.accellera.spirit.v1_2.choices import Choices
from org.accellera.spirit.v1_2.library_ref_type import LibraryRefType
from org.accellera.spirit.v1_2.name_value_pair_type import NameValuePairType

__NAMESPACE__ = "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.2"


@dataclass(slots=True)
class Pmd:
    """The root element of the platform meta-data definition file.

    This file defines the Platform meta-data to be applied to specific
    IP

    :ivar vendor: Name of the vendor who supplies this file.
    :ivar library: Name of the logical library this element belongs to.
    :ivar name: The name of the object.
    :ivar version:
    :ivar applies_to: Defines the components that this pmd applies to.
        When the user tries to add any of those components, this pmd
        will be applied.
    :ivar depends_on: Defines the components that  must exist in the
        current design for this pmd to apply. The pmd will only apply if
        an instance of each components declared in this list exists in
        the design. If the list is empty then this pmd file will apply
        unconditionally.
    :ivar transformer: The transformer element contains references to
        the actual code that will make the transformation. If there are
        multiple elements, they will be applied in sequence. i.e., the
        affected component document will pass through a pipeline of
        transformers with each child element representing a step in a
        pipeline.
    :ivar choices:
    """

    class Meta:
        name = "pmd"
        namespace = "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.2"

    vendor: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    library: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    version: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    applies_to: Optional["Pmd.AppliesTo"] = field(
        default=None,
        metadata={
            "name": "appliesTo",
            "type": "Element",
            "required": True,
        },
    )
    depends_on: Optional["Pmd.DependsOn"] = field(
        default=None,
        metadata={
            "name": "dependsOn",
            "type": "Element",
            "required": True,
        },
    )
    transformer: Optional["Pmd.Transformer"] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    choices: Optional[Choices] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )

    @dataclass(slots=True)
    class AppliesTo:
        """
        :ivar component_ref: A vendor-library-name-version identifier
            used to refer to components.
        """

        component_ref: Iterable["Pmd.AppliesTo.ComponentRef"] = field(
            default_factory=list,
            metadata={
                "name": "componentRef",
                "type": "Element",
                "min_occurs": 1,
            },
        )

        @dataclass(slots=True)
        class ComponentRef(LibraryRefType):
            """
            :ivar display_label: A display label to override the
                original component's display label if this PMD will
                apply.
            """

            display_label: Optional[str] = field(
                default=None,
                metadata={
                    "name": "displayLabel",
                    "type": "Element",
                    "white_space": "collapse",
                },
            )

    @dataclass(slots=True)
    class DependsOn:
        """
        :ivar component_ref: A vendor-library-name-version identifier
            used to refer to components.
        """

        component_ref: Iterable[LibraryRefType] = field(
            default_factory=list,
            metadata={
                "name": "componentRef",
                "type": "Element",
            },
        )

    @dataclass(slots=True)
    class Transformer:
        """
        :ivar xslt: An XSLT transformer that will transform the document
            based on rules defined in the xsl file mentioned here.
        """

        xslt: Iterable["Pmd.Transformer.Xslt"] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "min_occurs": 1,
            },
        )

        @dataclass(slots=True)
        class Xslt:
            """
            :ivar style_sheet: The relative path to the xsl stylesheet
                to be used for transformation.
            :ivar parameter: Parameters to be passed to the xslt
                stylesheet at run time.
            """

            style_sheet: Optional[str] = field(
                default=None,
                metadata={
                    "name": "styleSheet",
                    "type": "Element",
                    "required": True,
                },
            )
            parameter: Iterable[NameValuePairType] = field(
                default_factory=list,
                metadata={
                    "type": "Element",
                },
            )
