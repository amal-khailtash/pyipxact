from collections.abc import Iterable
from dataclasses import dataclass, field
from typing import Optional

from org.accellera.spirit.v1_5.configurable_element_values import (
    ConfigurableElementValues,
)
from org.accellera.spirit.v1_5.description import Description
from org.accellera.spirit.v1_5.display_name import DisplayName
from org.accellera.spirit.v1_5.instance_name import InstanceName
from org.accellera.spirit.v1_5.library_ref_type import LibraryRefType
from org.accellera.spirit.v1_5.vendor_extensions import VendorExtensions

__NAMESPACE__ = "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.5"


@dataclass(slots=True)
class DesignConfiguration:
    """Top level element for describing the current configuration of a design.

    Does not describe instance parameterization

    :ivar vendor: Name of the vendor who supplies this file.
    :ivar library: Name of the logical library this element belongs to.
    :ivar name: The name of the object.
    :ivar version: Indicates the version of the named element.
    :ivar design_ref: The design to which this configuration applies
    :ivar generator_chain_configuration: Contains the configurable
        information associated with a generatorChain and its generators.
        Note that configurable information for generators associated
        with components is stored in the design file.
    :ivar interconnection_configuration: Contains the information about
        the abstractors required to cross between two interfaces at with
        different abstractionDefs.
    :ivar view_configuration: Contains the active view for each instance
        in the design
    :ivar description:
    :ivar vendor_extensions:
    """

    class Meta:
        name = "designConfiguration"
        namespace = "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.5"

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
    generator_chain_configuration: Iterable[
        "DesignConfiguration.GeneratorChainConfiguration"
    ] = field(
        default_factory=list,
        metadata={
            "name": "generatorChainConfiguration",
            "type": "Element",
        },
    )
    interconnection_configuration: Iterable[
        "DesignConfiguration.InterconnectionConfiguration"
    ] = field(
        default_factory=list,
        metadata={
            "name": "interconnectionConfiguration",
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
    description: Optional[Description] = field(
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

    @dataclass(slots=True)
    class GeneratorChainConfiguration:
        """
        :ivar generator_chain_ref: References a generatorChain.
        :ivar configurable_element_values:
        """

        generator_chain_ref: Optional[LibraryRefType] = field(
            default=None,
            metadata={
                "name": "generatorChainRef",
                "type": "Element",
                "required": True,
            },
        )
        configurable_element_values: Optional[ConfigurableElementValues] = (
            field(
                default=None,
                metadata={
                    "name": "configurableElementValues",
                    "type": "Element",
                },
            )
        )

    @dataclass(slots=True)
    class InterconnectionConfiguration:
        """
        :ivar interconnection_ref: Reference to the interconnection
            name, monitor interconnection name or possibly a
            hierConnection interfaceName in a design file.
        :ivar abstractors: List of abstractors for this interconnection
        """

        interconnection_ref: Optional[str] = field(
            default=None,
            metadata={
                "name": "interconnectionRef",
                "type": "Element",
                "required": True,
            },
        )
        abstractors: Optional[
            "DesignConfiguration.InterconnectionConfiguration.Abstractors"
        ] = field(
            default=None,
            metadata={
                "type": "Element",
                "required": True,
            },
        )

        @dataclass(slots=True)
        class Abstractors:
            """
            :ivar abstractor: Element to hold a the abstractor
                reference, the configuration and viewName. If multiple
                elements are present then the order is the order in
                which the abstractors should be chained together.
            """

            abstractor: Iterable[
                "DesignConfiguration.InterconnectionConfiguration.Abstractors.Abstractor"
            ] = field(
                default_factory=list,
                metadata={
                    "type": "Element",
                    "min_occurs": 1,
                },
            )

            @dataclass(slots=True)
            class Abstractor:
                """
                :ivar instance_name: Instance name for the abstractor
                :ivar display_name:
                :ivar description:
                :ivar abstractor_ref: Abstractor reference
                :ivar configurable_element_values:
                :ivar view_name: The name of the active view for this
                    abstractor instance.
                """

                instance_name: Optional[str] = field(
                    default=None,
                    metadata={
                        "name": "instanceName",
                        "type": "Element",
                        "required": True,
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
                abstractor_ref: Optional[LibraryRefType] = field(
                    default=None,
                    metadata={
                        "name": "abstractorRef",
                        "type": "Element",
                        "required": True,
                    },
                )
                configurable_element_values: Optional[
                    ConfigurableElementValues
                ] = field(
                    default=None,
                    metadata={
                        "name": "configurableElementValues",
                        "type": "Element",
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
