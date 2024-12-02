from collections.abc import Iterable
from dataclasses import dataclass, field
from typing import Optional

from org.accellera.spirit.v1_0.parameter import Parameter
from org.accellera.spirit.v1_0.phase import Phase
from org.accellera.spirit.v1_0.vendor_extensions import VendorExtensions

__NAMESPACE__ = "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.0"


@dataclass(slots=True)
class GeneratorType:
    """
    Types of generators.

    :ivar name: The name of this generator.
    :ivar phase:
    :ivar parameter:
    :ivar access_type: Identifies the special requirements that this
        generator may place up on the DE.
    :ivar loose_generator_exe: The pathname to the executable file that
        implements the loose generator
    :ivar vendor_extensions:
    """

    class Meta:
        name = "generatorType"

    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.0",
            "required": True,
        },
    )
    phase: Optional[Phase] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.0",
        },
    )
    parameter: Iterable[Parameter] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.0",
        },
    )
    access_type: Optional["GeneratorType.AccessType"] = field(
        default=None,
        metadata={
            "name": "accessType",
            "type": "Element",
            "namespace": "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.0",
        },
    )
    loose_generator_exe: Optional[str] = field(
        default=None,
        metadata={
            "name": "looseGeneratorExe",
            "type": "Element",
            "namespace": "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.0",
            "required": True,
        },
    )
    vendor_extensions: Optional[VendorExtensions] = field(
        default=None,
        metadata={
            "name": "vendorExtensions",
            "type": "Element",
            "namespace": "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.0",
        },
    )

    @dataclass(slots=True)
    class AccessType:
        """
        :ivar read_only: If true then this generator will not make
            changes to the  design.
        :ivar hierarchical: If true then this generator is capable of
            running in a hierarchical manner and so the DE must ensure
            that all lower levels of hierarchy are also made available
        :ivar instance_required: If true then the generator operates on
            designated instances, not the whole design. The DE must
            capture the instances to be operated on.
        :ivar subset_only: If present then this generator only needs a
            subset of the design information.
        """

        read_only: bool = field(
            default=False,
            metadata={
                "name": "readOnly",
                "type": "Element",
                "namespace": "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.0",
                "required": True,
            },
        )
        hierarchical: bool = field(
            default=True,
            metadata={
                "type": "Element",
                "namespace": "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.0",
                "required": True,
            },
        )
        instance_required: bool = field(
            default=False,
            metadata={
                "name": "instanceRequired",
                "type": "Element",
                "namespace": "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.0",
                "required": True,
            },
        )
        subset_only: Optional["GeneratorType.AccessType.SubsetOnly"] = field(
            default=None,
            metadata={
                "name": "subsetOnly",
                "type": "Element",
                "namespace": "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.0",
            },
        )

        @dataclass(slots=True)
        class SubsetOnly:
            """
            :ivar design_file: If true then the generator only needs to
                look at design information.
            :ivar component_defs: If true then the generator only needs
                to look at component related information.
            :ivar bus_defs: If true then the generator only needs to
                look at bus definition information.
            """

            design_file: bool = field(
                default=True,
                metadata={
                    "name": "designFile",
                    "type": "Element",
                    "namespace": "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.0",
                    "required": True,
                },
            )
            component_defs: bool = field(
                default=True,
                metadata={
                    "name": "componentDefs",
                    "type": "Element",
                    "namespace": "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.0",
                    "required": True,
                },
            )
            bus_defs: bool = field(
                default=True,
                metadata={
                    "name": "busDefs",
                    "type": "Element",
                    "namespace": "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.0",
                    "required": True,
                },
            )
