from .Body import MDUpdateBody
from .Header import FIXHeader


class MDMessage:
    def __init__(self, header: FIXHeader, body: MDUpdateBody, original_message: bytes=None):
        self.header = header
        self.body = body
        self.original_message = original_message