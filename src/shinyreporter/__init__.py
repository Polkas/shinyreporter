# read version from installed package
from importlib.metadata import version

__version__ = version("shinyreporter")

from .ContentBlock import ContentBlock
from .StringBlock import StringBlock
from .Report import Report
from .report_module import report_ui, report_server
from .RendererDispatch import get_renderer
