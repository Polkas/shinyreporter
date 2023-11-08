from typing import Callable, TypeVar
from typing_extensions import ParamSpec, Concatenate

from shiny.session import Session, Inputs, Outputs

P = ParamSpec("P")
R = TypeVar("R", covariant=True)

ShinyUI = Callable[[], R]
ShinyServer = Callable[[Inputs, Outputs, Session], R]
