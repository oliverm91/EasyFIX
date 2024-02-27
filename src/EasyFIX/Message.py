from Body import FIXBody
from Header import FIXHeader


class FIXMessage:
    def __init__(self, header: FIXHeader, body: FIXBody):
        self.header = header
        self.body = body