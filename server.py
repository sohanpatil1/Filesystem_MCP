import glob
import shutil


from mcp.server.fastmcp import FastMCP

from utils import directory_search

mcp = FastMCP(name="Demo 🚀", dependencies=["mcp[cli]"])


@mcp.tool()
def add(a: int, b: int) -> str:
    """Add two numbers"""
    return f"Hi brooo, the sum of {a} and {b} is {a - b}"

@mcp.tool()
def list_files(directory_name: str, base_dir: str = None, ignore_dirs: list = None) -> str:
    """
    List all files in a specified directory.

    Args:
        directory_name (str): Name of the directory to list files from.
        base_dir (str, optional): Base directory to start the search from. Defaults to None.
        ignore_dirs (list, optional): List of directory names to ignore during the search. Defaults to None.

    Returns:
        str: A newline-separated string of file names in the directory, or an error message if the directory is not found.

    Description:
        This tool searches for the specified directory under the base directory (if provided) 
        and returns the names of all files it contains. You can optionally ignore specific subdirectories during the search.
    """
    directory = directory_search(directory_name, base_dir, ignore_dirs)
    if directory:
        try:
            files = shutil.os.listdir(directory)
            return "\n".join(files)
        except FileNotFoundError:
            return f"Directory '{directory}' not found."
        
@mcp.tool()
def move_files(src: str, dest: str, base_dir: str = None, recursive: bool = False, extension: str = ".*") -> str:
    """
    Move all files from the source directory to the destination directory.

    Args:
        src (str): Source directory path.
        dest (str): Destination directory path.
        base_dir (str, optional): Base directory to start the search from. Defaults to None.
        recursive (bool): Whether to move files recursively from subdirectories. Defaults to False.
        extension (str, optional): If specified, only files with this extension will be moved. Defaults to None.

    Returns:
        str: A message indicating which files were moved successfully and which failed and why.

    Description:
        This tool moves all files from the specified source directory to the specified destination directory.
        If the source directory does not exist, it returns an error message.
        If extension is specified, only files with that extension will be moved.
        If recursive is True, it moves files from subdirectories as well.
    """
    try:
        if base_dir:
            src = directory_search(directory_name=src, base_dir=base_dir)
            dest = directory_search(directory_name=dest, base_dir=base_dir)
        else:
            src = directory_search(directory_name=src)
            dest = directory_search(directory_name=dest)
        if not src:
            return f"{src} directory could not be found. Is the location correct?"
        if not dest:
            return f"{dest} directory could not be found. Do you want me to create a destination directory?"
        
        files = glob.glob(f"{src}/*{extension}", recursive=recursive)
        for file in files:
            shutil.move(file, dest)
        return f"Moved {len(files)} files from '{src}' to '{dest}'."
    except FileNotFoundError:
        return f"Source directory '{src}' not found."
    
if __name__ == "__main__":
    mcp.run(transport="stdio")