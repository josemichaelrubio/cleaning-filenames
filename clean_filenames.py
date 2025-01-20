import os
import re
from pathlib import Path

def clean_name(name, preserve_spaces=True):
    """
    Convert a name to contain only alphanumeric characters and optional spaces.
    Special characters are replaced with underscores.
    
    Args:
        name: The filename or folder name to clean
        preserve_spaces: If True, maintain spaces. If False, convert spaces to underscores
    """
    # First normalize multiple spaces to single spaces
    clean = re.sub(r'\s+', ' ', name)
    
    # Replace special characters with underscores
    clean = re.sub(r'[^a-zA-Z0-9\s]', '_', clean)
    
    # Remove spaces around underscores
    clean = re.sub(r'\s*_\s*', '_', clean)
    
    if not preserve_spaces:
        # Convert all remaining spaces to underscores if not preserving spaces
        clean = clean.replace(' ', '_')
    
    # Remove consecutive underscores
    clean = re.sub(r'_+', '_', clean)
    
    # Remove leading/trailing underscores and spaces
    clean = clean.strip('_ ')
    
    return clean if clean else "unnamed"

def clean_filename(filename, preserve_spaces=True):
    """
    Convert a filename to contain only alphanumeric characters and extensions.
    Preserves the file extension and optionally preserves spaces.
    
    Args:
        filename: The filename to clean
        preserve_spaces: If True, maintain spaces. If False, convert spaces to underscores
    """
    # Split filename into name and extension
    name, ext = os.path.splitext(filename)
    
    # Clean the name part
    clean_name_part = clean_name(name, preserve_spaces)
    
    # Return cleaned filename with original extension
    return f"{clean_name_part}{ext}"

def rename_item(original_path, new_name, is_file=True):
    """
    Rename a file or folder while handling duplicates.
    If a name collision occurs, appends an incrementing number until a unique name is found.
    Returns the new path if successful, None if failed.
    """
    try:
        directory = os.path.dirname(original_path)
        new_path = os.path.join(directory, new_name)
        
        # If the new path is the same as the original, return early
        if new_path == original_path:
            return original_path
            
        # Handle duplicate names
        counter = 1
        while os.path.exists(new_path):
            if is_file:
                name, ext = os.path.splitext(new_name)
                # Remove any existing counter from the name
                name = re.sub(r'_\d+$', '', name)
                new_path = os.path.join(directory, f"{name}_{counter}{ext}")
            else:
                # For folders, remove any existing counter
                base_name = re.sub(r'_\d+$', '', new_name)
                new_path = os.path.join(directory, f"{base_name}_{counter}")
            counter += 1
        
        # Perform the rename operation
        os.rename(original_path, new_path)
        return new_path
    except (OSError, PermissionError) as e:
        print(f"Error renaming {original_path}: {str(e)}")
        return None

def rename_items_in_directory(directory):
    """
    Recursively rename all files and folders in the given directory
    to contain only alphanumeric characters.
    """
    try:
        # Convert directory to Path object
        dir_path = Path(directory)
        
        # Counters for summary
        stats = {
            'files_renamed': 0,
            'files_skipped': 0,
            'folders_renamed': 0,
            'folders_skipped': 0,
            'errors': 0
        }
        
        # First, process all files (bottom-up to handle nested paths)
        for root, dirs, files in os.walk(dir_path, topdown=False):
            # Process files
            for filename in files:
                original_path = os.path.join(root, filename)
                # For files, preserve spaces
                new_filename = clean_filename(filename, preserve_spaces=True)
                
                if new_filename != filename:
                    if rename_item(original_path, new_filename, is_file=True):
                        print(f"Renamed file: {original_path} -> {new_filename}")
                        stats['files_renamed'] += 1
                    else:
                        stats['errors'] += 1
                else:
                    stats['files_skipped'] += 1
            
            # Process directories
            for dirname in dirs:
                original_path = os.path.join(root, dirname)
                # For folders, don't preserve spaces, use underscores
                new_dirname = clean_name(dirname, preserve_spaces=False)
                
                if new_dirname != dirname:
                    if rename_item(original_path, new_dirname, is_file=False):
                        print(f"Renamed folder: {original_path} -> {new_dirname}")
                        stats['folders_renamed'] += 1
                    else:
                        stats['errors'] += 1
                else:
                    stats['folders_skipped'] += 1
        
        # Print summary
        print("\nRename Operation Summary:")
        print(f"Files renamed: {stats['files_renamed']}")
        print(f"Files skipped (already clean): {stats['files_skipped']}")
        print(f"Folders renamed: {stats['folders_renamed']}")
        print(f"Folders skipped (already clean): {stats['folders_skipped']}")
        print(f"Errors encountered: {stats['errors']}")
        
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    # Get directory path from user
    directory = input("Enter the directory path to clean filenames and foldernames: ").strip()
    
    # Verify directory exists
    if not os.path.isdir(directory):
        print("Error: Invalid directory path")
    else:
        # Confirm with user
        print(f"\nAbout to clean filenames and foldernames in: {directory}")
        print("WARNING: This will rename both files and folders to contain only alphanumeric characters.")
        confirm = input("Do you want to continue? (y/n): ").lower()
        
        if confirm == 'y':
            rename_items_in_directory(directory)
        else:
            print("Operation cancelled by user.")