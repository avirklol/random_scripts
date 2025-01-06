import os
import platform
import subprocess
from pathlib import Path
from textual.app import App, ComposeResult
from textual.widgets import Header, Footer, Input, Label, RichLog, LoadingIndicator, Button
from textual.containers import VerticalGroup, HorizontalGroup, VerticalScroll, Container, Horizontal, Vertical
from textual.screen import Screen
from textual.geometry import Size
from large_file_finder import analyze_path

config_path = Path.home()/'Library'

# screen_size = Size(40, 60)

class FolderLog(RichLog):

    BORDER_TITLE = "FOLDERS"

    def compose(self) -> ComposeResult:
        yield RichLog(id="folder_log")

class FileLog(RichLog):

    BORDER_TITLE = "FILES"

    def compose(self) -> ComposeResult:
        yield RichLog(id="file_log")

class Output(Vertical):

    BORDER_TITLE = "OUTPUT"

    def compose(self) -> ComposeResult:
        yield FolderLog()
        yield FileLog()

class ConfigQuery(Vertical):

    BORDER_TITLE = "CONFIG AND QUERY"

    def compose(self) -> ComposeResult:
        with Horizontal(id="config_query_header"):
            yield Button("Select Path", id="path_select")
            yield Label(f"Path: {config_path}", id="path")
        with Vertical(id="config_query_body"):
            yield RichLog(id="config_log")
            yield Input(placeholder=">>>", id="query_input")

class Widgets(Vertical):

    BORDER_TITLE = "WIDGETS"

    def compose(self) -> ComposeResult:
        yield Label("Elapsed Scan Time", id="widget_1")
        yield Label("Total GB", id="widget_2")
        yield Label("BIG ASS APPS", id="widget_3")

class TestApp(Screen):

    def compose(self) -> ComposeResult:
        yield Header(name="Header")
        with Container (id="app_grid"):
            yield Widgets(id='widgets')
            yield Output(id='log')
            yield ConfigQuery(id='config_query')
        yield Footer()

class _app(App):

    TITLE = "Large File Finder"
    CSS_PATH = "test.tcss"
    # size = screen_size

    def on_ready(self):
        self.push_screen(TestApp())

if __name__ == '__main__':
    app = _app()
    app.run()
x
