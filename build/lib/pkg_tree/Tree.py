import os
import ast

def analyze_file(file_path):
    """Analyze a Python file to extract its classes, methods, and their arguments."""
    with open(file_path, "r", encoding="utf-8") as file:
        tree = ast.parse(file.read())
    methods = []
    classes = {}
    for node in ast.iter_child_nodes(tree):
        if isinstance(node, ast.FunctionDef):
            args = [arg.arg for arg in node.args.args]
            methods.append((node.name, args))
        elif isinstance(node, ast.ClassDef):
            class_methods = {}
            for class_node in node.body:
                if isinstance(class_node, ast.FunctionDef):
                    args = [arg.arg for arg in class_node.args.args]
                    class_methods[class_node.name] = args
            classes[node.name] = class_methods
    return methods, classes

def generate_tree(directory, indent="", show_args=True, skip_files=None):
    """
    Recursively generate a tree of the Python package structure.

    Parameters:
    - directory (str): Path to the directory to analyze.
    - indent (str): Indentation for the tree structure.
    - show_args (bool): Whether to display function/method arguments.
    - skip_files (set): A set of filenames or patterns to skip.
    """
    default_skip_files = {".ipynb_checkpoints", "__init__.py", "Tree.py"}  # Default files to skip
    skip_files = set(skip_files or []) | default_skip_files  # Merge custom and default skips

    for item in sorted(os.listdir(directory)):
        if item in skip_files:  # Skip specific files
            continue
        item_path = os.path.join(directory, item)
        if os.path.isdir(item_path):
            print(f"\n{indent}📂 **{item}/**")
            generate_tree(item_path, indent + "   ", show_args, skip_files)
        elif item.endswith(".py"):
            print(f"\n{indent}📄 **{item}**")
            methods, classes = analyze_file(item_path)
            if methods:
                print(f"{indent}   🔧 Functions:")
                for method, args in methods:
                    if show_args:
                        print(f"{indent}      - `{method}({', '.join(args)})`")
                    else:
                        print(f"{indent}      - `{method}()`")
            if classes:
                print(f"{indent}   🏷️ Classes:")
                for cls, cls_methods in classes.items():
                    print(f"{indent}      - **class {cls}**")
                    if cls_methods:
                        print(f"{indent}         Methods:")
                        for method, args in cls_methods.items():
                            if show_args:
                                print(f"{indent}            - `{method}({', '.join(args)})`")
                            else:
                                print(f"{indent}            - `{method}()`")

