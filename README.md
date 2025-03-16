# Workspace Scanner and Extractor

## Overview

This Python script (`main.py`) scans a specified workspace directory and creates a comprehensive text file that includes:

1. A hierarchical representation of the directory structure
2. The content of all code files in the workspace

The tool is designed to help developers document their codebase, prepare for code reviews, or create a single file containing all relevant code for analysis or sharing.

## Features

- **Directory Structure Visualization**: Creates an indented tree view of your project's folder structure
- **Code Content Extraction**: Extracts and combines the content of all code files into a single document
- **Customizable Filtering**: Allows you to specify which file types to include and which directories/files to exclude
- **Encoding Handling**: Attempts to handle different file encodings (UTF-8 and CP1252)
- **Statistics Reporting**: Provides feedback on the number of files and directories processed

## Requirements

- Python 3.6 or higher
- No external dependencies (uses only the standard library)

## Installation

No installation is required. Simply download the `main.py` file to your computer.

## Usage

1. Open the `main.py` file in a text editor
2. Modify the configuration variables at the top of the file:
   ```python
   # Define the directory you want to scan
   workspace_dir = 'd:\AI'  # Change this to your workspace path
   
   # Define the output file
   output_file = 'd:\AI\workspace_output.txt'  # Change this to your desired output location
   ```
3. Run the script:
   ```
   python main2.py
   ```
4. Check the output file at the specified location

## Configuration Options

### File Extensions to Include

By default, the script includes files with the following extensions:
```python
code_extensions = ['.py', '.js', '.html', '.css', '.json', '.md', '.txt']
```

To include all file types, set this to an empty list:
```python
code_extensions = []
```

### Excluded Directories

The script automatically excludes common build, dependency, and data directories:

```python
excluded_directories = [
    # Version Control
    '.git', '.svn', '.hg',
    # Build and Distribution
    'build', 'dist', 'out', 'target', 'bin', 'obj',
    # Dependencies
    'node_modules', 'vendor', 'packages', 'venv', 'env',
    # Data and Cache
    'data', 'cache', '.cache', '__pycache__'
]
```

### Excluded File Extensions

The script automatically excludes common data, log, and temporary file extensions:

```python
excluded_extensions = [
    # Data files
    '.json', '.xml', '.yaml', '.yml', '.csv', '.dat',
    # Log files
    '.log', '.logs',
    # Temporary and cache files
    '.tmp', '.temp', '.cache',
    # Compiled and build artifacts
    '.pyc', '.pyo', '.class', '.o', '.obj', '.dll', '.exe',
    # Debug and IDE files
    '.pdb', '.idb', '.suo',
    # Documentation and reports
    '.txt', '.pdf', '.doc', '.docx'
]
```

## Output Format

The output file contains:

1. A tree view of the directory structure with indentation
2. The content of each included file, preceded by its file path
3. Separator lines between files for better readability

Example output:
```
AI/
    src/
        main.py
        utils.py
    docs/
        readme.md


# FILE: d:\AI\src\main.py

[file content here]

--------------------------------------------------------------------------------

# FILE: d:\AI\src\utils.py

[file content here]

--------------------------------------------------------------------------------
```

## Error Handling

The script attempts to handle different file encodings:
1. First tries to read files with UTF-8 encoding
2. If that fails, attempts to read with CP1252 encoding
3. If both fail, includes an error message in the output file

## Limitations

- Binary files or files with unusual encodings may not be properly included
- Very large workspaces may result in large output files
- The script does not preserve file formatting beyond plain text

## Customization

To customize the script for your specific needs, you can modify:

- The `should_exclude()` function to implement more complex filtering logic
- The output format by changing the string formatting in the write operations
- The encoding handling to support additional file encodings

## License

This script is provided as-is with no warranty. Feel free to modify and distribute as needed.