import os
from pathlib import Path

def get_parent_folders(file_path, levels=3):
    path = Path(file_path)
    
    parents = []
    current_parent = path.parent
    for _ in range(levels):
        if current_parent == current_parent.parent:
            break
        parents.append(current_parent.name)
        current_parent = current_parent.parent
    
    return parents
