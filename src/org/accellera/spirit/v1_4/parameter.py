from dataclasses import dataclass

from org.accellera.spirit.v1_4.name_value_pair_type import NameValuePairType

__NAMESPACE__ = "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.4"


@dataclass(slots=True)
class Parameter(NameValuePairType):
    """A name value pair.

    The name is specified by the name element.  The value is in the text
    content of the value element.  This value element supports all
    configurability attributes.
    """

    class Meta:
        name = "parameter"
        namespace = "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.4"
