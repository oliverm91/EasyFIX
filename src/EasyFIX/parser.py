from EasyFIX.Messages import MDMessage
from Header import FIXHeader
from definitions.header import accepted_header_tags, header_tags_dict, HeaderTags, accepted_msg_types, msg_type_dict
from definitions.market_data.tags import accepted_md_tags, MDTags, MDRepeatingGroupConfiguration, repeating_group_starter_tags, repeating_group_configurations, md_tags_dict
from definitions.market_data.values import value_dict_mapper
from Body import MDUpdateBody, MDEntry, RepeatingGroup


__SOH__ = b'\x01'
__BODY_HEADER_SPLITTER__ = __SOH__ + b'262='
__ENTRIES_SPLITTER__ = __SOH__ + b'279='
__FOOTER_SPLITTER__ = __SOH__ + b'10='
__TAG_SPLITTER__ = b'='
def create_fix_message(byte_fix_message: bytes) -> MDMessage:
    header_bytes, body_bytes = byte_fix_message.split(__BODY_HEADER_SPLITTER__)
    body_bytes = b'262=' + body_bytes
    header = create_header(header_bytes)
    body = create_md_update_body(body_bytes)

    return MDMessage(header, body)


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


def create_md_update_body(byte_body_fix_message: bytes) -> MDUpdateBody:
    byte_body_fix_message, _ = byte_body_fix_message.split(__FOOTER_SPLITTER__)
    entries_message = byte_body_fix_message.split(__ENTRIES_SPLITTER__)[1:]
    
    entries = []
    for entry_message in entries_message:
        entry_message = b'279=' + entry_message
        tag_values = entry_message.split(__SOH__)
        tag_splitter = __TAG_SPLITTER__
        entry_inner_dict = {}
        starter_tag_repeating_groups = None
        for tag_value in tag_values:
            tag, value = tag_value.split(tag_splitter)
            if tag not in accepted_md_tags:
                continue
            enumed_tag = md_tags_dict[tag]
            if enumed_tag not in repeating_group_starter_tags:
                enum_dict = value_dict_mapper.get(enumed_tag, None)
                if enum_dict is None:
                    entry_inner_dict[md_tags_dict[enumed_tag]] = value
                else:
                    enumed_value = enum_dict[enumed_tag]
                    entry_inner_dict[md_tags_dict[enumed_tag]] = enumed_value
            else:
                # Process repeating_group: Maybe add to a list or dict of entry tag_values and process them separetly?
                pass
            entry = MDEntry(entry_inner_dict, starter_tag_repeating_groups)
            entries.append(entry)

    body = MDUpdateBody(entries)
    return body