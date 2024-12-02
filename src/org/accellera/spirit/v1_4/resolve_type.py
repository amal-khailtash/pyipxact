from enum import Enum

__NAMESPACE__ = "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.4"


class ResolveType(Enum):
    """Determines how a property is resolved.

    Immediate means the value is included in the XML document and cannot
    be changed by the user.  User means the value must be obtained from
    the user.  Dependent means the value depends on the value of other
    properties.  A dependency expression must be supplied in the
    dependency attribute.  Generated means the value will be provided by
    a generator.

    :cvar IMMEDIATE: Property value is included in the XML file.  It
        cannot be configured.
    :cvar USER: Property content can be modified through confiugration.
        Modifications will be saved with the design.
    :cvar DEPENDENT: Property value is expressed as an XPath expression
        which may refer to other properties.  The expression must appear
        in the dendency attribute.
    :cvar GENERATED: Generators may modify this property.  Modifications
        get saved with the design.
    """

    IMMEDIATE = "immediate"
    USER = "user"
    DEPENDENT = "dependent"
    GENERATED = "generated"
