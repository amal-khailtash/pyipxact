from enum import Enum

__NAMESPACE__ = "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1685-2009"


class GroupSelectorMultipleGroupSelectionOperator(Enum):
    AND = "and"
    OR = "or"