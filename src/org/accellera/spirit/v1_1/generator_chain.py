from collections.abc import Iterable
from dataclasses import dataclass, field
from typing import Optional

from org.accellera.spirit.v1_1.generator import Generator
from org.accellera.spirit.v1_1.generator_selector_type import (
    GeneratorSelectorType,
)
from org.accellera.spirit.v1_1.group_selector import GroupSelector
from org.accellera.spirit.v1_1.library_ref_type import LibraryRefType
from org.accellera.spirit.v1_1.parameter import Parameter

__NAMESPACE__ = "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.1"


@dataclass(slots=True)
class GeneratorChain:
    """
    :ivar vendor: Name of the vendor who supplies this file.
    :ivar library: Name of the logical library this component belongs
        to.  Note that a physical library may contain components from
        multiple logical libraries.  Logical libraries are displayes in
        component browser.
    :ivar name: The name of the object.  Must match the root name of the
        XML file and the directory name it or its version directory
        belongs to.
    :ivar version:
    :ivar file_generator_selector: Select other generator chain files
        for inclusion into this chain. The boolean attribute "unique"
        (default false) specifies that only a single generator is valid
        in this context. If more that one generator is selcted based on
        the selection criteria, DE will prompt the user to resolve to a
        single generator.
    :ivar component_generator_selector: Selects generators declared in
        component description files of the current design for inclusion
        into this generator chain.
    :ivar generator:
    :ivar chain_group: Identifies this generator chain as belonging to
        the named group. This is used by other generator chains to
        select this chain for programmatic inclusion.
    :ivar parameter:
    """

    class Meta:
        name = "generatorChain"
        namespace = "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.1"

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
    file_generator_selector: Iterable[
        "GeneratorChain.FileGeneratorSelector"
    ] = field(
        default_factory=list,
        metadata={
            "name": "fileGeneratorSelector",
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
    parameter: Iterable[Parameter] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )

    @dataclass(slots=True)
    class FileGeneratorSelector:
        """
        :ivar group_selector:
        :ivar file_name: Select another generator chain using the unique
            identifier of this generator chain.
        :ivar unique:
        """

        group_selector: Optional[GroupSelector] = field(
            default=None,
            metadata={
                "name": "groupSelector",
                "type": "Element",
            },
        )
        file_name: Optional[LibraryRefType] = field(
            default=None,
            metadata={
                "name": "fileName",
                "type": "Element",
            },
        )
        unique: bool = field(
            default=True,
            metadata={
                "type": "Attribute",
                "namespace": "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.1",
            },
        )
