import os
import click
import platform
import subprocess
from httpx import head
from rich.console import Console
from rich.style import Style
from rich.color import Color
from pathlib import Path

# CONFIGURATION:
parent_folders = {} # Dictionary to store parent folder sizes
sub_folders = {} # Dictionary to store sub-folder sizes
largest_folders = {} # Dictionary to store largest sub-folders
largest_files = {} # Dictionary to store largest files

# RICH CONSOLE:
console = Console()

# STYLES & COLORS:
fg_parent = Color.from_rgb(255,255,102) # Yellow
bg_parent = Color.from_rgb(160,160,160) # Grey
heading_ = Style(color='green', bold=True, underline=True, bgcolor='black')
parent_ = Style(color=fg_parent, bold=True, bgcolor=None)
sub_ = Style(color='red')



@click.command()
@click.argument('config_path', default=Path.home()/'Library')
@click.option('--num_results', default=10)
def analyze_path(config_path: Path, num_results: int):

    global parent_folders, largest_folders

    run = True

    config_path = Path(config_path)

    def get_depth(base: Path, target: Path):
        try:
            relative_path = target.relative_to(base)
            return len(relative_path.parts), relative_path.parts  # Number of subdirectories deep
        except ValueError:
            return None  # If the path isn't relative to the base

    # Recursively calculate folder sizes and
    def size_up(path: Path):

        global sub_folders, largest_files

        depth, parts = get_depth(config_path, Path(path))
        parent_path = config_path / parts[0]
        folder_size = 0

        if parent_path not in sub_folders:
            sub_folders[config_path / parts[0]] = {}

        try:
            with os.scandir(path) as entries:
                for entry in entries:
                    try:
                        if entry.is_dir(follow_symlinks=False):
                            folder_size += size_up(entry.path)
                            if depth > 1:
                                sub_folders[config_path / parts[0]][parts[1]] = folder_size
                        else:
                            file_size = entry.stat(follow_symlinks=False).st_size
                            folder_size += file_size
                            largest_files[entry.path] = file_size
                    except (FileNotFoundError, PermissionError) as e:
                        print(f"\nSkipping {entry.path}: {e}")
                        continue
        except (FileNotFoundError, PermissionError) as e:
            print(f"\nError accessing {path}: {e}")
            pass
        return folder_size

    def sort_by_size(folders:dict):
        return sorted(folders.items(), key=lambda x: x[1], reverse=True)

    def open_folder(path):
            if platform.system() == "Windows":
                os.startfile(path)
            elif platform.system() == "Darwin":  # macOS
                subprocess.run(["open", path])
            else:  # Linux
                subprocess.run(["xdg-open", path])

    with console.status("[bold green]Sizing up files and folders (this may take a while)..."):
        for folder in config_path.iterdir():
            if folder.is_dir():
                parent_folders[folder] = size_up(folder)

    # Sort by size and display results
    sorted_parent_folders = sort_by_size(parent_folders)

    parent_folder_header = f"Top {num_results} folders by size in {config_path}".upper()
    console.print(parent_folder_header, style=heading_)
    for folder, size in sorted_parent_folders[:num_results]:
        console.print(f"{folder}: {size/(1024*1024):.2f} MB", style=parent_)
        sorted_sub_folders = sort_by_size(sub_folders[folder])
        for folder, size in sorted_sub_folders[:num_results]:
            console.print(f"   {folder}: {size/(1024*1024):.2f} MB", style=sub_)
            if size > 1000 * 1024 * 1024:
                largest_folders[folder] = size

    sorted_largest_folders = sort_by_size(largest_folders)

    sub_folder_header = f"Top {num_results} sub-folders by size".upper()
    console.print(sub_folder_header, style=heading_)
    for folder, size in sorted_largest_folders[:num_results]:
        console.print(f"{folder}: {size/(1024*1024):.2f} MB", style=sub_)

    sorted_largest_files = sort_by_size(largest_files)

    largest_files_header = f"Top {num_results} files by size".upper()
    console.print(largest_files_header, style=heading_)
    for file, size in sorted_largest_files[:num_results]:
        console.print(f"{file}: {size/(1024*1024):.2f} MB", style=sub_)

    click.echo(click.style(f'\nSized up all the folders and files in {config_path}.\nWould you like to open the folders for the largest files?', bold=True, fg='green'))
    open_folders = click.confirm('')

    if open_folders:
        click.echo(click.style(f"\nOpening folders for top {num_results} largest files...", bold=True, fg='green'))
        for file, size in sorted_largest_files[:num_results]:
            open_folder(str(Path(file).parent))

        click.echo(click.style(f"\nFolders have been opened, would you like to size up another directory?", bold=True, fg='green'))
        run_again = click.confirm('', abort=True)
    else:
        click.echo(click.style(f"\nWould you like to size up another directory?", bold=True, fg='green'))
        run_again = click.confirm('', abort=True)

    if run_again:
        analyze_path()

analyze_path()
