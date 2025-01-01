from textual.app import App, ComposeResult
from textual.widgets import Header, Footer, Input, Label, RichLog, LoadingIndicator
from textual.containers import VerticalGroup, HorizontalGroup, VerticalScroll
# from find_largest_folders_and_files import analyze_path

class Widgets(VerticalGroup):

    def compose(self) -> ComposeResult:
        yield Label("poo")
        yield Label("poo")
        yield Label("poo")
        yield Label("poo")
        yield Label("poo")

class TestApp(App):

    def compose(self) -> ComposeResult:
        yield Header(name="Header")
        yield Widgets()
        yield RichLog()
        yield Input(placeholder="Input")
        yield Footer()

if __name__ == '__main__':
    app = TestApp()
    app.run()
