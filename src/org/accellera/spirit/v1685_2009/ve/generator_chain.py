from collections.abc import Iterable
from dataclasses import dataclass, field
from typing import Optional

from org.accellera.spirit.v1685_2009.ve.choices import Choices
from org.accellera.spirit.v1685_2009.ve.description import Description
from org.accellera.spirit.v1685_2009.ve.display_name import DisplayName
from org.accellera.spirit.v1685_2009.ve.generator import Generator
from org.accellera.spirit.v1685_2009.ve.generator_selector_type import (
    GeneratorSelectorType,
)
from org.accellera.spirit.v1685_2009.ve.group_selector import GroupSelector
from org.accellera.spirit.v1685_2009.ve.library_ref_type import LibraryRefType
from org.accellera.spirit.v1685_2009.ve.vendor_extensions import (
    VendorExtensions,
)

__NAMESPACE__ = "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1685-2009"


@dataclass(slots=True)
class GeneratorChain:
    """
    :ivar vendor: Name of the vendor who supplies this file.
    :ivar library: Name of the logical library this element belongs to.
    :ivar name: The name of the object.
    :ivar version: Indicates the version of the named element.
    :ivar generator_chain_selector: Select other generator chain files
        for inclusion into this chain. The boolean attribute "unique"
        (default false) specifies that only a single generator is valid
        in this context. If more that one generator is selected based on
        the selection criteria, DE will prompt the user to resolve to a
        single generator.
    :ivar component_generator_selector: Selects generators declared in
        components of the current design for inclusion into this
        generator chain.
    :ivar generator:
    :ivar chain_group: Identifies this generator chain as belonging to
        the named group. This is used by other generator chains to
        select this chain for programmatic inclusion.
    :ivar display_name:
    :ivar description:
    :ivar choices:
    :ivar vendor_extensions:
    :ivar hidden: If this attribute is true then the generator should
        not be presented to the user, it may be part of a chain and has
        no useful meaning when invoked standalone.
    """

    class Meta:
        name = "generatorChain"
        namespace = (
            "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1685-2009"
        )

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
    generator_chain_selector: Iterable[
        "GeneratorChain.GeneratorChainSelector"
    ] = field(
        default_factory=list,
        metadata={
            "name": "generatorChainSelector",
            "type": "Element",
        },
    )
    component_generator_selector: Iterable[GeneratorSelectorType] = field(
        default_factory=list,
        metadata={
            "name": "componentGeneratorSelector",
            "type": "Element",
        },
    )
    generator: Iterable[Generator] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    chain_group: Iterable[str] = field(
        default_factory=list,
        metadata={
            "name": "chainGroup",
            "type": "Element",
        },
    )
    display_name: Optional[DisplayName] = field(
        default=None,
        metadata={
            "name": "displayName",
            "type": "Element",
        },
    )
    description: Optional[Description] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    choices: Optional[Choices] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    vendor_extensions: Optional[VendorExtensions] = field(
        default=None,
        metadata={
            "name": "vendorExtensions",
            "type": "Element",
        },
    )
    hidden: bool = field(
        default=False,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1685-2009",
        },
    )

    @dataclass(slots=True)
    class GeneratorChainSelector:
        """
        :ivar group_selector:
        :ivar generator_chain_ref: Select another generator chain using
            the unique identifier of this generator chain.
        :ivar unique: Specifies that only a single generator is valid in
            this context. If more that one generator is selcted based on
            the selection criteria, DE will prompt the user to resolve
            to a single generator.
        """

        group_selector: Optional[GroupSelector] = field(
            default=None,
            metadata={
                "name": "groupSelector",
                "type": "Element",
            },
        )
        generator_chain_ref: Optional[LibraryRefType] = field(
            default=None,
            metadata={
                "name": "generatorChainRef",
                "type": "Element",
            },
        )
        unique: bool = field(
            default=False,
            metadata={
                "type": "Attribute",
                "namespace": "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1685-2009",
            },
        )
