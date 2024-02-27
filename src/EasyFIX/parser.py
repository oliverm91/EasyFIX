from Message import FIXMessage
from Header import FIXHeader
from definitions.header import accepted_header_tags, header_tags_dict, HeaderTags, accepted_msg_types, msg_type_dict
from Body import FIXBody

__SOH__ = b'\x01'
__BODY_HEADER_SPLITTER__ = __SOH__ + b'279='
__TAG_SPLITTER__ = b'='
def create_fix_message(byte_fix_message: bytes) -> FIXMessage:
    header_bytes, body_bytes = byte_fix_message.split(__BODY_HEADER_SPLITTER__)
    header = create_header(header_bytes)
    body = create_body(body_bytes)

    return FIXMessage(header, body)


def create_header(byte_header_fix_message: bytes) -> FIXHeader:
    tag_values = byte_header_fix_message.split(__SOH__)
    inner_dict = {}
    tag_splitter = __TAG_SPLITTER__
    for tag_value in tag_values:
        tag, value = tag_value.split(tag_splitter)
        if tag not in accepted_header_tags:
            continue
        inner_dict[header_tags_dict[tag]] = value

    msg_type_value = inner_dict[HeaderTags.MsgType]
    if msg_type_value in accepted_msg_types:
        inner_dict[HeaderTags.MsgType] = msg_type_dict[msg_type_value]
        return FIXHeader(inner_dict)
    else:
        raise ValueError(f'Message Type 35={msg_type_value} not supported')


def create_body(byte_body_fix_message: bytes, header: FIXHeader) -> FIXBody:
    entry_amount = header.get(HeaderTags.NoMDEntries)
    