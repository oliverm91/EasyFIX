from definitions.market_data.tags import MDTags


class RepeatingGroup:
    __slots__ = ('_inner_dict',)
    def __init__(self, inner_dict: dict[MDTags, str]):
        self._inner_dict = inner_dict

    def get_tag_value(self, tag: MDTags) -> str:
        try:
            return self._inner_dict[tag]
        except KeyError as _:
            raise KeyError(f'Tag {tag} not found in inner dict: {self._inner_dict}')
        

class MDEntry:
    __slots__ = ('_inner_dict', '_starter_tag_repeating_groups')
    def __init__(self, inner_dict: dict[MDTags, str], starter_tag_repeating_groups: dict[MDTags, list[RepeatingGroup]]=None):
        self._inner_dict = inner_dict
        self._starter_tag_repeating_groups = starter_tag_repeating_groups

    def get_tag_value(self, market_data_tag: MDTags) -> str:
        try:
            return self._inner_dict[market_data_tag]
        except KeyError as _:
            raise KeyError(f'Market Data tag {market_data_tag} not found in inner dict: {self._inner_dict}')
        
    def get_repeating_group(self, repeating_group_starter_tag: MDTags) -> list[RepeatingGroup]:
        try:
            return self._starter_tag_repeating_groups[repeating_group_starter_tag]
        except KeyError as _:
            raise KeyError(f'Repeating group starter tag {repeating_group_starter_tag} not found: {self._starter_tag_repeating_groups}')
        

class MDUpdateBody:
    def __init__(self, entries: list[MDEntry]):
        self.entries = entries