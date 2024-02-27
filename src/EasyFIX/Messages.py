from Body import MDBody
from Header import FIXHeader

class MDMessage:
    def __init__(self, header: FIXHeader, body: MDBody):
        self.header = header
        self.body = body