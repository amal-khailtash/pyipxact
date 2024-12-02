from dataclasses import dataclass

from org.accellera.spirit.v1_2.name_value_pair_type import NameValuePairType

__NAMESPACE__ = "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.2"


@dataclass(slots=True)
class Parameter(NameValuePairType):
    """A name value pair.

    The name is specified by the name attribute.  The value is in the
    text content of the element.  This element supports all
    configurability attributes.  It also supports a cross reference
    attribute which allows it to be associated with other elements in
    the document through an XPath expression.
    """

    class Meta:
        name = "parameter"
        namespace = "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.2"
