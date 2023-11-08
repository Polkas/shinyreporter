from typing import Optional
from .ContentBlock import ContentBlock

__all__ = ["StringBlock"]


class StringBlock(ContentBlock[str]):
    def __init__(self, content: Optional[str] = None):
        super().__init__(content)
