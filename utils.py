import os

def allow_dirs():
    with open('.allowed_dirs', 'r') as f:
        dirs = f.read().splitlines()
    return dirs

def directory_search(directory_name: str, base_dir: str = None) -> list[str]:
    """
    Search for a directory and return a sorted list of unique matching paths.

    Args:
        directory_name (str): Directory name to search for, e.g. "images" or "Desktop/images".
        base_dir (str, optional): Base directory to start the search from. 
                                  If None, searches across all allowed_dirs.
    """
    allowed_dirs = allow_dirs()
    parts = directory_name.strip("/").split("/")

    parent_dir = parts[:-1]
    child_dir = parts[-1] if len(parts) > 1 else None

    # candidate roots to search
    search_roots = [base_dir] if base_dir else allowed_dirs

    matches = set()  # use a set for deduplication

    for root_dir in search_roots:
        for root, dirs, files in os.walk(root_dir):
            # filter out hidden dirs and enforce allowed_dirs
            dirs[:] = [
                d for d in dirs
                if not d.startswith(".")
                and any(
                    os.path.commonpath([os.path.join(root, d), allowed]) == allowed
                    for allowed in allowed_dirs
                )
            ]

            if child_dir:  # two-level search like Desktop/images
                if parent_dir in dirs:
                    dirs[:] = [parent_dir]  # restrict descent

                if os.path.basename(root) == child_dir and parent_dir in root:
                    matches.add(root)

            else:  # single-level search like images or Desktop
                if parent_dir in dirs and os.path.join(root, parent_dir) in allowed_dirs:
                    matches.add(os.path.join(root, parent_dir))

    # sort by path length (shorter paths = closer to base_dir)
    return sorted(matches, key=len)[0]

if __name__ == "__main__":
    directory_search("mcp_proj", "/Users/sohanpatil/Documents/VSWorkspace/")