from dataclasses import dataclass

from org.accellera.spirit.v1685_2009.ve.core.name_value_pair_type_2 import (
    NameValuePairType2,
)

__NAMESPACE__ = (
    "http://www.accellera.org/XMLSchema/SPIRIT/1685-2009-VE/CORE-1.0"
)


@dataclass(slots=True)
class PortParameter(NameValuePairType2):
    """A name value pair.

    The name is specified by the name element.  The value is in the text
    content of the value element.  This value element supports all
    configurability attributes.
    """

    class Meta:
        name = "portParameter"
        namespace = (
            "http://www.accellera.org/XMLSchema/SPIRIT/1685-2009-VE/CORE-1.0"
        )
