from enum import Enum


class HeaderTags(Enum):
    BeginString = '8'
    BodyLength = '9'
    MsgType = '35'
    MsgSequenceNumber = '34'
    SenderCompID = '49'
    SendingTime = '52'
    TargetCompID = '56'
    NoMDEntries = '268'
    MDReqID = '262'

header_tags_dict: dict[str, HeaderTags] = {header_tag.value: header_tag for header_tag in HeaderTags}
accepted_header_tags: str[str] = set(header_tags_dict.keys())


class MsgType(Enum):
    HEART_BEAT = '0'
    TEST_REQUEST = '1'
    RESEND_REQUEST = '2'
    REJECT = '3'
    SEQUENCE_RESET = '4'
    LOGOUT = '5'
    LOGON = 'A'

    MD_SNAPSHOT = 'W'
    MD_INCREMENTAL_REFRESH = 'X'
    MD_REQUEST_REJECT = 'Y'
    SECURITY_STATUS_REQUESTS = 'e'

    BUSINESS_MESSAGE_REQUEST = 'j'

msg_type_dict: dict[str, MsgType] = {msg_type.value: msg_type for msg_type in MsgType}
accepted_msg_types: set[str] = set(msg_type_dict.keys())