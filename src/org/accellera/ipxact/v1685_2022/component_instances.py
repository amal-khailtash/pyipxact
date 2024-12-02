from collections.abc import Iterable
from dataclasses import dataclass, field

from org.accellera.ipxact.v1685_2022.component_instance import (
    ComponentInstance,
)

__NAMESPACE__ = "http://www.accellera.org/XMLSchema/IPXACT/1685-2022"


@dataclass(slots=True)
class ComponentInstances:
    """
    Sub instances of internal components.
    """

    class Meta:
        name = "componentInstances"
        namespace = "http://www.accellera.org/XMLSchema/IPXACT/1685-2022"

    component_instance: Iterable[ComponentInstance] = field(
        default_factory=list,
        metadata={
            "name": "componentInstance",
            "type": "Element",
            "min_occurs": 1,
        },
    )
