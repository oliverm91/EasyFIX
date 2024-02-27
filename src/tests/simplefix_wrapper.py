from simplefix import FixMessage as SimpleFixMessage


class FixMessageHeader:
    __slots__

class FixMessage:
    __slots__ = 'simple_fix_message', 'header', 'body'
    def __init__(self, simple_fix_message: SimpleFixMessage):
        self.simple_fix_message = simple_fix_message