from collections.abc import Iterable
from dataclasses import dataclass, field
from typing import Optional

from org.accellera.spirit.v1_0.name_value_type_type import NameValueTypeType
from org.accellera.spirit.v1_0.signal import Signal
from org.accellera.spirit.v1_0.vendor_extensions import VendorExtensions
from org.accellera.spirit.v1_0.view_type import ViewType

__NAMESPACE__ = "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.0"


@dataclass(slots=True)
class HwModelType:
    """
    Hardware model information.

    :ivar views: View container
    :ivar signals: Signal container
    :ivar hw_parameters: Hardware parameter name value pairs container
    :ivar vendor_extensions:
    """

    class Meta:
        name = "hwModelType"

    views: Optional["HwModelType.Views"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.0",
        },
    )
    signals: Optional["HwModelType.Signals"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.0",
        },
    )
    hw_parameters: Optional["HwModelType.HwParameters"] = field(
        default=None,
        metadata={
            "name": "hwParameters",
            "type": "Element",
            "namespace": "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.0",
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
    class Views:
        view: Iterable[ViewType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.0",
            },
        )

    @dataclass(slots=True)
    class Signals:
        signal: Iterable[Signal] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.0",
            },
        )

    @dataclass(slots=True)
    class HwParameters:
        """
        :ivar hw_parameter: A hardware parameter name value pair.  The
            name is given in an attribute.  The value is the element
            value. The dataType (applicable to high level modeling) is
            given in the dataType attribute. The name should be
            identical to the RTL (VHDL generic or Verilog parameter)
        """

        hw_parameter: Iterable[NameValueTypeType] = field(
            default_factory=list,
            metadata={
                "name": "hwParameter",
                "type": "Element",
                "namespace": "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.0",
            },
        )
