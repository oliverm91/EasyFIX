from typing import Any
from definitions.market_data_tags import MarketDataTags


class RepeatingGroup:
    pass


class MDEntry:
    __slots__ = ('_inner_dict',)
    def __init__(self, inner_dict: dict[MarketDataTags, Any]):
        self._inner_dict = inner_dict

    def get(self, market_data_tag: MarketDataTags) -> Any:
        try:
            return self._inner_dict[market_data_tag]
        except KeyError as _:
            raise KeyError(f'Market Data tag {market_data_tag} not found in inner dict: {self._inner_dict}')
        

class FIXBody:
    def __init__(self, entries: list[MDEntry]):
        self.entries = entries