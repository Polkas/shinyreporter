from abc import abstractmethod
from typing import Any, TypeVar, Protocol, Tuple, Callable
from typing_extensions import ParamSpec, Concatenate

from .ContentBlock import ContentBlock
from .type_aliases import ShinyUI, ShinyServer
from shiny import reactive, render, ui, module
from shiny.session import Inputs, Outputs, Session

__all__ = ["ShinyRenderer", "TextRenderer", "NumberRenderer"]

CBlock = TypeVar("CBlock", bound="ContentBlock", contravariant=True)
RendererOut = TypeVar("RendererOut", covariant=True)


class ShinyRenderer(Protocol[CBlock, RendererOut]):
    @abstractmethod
    def render(self, block: CBlock) -> RendererOut:
        ...


class TextRenderer(ShinyRenderer[ContentBlock[str], ShinyUI]):
    def render(self, block: ContentBlock[str]) -> ShinyUI:
        def custom_ui() -> ui.TagChild:
            return ui.div(block.get_content() or "Empty block!")

        return custom_ui


class NumberRenderer(ShinyRenderer[ContentBlock[int], ShinyUI]):
    def render(self, block: ContentBlock[int]) -> ShinyUI:
        return lambda: ui.div(block.get_content() or "Empty block!")
