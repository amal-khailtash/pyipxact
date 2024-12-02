from dataclasses import dataclass, field
from typing import Optional

from org.accellera.spirit.v1685_2009.ve.area_estimation import AreaEstimation
from org.accellera.spirit.v1685_2009.ve.technology_name import TechnologyName

__NAMESPACE__ = "http://www.accellera.org/XMLSchema/SPIRIT/1685-2009-VE"


@dataclass(slots=True)
class View:
    """
    View extension.
    """

    class Meta:
        name = "view"
        namespace = "http://www.accellera.org/XMLSchema/SPIRIT/1685-2009-VE"

    technology_name: Optional[TechnologyName] = field(
        default=None,
        metadata={
            "name": "technologyName",
            "type": "Element",
            "namespace": "http://www.accellera.org/XMLSchema/SPIRIT/1685-2009-VE/PDP-1.0",
        },
    )
    area_estimation: Optional[AreaEstimation] = field(
        default=None,
        metadata={
            "name": "areaEstimation",
            "type": "Element",
            "namespace": "http://www.accellera.org/XMLSchema/SPIRIT/1685-2009-VE/PDP-1.0",
        },
    )
