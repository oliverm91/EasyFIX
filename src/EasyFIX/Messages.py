from .Body import MDUpdateBody
from .Header import FIXHeader

class MDMessage:
    def __init__(self, header: FIXHeader, body: MDUpdateBody):
        self.header = header
        self.body = body