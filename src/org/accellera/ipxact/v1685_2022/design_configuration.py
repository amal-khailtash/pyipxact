from collections.abc import Iterable
from dataclasses import dataclass, field
from typing import Optional

from org.accellera.ipxact.v1685_2022.assertions import Assertions
from org.accellera.ipxact.v1685_2022.choices import Choices
from org.accellera.ipxact.v1685_2022.configurable_element_values import (
    ConfigurableElementValues,
)
from org.accellera.ipxact.v1685_2022.configurable_library_ref_type import (
    ConfigurableLibraryRefType,
)
from org.accellera.ipxact.v1685_2022.description import Description
from org.accellera.ipxact.v1685_2022.display_name import DisplayName
from org.accellera.ipxact.v1685_2022.instance_name import InstanceName
from org.accellera.ipxact.v1685_2022.library_ref_type import LibraryRefType
from org.accellera.ipxact.v1685_2022.parameters import Parameters
from org.accellera.ipxact.v1685_2022.short_description import ShortDescription
from org.accellera.ipxact.v1685_2022.vendor_extensions import VendorExtensions

__NAMESPACE__ = "http://www.accellera.org/XMLSchema/IPXACT/1685-2022"


@dataclass(slots=True)
class DesignConfiguration:
    """Top level element for describing the current configuration of a design.

    Does not describe instance parameterization

    :ivar vendor: Name of the vendor who supplies this file.
    :ivar library: Name of the logical library this element belongs to.
    :ivar name: The name of the object.
    :ivar version: Indicates the version of the named element.
    :ivar display_name: Name for display purposes. Typically a few words
        providing a more detailed and/or user-friendly name than the
        vlnv.
    :ivar short_description:
    :ivar description:
    :ivar design_ref: The design to which this configuration applies
    :ivar generator_chain_configuration: Contains the configurable
        information associated with a generatorChain and its generators.
        Note that configurable information for generators associated
        with components is stored in the design file.
    :ivar interconnection_configuration: Contains the information about
        the abstractors required to cross between two interfaces at with
        different abstractionDefs.
    :ivar view_configuration: Contains the active views for each
        instance in the design
    :ivar choices:
    :ivar parameters:
    :ivar assertions:
    :ivar vendor_extensions:
    :ivar id:
    """

    class Meta:
        name = "designConfiguration"
        namespace = "http://www.accellera.org/XMLSchema/IPXACT/1685-2022"

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
    display_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "displayName",
            "type": "Element",
        },
    )
    short_description: Optional[ShortDescription] = field(
        default=None,
        metadata={
            "name": "shortDescription",
            "type": "Element",
        },
    )
    description: Optional[Description] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    design_ref: Optional[LibraryRefType] = field(
        default=None,
        metadata={
            "name": "designRef",
            "type": "Element",
        },
    )
    generator_chain_configuration: Iterable[ConfigurableLibraryRefType] = (
        field(
            default_factory=list,
            metadata={
                "name": "generatorChainConfiguration",
                "type": "Element",
            },
        )
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
    choices: Optional[Choices] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    parameters: Optional[Parameters] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    assertions: Optional[Assertions] = field(
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
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )

    @dataclass(slots=True)
    class InterconnectionConfiguration:
        """
        :ivar interconnection_ref: Reference to the interconnection
            name, monitor interconnection name or possibly a
            hierConnection interfaceName in a design file.
        :ivar abstractor_instances: List of abstractor-instances for
            this interconnection. Multiple abstractor-instances elements
            may be present for a 1-to-many (broadcast) interconnection.
            In that case, the optional interfaceRef elements must
            reference non-overlapping interfaces from the 'many' side of
            the interconnection.
        :ivar vendor_extensions:
        :ivar id:
        """

        interconnection_ref: Optional[str] = field(
            default=None,
            metadata={
                "name": "interconnectionRef",
                "type": "Element",
                "required": True,
            },
        )
        abstractor_instances: Iterable[
            "DesignConfiguration.InterconnectionConfiguration.AbstractorInstances"
        ] = field(
            default_factory=list,
            metadata={
                "name": "abstractorInstances",
                "type": "Element",
                "min_occurs": 1,
            },
        )
        vendor_extensions: Optional[VendorExtensions] = field(
            default=None,
            metadata={
                "name": "vendorExtensions",
                "type": "Element",
            },
        )
        id: Optional[str] = field(
            default=None,
            metadata={
                "type": "Attribute",
                "namespace": "http://www.w3.org/XML/1998/namespace",
            },
        )

        @dataclass(slots=True)
        class AbstractorInstances:
            """
            :ivar interface_ref: Defines the broadcast endpoint to which
                this chain of abstractors applies.
            :ivar abstractor_instance: Element to hold a the abstractor
                reference, the configuration and viewName. If multiple
                elements are present then the order is the order in
                which the abstractors should be chained together.
            :ivar vendor_extensions:
            :ivar id:
            """

            interface_ref: Iterable[
                "DesignConfiguration.InterconnectionConfiguration.AbstractorInstances.InterfaceRef"
            ] = field(
                default_factory=list,
                metadata={
                    "name": "interfaceRef",
                    "type": "Element",
                },
            )
            abstractor_instance: Iterable[
                "DesignConfiguration.InterconnectionConfiguration.AbstractorInstances.AbstractorInstance"
            ] = field(
                default_factory=list,
                metadata={
                    "name": "abstractorInstance",
                    "type": "Element",
                    "min_occurs": 1,
                },
            )
            vendor_extensions: Optional[VendorExtensions] = field(
                default=None,
                metadata={
                    "name": "vendorExtensions",
                    "type": "Element",
                },
            )
            id: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Attribute",
                    "namespace": "http://www.w3.org/XML/1998/namespace",
                },
            )

            @dataclass(slots=True)
            class InterfaceRef:
                """
                :ivar vendor_extensions:
                :ivar component_ref: Reference to a component instance
                    nane.
                :ivar bus_ref: Reference to a component bus interface
                    name.
                :ivar id:
                """

                vendor_extensions: Optional[VendorExtensions] = field(
                    default=None,
                    metadata={
                        "name": "vendorExtensions",
                        "type": "Element",
                    },
                )
                component_ref: Optional[str] = field(
                    default=None,
                    metadata={
                        "name": "componentRef",
                        "type": "Attribute",
                        "required": True,
                    },
                )
                bus_ref: Optional[str] = field(
                    default=None,
                    metadata={
                        "name": "busRef",
                        "type": "Attribute",
                        "required": True,
                    },
                )
                id: Optional[str] = field(
                    default=None,
                    metadata={
                        "type": "Attribute",
                        "namespace": "http://www.w3.org/XML/1998/namespace",
                    },
                )

            @dataclass(slots=True)
            class AbstractorInstance:
                """
                :ivar instance_name: Instance name for the abstractor
                :ivar display_name:
                :ivar short_description:
                :ivar description:
                :ivar abstractor_ref: Abstractor reference
                :ivar view_name: The name of the active view for this
                    abstractor instance.
                :ivar id:
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
                short_description: Optional[ShortDescription] = field(
                    default=None,
                    metadata={
                        "name": "shortDescription",
                        "type": "Element",
                    },
                )
                description: Optional[Description] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                    },
                )
                abstractor_ref: Optional[ConfigurableLibraryRefType] = field(
                    default=None,
                    metadata={
                        "name": "abstractorRef",
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
                id: Optional[str] = field(
                    default=None,
                    metadata={
                        "type": "Attribute",
                        "namespace": "http://www.w3.org/XML/1998/namespace",
                    },
                )

    @dataclass(slots=True)
    class ViewConfiguration:
        """
        :ivar instance_name:
        :ivar view: The selected view for the instance.
        :ivar vendor_extensions:
        :ivar id:
        """

        instance_name: Optional[InstanceName] = field(
            default=None,
            metadata={
                "name": "instanceName",
                "type": "Element",
                "required": True,
            },
        )
        view: Optional["DesignConfiguration.ViewConfiguration.View"] = field(
            default=None,
            metadata={
                "type": "Element",
                "required": True,
            },
        )
        vendor_extensions: Optional[VendorExtensions] = field(
            default=None,
            metadata={
                "name": "vendorExtensions",
                "type": "Element",
            },
        )
        id: Optional[str] = field(
            default=None,
            metadata={
                "type": "Attribute",
                "namespace": "http://www.w3.org/XML/1998/namespace",
            },
        )

        @dataclass(slots=True)
        class View:
            """
            :ivar configurable_element_values: Parameter values to set
                in the selected configuredView.
            :ivar view_ref:
            """

            configurable_element_values: Optional[
                ConfigurableElementValues
            ] = field(
                default=None,
                metadata={
                    "name": "configurableElementValues",
                    "type": "Element",
                },
            )
            view_ref: Optional[str] = field(
                default=None,
                metadata={
                    "name": "viewRef",
                    "type": "Attribute",
                    "required": True,
                },
            )
