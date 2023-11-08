from typing import List

from .ContentBlock import ContentBlock

__all__ = ["Report"]


class Report:
    def __init__(self) -> None:
        self._blocks: List[ContentBlock] = []

    def add_block(self, block: ContentBlock) -> None:
        self._blocks.append(block)

    def blocks(self) -> List[ContentBlock]:
        return self._blocks
