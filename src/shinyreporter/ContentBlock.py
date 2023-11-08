from typing import List, Optional, Any, Dict, Generic, TypeVar

__all__ = ["ContentBlock"]

Content = TypeVar("Content")


class ContentBlock(Generic[Content]):
    """
    A class representing a content block with various methods to set and retrieve content.
    """

    def __init__(self, content: Optional[Content] = None):
        """
        Initializes an empty content block.
        """
        self._content: Optional[Content] = content

    def set_content(self, content: Content) -> None:
        """
        Sets the content of the content block.

        Args:
            content (Content): The content to be set. Can be of any type or None.
        """
        self._content = content

    def get_content(self) -> Optional[Content]:
        """
        Retrieves the content of the content block.

        Returns:
            str: The content as a string.
        """
        return self._content
