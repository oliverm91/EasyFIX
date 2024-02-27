from enum import Enum

class MDUpdateAction(Enum):
    New = '0'
    Change = '1'
    Delete = '2'

md_update_action_dict: dict[str, MDUpdateAction] = {mdua.value: mdua for mdua in MDUpdateAction}


class MDEntryType(Enum):
    Trade = '2'
    Indexes = '3'
    ClosingPrice = '5'
    HighPrice = '7'
    LowPrice = '8'
    AveragePrice = '9'
    Duration = 'r'
    Benchmarks = 'A'

md_update_action_dict: dict[str, MDEntryType] = {mdet.value: mdet for mdet in MDEntryType}


class NoSides(Enum):
    OneSide = '1'
    BothSides = '2'

no_sides_dict: dict[str, NoSides] = {ns.value: ns for ns in NoSides}


class Side(Enum):
    Buy = '1'
    Sell = '2'
    ShortSell = '5'

side_dict: dict[str, Side] = {s.value: s for s in Side}


class LastFragment(Enum):
    LastMessage = 'Y'
    NotLastMessage = 'N'

side_dict: dict[str, LastFragment] = {lf.value: lf for lf in LastFragment}