from typing import Dict, Any, TypeVar, Union, Optional, Type

from .ShinyRenderer import TextRenderer, ShinyRenderer, NumberRenderer
from .StringBlock import StringBlock
from .ContentBlock import ContentBlock

__all__ = ["renderer_dispatch", "get_renderer"]

# This needs to have Any as one of the allowed types, which is not super useful
# but this way we allow to register new renderers.
# The type analysis is static, so if we type this dict statically, we cannot
# properly type the `register_renderer` function
renderer_dispatch: dict[Type, Type[Union[TextRenderer, NumberRenderer, Any]]] = {
    str: TextRenderer,
    StringBlock: TextRenderer,
    int: NumberRenderer,
}

Block = TypeVar("Block", bound="ContentBlock")


def get_renderer(block: Block) -> Union[TextRenderer, NumberRenderer, Any, None]:
    return (
        renderer_dispatch.get(block.__class__)
        or renderer_dispatch.get(block.get_content().__class__)
        or None
    )


Renderer = TypeVar("Renderer", bound="ShinyRenderer")


def register_renderer(type: Any, renderer: Renderer):
    renderer_dispatch[type] = type(renderer)
