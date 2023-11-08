from shinyreporter import report_server, report_ui, Report, ContentBlock, StringBlock
from shiny import App, ui, Inputs, Outputs, Session, reactive

app_ui = ui.page_fluid(report_ui("report"))


def server(inputs: Inputs, outputs: Outputs, session: Session):
    report: Report = Report()
    report.add_block(StringBlock("This is a string block"))
    report.add_block(ContentBlock("This is a content block with a string in it"))
    report.add_block(ContentBlock(8))
    report.add_block(ContentBlock())
    report_server("report", report=report)


app = App(app_ui, server)
