from collections.abc import Iterable
from dataclasses import dataclass, field
from typing import Optional

from org.accellera.spirit.v1_2.configurable_element import ConfigurableElement
from org.accellera.spirit.v1_2.instance_name import InstanceName
from org.accellera.spirit.v1_2.library_ref_type import LibraryRefType
from org.accellera.spirit.v1_2.vendor_extensions import VendorExtensions

__NAMESPACE__ = "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.2"


@dataclass(slots=True)
class DesignConfiguration:
    """Top level element for describing the current configuration of a design.

    Does not describe instance parameterization

    :ivar vendor: Name of the vendor who supplies this file.
    :ivar library: Name of the logical library this element belongs to.
    :ivar name: The name of the object.
    :ivar version:
    :ivar design_ref: The design to which this configuration applies
    :ivar pmd_configuration: Contains the configurable information
        associated with a particular PMD
    :ivar generator_chain_configuration: Contains the configurable
        information associated with a generatorChain and its generators.
        Note that configurable information for generators associated
        with components is stored in the design file.
    :ivar view_configuration: Contains the active view for each instance
        in the design
    :ivar vendor_extensions:
    """

    class Meta:
        name = "designConfiguration"
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
    design_ref: Optional[LibraryRefType] = field(
        default=None,
        metadata={
            "name": "designRef",
            "type": "Element",
            "required": True,
        },
    )
    pmd_configuration: Iterable["DesignConfiguration.PmdConfiguration"] = (
        field(
            default_factory=list,
            metadata={
                "name": "pmdConfiguration",
                "type": "Element",
            },
        )
    )
    generator_chain_configuration: Iterable[
        "DesignConfiguration.GeneratorChainConfiguration"
    ] = field(
        default_factory=list,
        metadata={
            "name": "generatorChainConfiguration",
            "type": "Element",
        },
    )
    view_configuration: Iterable["DesignConfiguration.ViewConfiguration"] = (
        field(
            default_factory=list,
            metadata={
                "name": "viewConfiguration",
                "type": "Element",
            },
        )
    )
    vendor_extensions: Optional[VendorExtensions] = field(
        default=None,
        metadata={
            "name": "vendorExtensions",
            "type": "Element",
        },
    )

    @dataclass(slots=True)
    class PmdConfiguration:
        """
        :ivar pmd_ref: References a PMD.
        :ivar configurable_element:
        """

        pmd_ref: Optional[LibraryRefType] = field(
            default=None,
            metadata={
                "name": "pmdRef",
                "type": "Element",
                "required": True,
            },
        )
        configurable_element: Iterable[ConfigurableElement] = field(
            default_factory=list,
            metadata={
                "name": "configurableElement",
                "type": "Element",
                "min_occurs": 1,
            },
        )

    @dataclass(slots=True)
    class GeneratorChainConfiguration:
        """
        :ivar generator_chain_ref: References a generatorChain.
        :ivar configurable_element:
        :ivar generators: Stores configurable information for generators
            referenced in the chain
        """

        generator_chain_ref: Optional[LibraryRefType] = field(
            default=None,
            metadata={
                "name": "generatorChainRef",
                "type": "Element",
                "required": True,
            },
        )
        configurable_element: Iterable[ConfigurableElement] = field(
            default_factory=list,
            metadata={
                "name": "configurableElement",
                "type": "Element",
            },
        )
        generators: Iterable[
            "DesignConfiguration.GeneratorChainConfiguration.Generators"
        ] = field(
            default_factory=list,
            metadata={
                "type": "Element",
            },
        )

        @dataclass(slots=True)
        class Generators:
            """
            :ivar generator_name: This identifies the generator in the
                chain.
            :ivar configurable_element:
            """

            generator_name: Optional[str] = field(
                default=None,
                metadata={
                    "name": "generatorName",
                    "type": "Element",
                    "required": True,
                },
            )
            configurable_element: Iterable[ConfigurableElement] = field(
                default_factory=list,
                metadata={
                    "name": "configurableElement",
                    "type": "Element",
                    "min_occurs": 1,
                },
            )

    @dataclass(slots=True)
    class ViewConfiguration:
        """
        :ivar instance_name:
        :ivar view_name: The name of the active view for this instance
        """

        instance_name: Optional[InstanceName] = field(
            default=None,
            metadata={
                "name": "instanceName",
                "type": "Element",
                "required": True,
            },
        )
        view_name: Optional[str] = field(
            default=None,
            metadata={
                "name": "viewName",
                "type": "Element",
                "required": True,
            },
        )
