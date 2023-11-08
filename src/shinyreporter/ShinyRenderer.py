from abc import abstractmethod
from typing import Any, TypeVar, Protocol, Tuple, Callable
from typing_extensions import ParamSpec, Concatenate

from .ContentBlock import ContentBlock
from .type_aliases import ShinyUI, ShinyServer
from shiny import reactive, render, ui, module
from shiny.session import Inputs, Outputs, Session

__all__ = ["ShinyRenderer", "TextRenderer"]

CBlock = TypeVar("CBlock", bound="ContentBlock", contravariant=True)
RendererOut = TypeVar("RendererOut", covariant=True)


class ShinyRenderer(Protocol[CBlock, RendererOut]):
    @abstractmethod
    def render(self, block: CBlock) -> RendererOut:
        ...


class TextRenderer(ShinyRenderer[ContentBlock[str], Tuple[ShinyUI, ShinyServer]]):
    def render(self, block: ContentBlock[str]) -> Tuple[ShinyUI, ShinyServer]:
        def custom_ui() -> ui.tagChild:
            ui.div(block.get_content() or "Empty block!")

        def custom_srv(input: Inputs, output: Outputs, session: Session):
            pass

        def f(ui: ShinyUI) -> None:
            pass

        f(custom_ui)

        return custom_ui, custom_srv
