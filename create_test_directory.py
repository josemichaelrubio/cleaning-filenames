import os
import shutil
from pathlib import Path

def create_test_directory():
    # Define base test directory
    test_dir = "filename_cleaner_test"
    
    # Remove existing test directory if it exists
    if os.path.exists(test_dir):
        shutil.rmtree(test_dir)
    
    # Create test directory structure with problematic names
    structure = {
        "My Documents!": {
            "file (1).txt": "Test content 1",
            "file (2).txt": "Test content 2",
            "test-file@123.doc": "Test content 3"
        },
        "Program Files@": {
            "app_1.0.2 (beta).exe": "Test content 4",
            "install-notes.txt": "Test content 5"
        },
        "Data & Settings": {
            "user.config": "Test content 6",
            "backup (old)": {
                "data#1.bak": "Test content 7",
                "data#2.bak": "Test content 8"
            }
        },
        "Test Files (Duplicate Names)": {
            "my-file.txt": "Content 1",
            "my_file.txt": "Content 2",
            "my file.txt": "Content 3"
        },
        "Special & Chars": {
            "file@#$%.txt": "Special chars test",
            "unicode_τεστ.dat": "Unicode test",
            "spaces   test.txt": "Multiple spaces test",
            "  leading spaces.txt": "Leading spaces test",
            "trailing spaces  .txt": "Trailing spaces test",
            "  both ends  .txt": "Both ends spaces test"
        }
    }
    
    try:
        # Create the main test directory
        os.makedirs(test_dir)
        
        # Create the directory structure
        for dir_name, contents in structure.items():
            dir_path = os.path.join(test_dir, dir_name)
            os.makedirs(dir_path, exist_ok=True)
            
            # Create files and subdirectories
            for item_name, content in contents.items():
                item_path = os.path.join(dir_path, item_name)
                
                if isinstance(content, dict):
                    # If content is a dict, it's a subdirectory
                    os.makedirs(item_path, exist_ok=True)
                    for sub_name, sub_content in content.items():
                        sub_path = os.path.join(item_path, sub_name)
                        with open(sub_path, 'w', encoding='utf-8') as f:
                            f.write(sub_content)
                else:
                    # It's a file
                    with open(item_path, 'w', encoding='utf-8') as f:
                        f.write(content)
        
        print(f"\nTest directory '{test_dir}' created successfully!")
        print("\nDirectory structure created:")
        
        # Print the directory structure
        for root, dirs, files in os.walk(test_dir):
            level = root.replace(test_dir, '').count(os.sep)
            indent = '  ' * level
            print(f"{indent}{os.path.basename(root)}/")
            subindent = '  ' * (level + 1)
            for f in files:
                print(f"{subindent}{f}")
                
        print("\nYou can now test the filename cleaner script on this directory:")
        print(f"  {os.path.abspath(test_dir)}")
        
    except Exception as e:
        print(f"Error creating test directory: {str(e)}")

if __name__ == "__main__":
    create_test_directory()