from collections.abc import Iterable
from dataclasses import dataclass, field
from typing import Optional

from org.accellera.spirit.v1_0.parameter import Parameter
from org.accellera.spirit.v1_0.resolved_library_ref_type import (
    ResolvedLibraryRefType,
)

__NAMESPACE__ = "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.0"


@dataclass(slots=True)
class LooseGeneratorInvocation:
    """
    Specifies the information required to invoke a loosely coupled generator.

    :ivar design_file: Path to description of top level design
    :ivar bus_definition_files: The list of bus definition files
        currently in use within the design
    :ivar component_definition_files: The list of component definition
        files currently needed to define all the components within the
        design.
    :ivar parameters: List of values of configurable settings for this
        generator invocation
    :ivar selected_instances: The list of instances to be worked upon by
        the generator, no instances selected indicates whole design
    :ivar phase_number: The non-negative floating point phase number
        associated with this generator invocation
    :ivar group_name: The generator group name associated with this
        generator invocation
    """

    class Meta:
        name = "looseGeneratorInvocation"
        namespace = "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.0"

    design_file: Optional[object] = field(
        default=None,
        metadata={
            "name": "designFile",
            "type": "Element",
        },
    )
    bus_definition_files: Optional[
        "LooseGeneratorInvocation.BusDefinitionFiles"
    ] = field(
        default=None,
        metadata={
            "name": "busDefinitionFiles",
            "type": "Element",
        },
    )
    component_definition_files: Optional[
        "LooseGeneratorInvocation.ComponentDefinitionFiles"
    ] = field(
        default=None,
        metadata={
            "name": "componentDefinitionFiles",
            "type": "Element",
        },
    )
    parameters: Optional["LooseGeneratorInvocation.Parameters"] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    selected_instances: Optional[
        "LooseGeneratorInvocation.SelectedInstances"
    ] = field(
        default=None,
        metadata={
            "name": "selectedInstances",
            "type": "Element",
        },
    )
    phase_number: Optional[float] = field(
        default=None,
        metadata={
            "name": "phaseNumber",
            "type": "Element",
            "required": True,
        },
    )
    group_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "groupName",
            "type": "Element",
            "required": True,
        },
    )

    @dataclass(slots=True)
    class BusDefinitionFiles:
        """
        :ivar bus_definition_file: Path to a bus definition file used
            within design. Attributes VLNV used to indicate which bus
            definition this file represents.
        """

        bus_definition_file: Iterable[ResolvedLibraryRefType] = field(
            default_factory=list,
            metadata={
                "name": "busDefinitionFile",
                "type": "Element",
                "min_occurs": 1,
            },
        )

    @dataclass(slots=True)
    class ComponentDefinitionFiles:
        """
        :ivar component_definition_file: Path to component definition
            file. This component definition is the component definition
            as it appears in the DE; i.e. after having been transformed
            by any PMD info, and including any instance specific
            settings such as parameter values. The instanceRef attribute
            is the name of the instance that this file describes.
        """

        component_definition_file: Iterable[
            "LooseGeneratorInvocation.ComponentDefinitionFiles.ComponentDefinitionFile"
        ] = field(
            default_factory=list,
            metadata={
                "name": "componentDefinitionFile",
                "type": "Element",
                "min_occurs": 1,
            },
        )

        @dataclass(slots=True)
        class ComponentDefinitionFile:
            """
            :ivar instance_ref: Reference handle for this component
                definition
            :ivar content:
            """

            instance_ref: Optional[str] = field(
                default=None,
                metadata={
                    "name": "instanceRef",
                    "type": "Attribute",
                    "namespace": "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.0",
                    "required": True,
                },
            )
            content: Iterable[object] = field(
                default_factory=list,
                metadata={
                    "type": "Wildcard",
                    "namespace": "##any",
                    "mixed": True,
                },
            )

    @dataclass(slots=True)
    class Parameters:
        parameter: Iterable[Parameter] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "min_occurs": 1,
            },
        )

    @dataclass(slots=True)
    class SelectedInstances:
        """
        :ivar selected_instance: Instance name of selected instance that
            the generator is expected to work upon. This may be a
            hierarchical instance name.
        """

        selected_instance: Iterable[str] = field(
            default_factory=list,
            metadata={
                "name": "selectedInstance",
                "type": "Element",
                "min_occurs": 1,
            },
        )
