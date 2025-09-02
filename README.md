# MCP File System Server

This project is an MCP (Model Context Protocol) server designed to provide file system utilities via a set of tools. It allows you to interact with your file system in a controlled and extensible way, leveraging the MCP protocol for integration with AI agents or other clients.

## Features

- **Directory Search**: Find directories by name within a set of allowed base directories.
- **List Files**: List all files in a specified directory, with support for ignoring certain subdirectories.
- **Move Files**: Move files from one directory to another, with options for filtering by extension and recursive moves.
- **Configurable Allowed Directories**: Restricts file operations to directories listed in `.allowed_dirs` for safety.

## Project Structure

- `server.py` — Main MCP server implementation and tool definitions.
- `utils.py` — Utility functions for directory searching and validation.
- `.allowed_dirs` — List of directories where file operations are permitted.
- `pyproject.toml`, `uv.lock` — Project dependencies and environment management.

## Usage

1. **Configure Allowed Directories**
	- Edit `.allowed_dirs` to specify which directories the server can access.

2. **Run the Server**
	```bash
	python server.py
	```
	The server will start and listen for MCP protocol requests.

3. **Available Tools**
	- `add(a, b)`: Example tool that adds two numbers.
	- `list_files(directory_name, base_dir=None, ignore_dirs=None)`: Lists files in a directory.
	- `move_files(src, dest, base_dir=None, recursive=False, extension='.*')`: Moves files between directories.

## Security

- All file operations are restricted to directories listed in `.allowed_dirs`.
- Hidden directories are ignored during searches.

## Requirements

- Python 3.10+
- [mcp](https://github.com/context-labs/model-context-protocol) (with `mcp[cli]`)


*This project is intended for local file system management and experimentation with MCP servers.*  
*README created using Cursor*
