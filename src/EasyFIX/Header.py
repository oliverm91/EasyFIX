from typing import Any
from .definitions.header import HeaderTags


class FIXHeader:
    __slots__ = '_inner_dict', 'message_type'
    def __init__(self, inner_dict: dict[HeaderTags, Any]):        
        self._inner_dict = inner_dict
        self.message_type = self.get_tag_value(HeaderTags.MsgType)
        
    def get_tag_value(self, header_tag: HeaderTags) -> Any:
        try:
            return self._inner_dict[header_tag]
        except KeyError as _:
            raise KeyError(f'Header tag {header_tag} not found in inner dict: {self._inner_dict}')
