import os
import shutil
import time

# Define the folder to monitor and the destination folder
source_folder = "G:\\"
destination_folder = "C:\\krish copy"

# Ensure the destination folder exists
os.makedirs(destination_folder, exist_ok=True)

def copy_files():
    """Copies files from source to destination."""
    for file_name in os.listdir(source_folder):
        source_path = os.path.join(source_folder, file_name)
        destination_path = os.path.join(destination_folder, file_name)
        
        if os.path.isfile(source_path):  # Only copy files, not directories
            shutil.copy2(source_path, destination_path)
            print(f"Copied: {file_name}")

while True:
    if os.path.exists(source_folder):
        print("Folder detected. Copying files...")
        copy_files()
    else:
        print("Source folder not found. Waiting...")
    
    time.sleep(5)  # Check every 5 seconds
