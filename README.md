# pkg_tree

`pkg_tree` is a Python package designed to analyze Python files and generate a structured tree representation of a Python package.

## Features

- Analyze Python files to extract:
  - Classes and their methods
  - Functions and their arguments
- Generate a visually appealing tree of a Python package structure.
- Skip unnecessary files and directories during analysis.

## Installation

You can install using

```bash
pip install git+https://github.com/santoshrajkumar/pkg_tree.git
```

## Usage

Here's how you can use `pkg_tree` in your projects:

### Example 1: Generating a Tree

```python
from pkg_tree import generate_tree

# Analyze and print the tree of a package
generate_tree("path/to/your/package")
```

### Example 2: Customizing Output

```python
from pkg_tree import generate_tree

# Generate a tree with specific options
generate_tree(
    directory="path/to/your/package",
    indent="  ",
    show_args=False,
    skip_files={"example.py", "test.py"}
)
```

## Contributing

Contributions are welcome! Please fork this repository and submit a pull request.

## License

This project is licensed under the MIT License. See the LICENSE file for details.
