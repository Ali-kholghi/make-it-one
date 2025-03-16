import os

# Define the directory you want to scan
workspace_dir = 'd:\\AI-Scrper'

# Define the output file
output_file = 'd:\\AI-Scrper\\workspace_output.txt'

# Define file extensions to include (empty list means include all files)
code_extensions = ['.py', '.js', '.html', '.css', '.json', '.md', '.txt']

# Common build, dependency, and data directories across programming languages
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

# Common data, log, and temporary file extensions across programming languages
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

# Function to check if a path should be excluded
def should_exclude(path, is_dir=False):
    """
    Determines if a file or directory should be excluded from the output.
    
    Args:
        path: The file or directory path to check
        is_dir: Boolean indicating if the path is a directory
        
    Returns:
        True if the path should be excluded, False otherwise
    """
    if is_dir:
        # Check if directory name is in the excluded list
        dir_name = os.path.basename(path)
        return dir_name in excluded_directories
    else:
        # Check if file extension is in the excluded list
        file_ext = os.path.splitext(path)[1].lower()
        return file_ext in excluded_extensions

# Track statistics for feedback
processed_files = 0
processed_dirs = 0

# Open the output file in write mode
with open(output_file, 'w', encoding='utf-8') as outfile:
    # Write the project layout
    for root, dirs, files in os.walk(workspace_dir):
        # Filter out excluded directories (modifies dirs in-place)
        dirs[:] = [d for d in dirs if not should_exclude(os.path.join(root, d), is_dir=True)]
        processed_dirs += len(dirs)
        
        level = root.replace(workspace_dir, '').count(os.sep)
        indent = ' ' * 4 * level
        outfile.write(f'{indent}{os.path.basename(root)}/\n')
        subindent = ' ' * 4 * (level + 1)
        
        # Filter out excluded files
        filtered_files = [f for f in files if not should_exclude(os.path.join(root, f))]
        processed_files += len(filtered_files)
        for file in filtered_files:
            outfile.write(f'{subindent}{file}\n')
    outfile.write('\n\n')

    # Write each file's name and content
    for root, dirs, files in os.walk(workspace_dir):
        # Filter out excluded directories (modifies dirs in-place)
        dirs[:] = [d for d in dirs if not should_exclude(os.path.join(root, d), is_dir=True)]
        
        # Filter out excluded files
        filtered_files = [f for f in files if not should_exclude(os.path.join(root, f))]
        
        for file in filtered_files:
            file_path = os.path.join(root, file)
            
            # Skip the output file itself to avoid recursion
            if file_path == output_file:
                continue
                
            # Check if we should include this file
            file_ext = os.path.splitext(file)[1].lower()
            if not code_extensions or file_ext in code_extensions:
                outfile.write(f'# FILE: {file_path}\n\n')
                
                try:
                    with open(file_path, 'r', encoding='utf-8') as infile:
                        outfile.write(infile.read())
                except UnicodeDecodeError:
                    try:
                        with open(file_path, 'r', encoding='cp1252') as infile:
                            outfile.write(infile.read())
                    except:
                        outfile.write(f"[Error: Unable to read file - might be binary or use different encoding]\n")
                
                outfile.write('\n\n' + '-'*80 + '\n\n')

# Print success message with statistics
print(f"\nOperation completed successfully!")
print(f"Processed {processed_dirs} directories and {processed_files} files")
print(f"Output written to: {output_file}")
