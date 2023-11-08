from shiny import App, Inputs, Outputs, Session, module, reactive, render, ui
from .Report import Report
from .RendererDispatch import get_renderer

__all__ = ["report_ui", "report_server"]


@module.ui
def report_ui() -> ui.TagChild:
    return ui.div(ui.div("Report module"), ui.output_ui("blocks"))


@module.server
def report_server(inputs: Inputs, outputs: Outputs, session: Session, report: Report):
    @outputs
    @render.ui
    def blocks():
        blocks = report.blocks()

        def get_ui(block):
            renderer_class = get_renderer(block)
            if renderer_class:
                renderer = renderer_class()
                ui_func = renderer.render(block)
                return ui_func()
            return ui.div("No renderer found")

        return ui.div([get_ui(block) for block in blocks])
