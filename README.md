# Filename Cleaner

A Python script that recursively cleans filenames and folder names by removing special characters and ensuring computer-friendly naming conventions.

## Features

- Recursively processes all files and folders in a directory
- Removes special characters while maintaining readability
- Preserves spaces in filenames but uses underscores in folder names
- Handles duplicate names by adding incremental numbers
- Preserves file extensions
- Works on both Windows and Unix-style paths
- Safe operation with confirmation prompt
- Detailed operation summary

## Setting Up a Virtual Environment

It is recommended to use a virtual environment to run the script. Below are the instructions for creating and activating a virtual environment on different operating systems.

### Windows

1. Open PowerShell.
2. Navigate to your project directory.
3. Create a virtual environment:

   ```powershell
   python -m venv venv
   ```

4. Activate the virtual environment:

   ```powershell
   .\venv\Scripts\Activate
   ```

### Linux and Mac

1. Open a terminal.
2. Navigate to your project directory.
3. Create a virtual environment:

   ```bash
   python3 -m venv venv
   ```

4. Activate the virtual environment:

   ```bash
   source venv/bin/activate
   ```

### Using WSL2 Environment

If you are using a WSL2 environment on Windows, follow the Linux instructions above to create and activate the virtual environment.

## Usage

1. Save the script as `clean_filenames.py`

### Windows

1. Open PowerShell.
2. Navigate to your project directory.
3. Run the script:

   ```powershell
   python clean_filenames.py
   ```

4. Enter the directory path when prompted.
5. Confirm the operation.

### Linux and Mac

1. Open a terminal.
2. Navigate to your project directory.
3. Run the script:

   ```bash
   python3 clean_filenames.py
   ```

4. Enter the directory path when prompted.
5. Confirm the operation.

## Creating a Test Directory (OPTIONAL)

To create a test directory with various problematic filenames and folder names, you can use the `create_test_directory.py` script. This script sets up a directory structure that you can use to test the filename cleaner.

1. Save the script as `create_test_directory.py`
2. Run the script:

   ```bash
   python create_test_directory.py
   ```

3. The script will create a directory named `filename_cleaner_test` with various files and folders.

## File Naming Rules

### For Files

- Preserves spaces within names (e.g., "my document.txt")
- Replaces special characters with underscores
- Removes leading/trailing spaces
- Handles duplicates with numbered suffixes (e.g., "file_1.txt", "file_2.txt")
- Preserves file extensions

### For Folders

- Converts spaces and special characters to underscores
- Creates clean, script-friendly names (e.g., "My Documents!" -> "My_Documents")
- Handles duplicates with numbered suffixes

## Examples

  ``` txt
  Before:
    My Documents!/
      file (1).txt
      test-file@123.doc
    Program Files@/
      app_1.0.2 (beta).exe
      install-notes.txt

  After:
    My_Documents/
      file_1.txt
      test_file_123.doc
    Program_Files/
      app_1_0_2_beta.exe
      install_notes.txt
  ```

## Requirements

- Python 3.x
- No additional dependencies required

## Safety Features

- Confirmation prompt before processing
- Detailed reporting of all changes
- No overwriting of existing files
- Preserves original file extensions
- Bottom-up processing to handle nested paths safely

## Output Summary

The script provides a summary of operations:

- Number of files renamed
- Number of files skipped (already clean)
- Number of folders renamed
- Number of folders skipped (already clean)
- Any errors encountered
