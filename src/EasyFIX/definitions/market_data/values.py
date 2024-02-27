from enum import Enum

from .tags import MDTags


class MDUpdateAction(Enum):
    New = '0'
    Change = '1'
    Delete = '2'

md_update_action_dict: dict[str, MDUpdateAction] = {mdua.value: mdua for mdua in MDUpdateAction}


class MDEntryType(Enum):
    Bid = '0'
    Offer = '1'
    Trade = '2'
    ClosingPrice = '5'
    Duration = 'r'

md_entry_type_dict: dict[str, MDEntryType] = {mdet.value: mdet for mdet in MDEntryType}


class Side(Enum):
    Buy = '1'
    Sell = '2'
    ShortSell = '5'

side_dict: dict[str, Side] = {s.value: s for s in Side}


class LastFragment(Enum):
    LastMessage = 'Y'
    NotLastMessage = 'N'

last_fragment_dict: dict[str, LastFragment] = {lf.value: lf for lf in LastFragment}

value_dict_mapper: dict[MDTags, dict[str, Enum]] = {
    MDTags.MDUpdateAction: md_update_action_dict,
    MDTags.MDEntryType: md_entry_type_dict,
    MDTags.Side: side_dict,
    MDTags.LastFragment: last_fragment_dict
}