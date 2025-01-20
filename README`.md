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

## Usage

1. Save the script as `clean_filenames.py`
2. Run the script:

   ```bash
   python clean_filenames.py
   ```

3. Enter the directory path when prompted
4. Confirm the operation

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
