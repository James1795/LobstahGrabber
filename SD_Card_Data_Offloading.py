import os
import shutil
from pathlib import Path
import tkinter as tk
from tkinter import filedialog, simpledialog

def select_drive():
    drive_path = filedialog.askdirectory()
    return drive_path

def create_folder_structure(base_path):
    """Creates the required folder structure at the given base path."""
    structure = [
        'DVR',
        'HLR/CLIP',
        'HLR/PICT',
        'HLR/STIL',
        'PRI/CHAP',
        'PRI/CLIP',
        'PRI/PICT',
    ]
    for folder in structure:
        (base_path / folder).mkdir(parents=True, exist_ok=True)

def copy_mp4_files(source_drives, prefixes, target_drive):
    for i, drive in enumerate(source_drives):
        source_path = Path(drive)
        if source_path.exists():
            # Create the target folder named after the prefix (without trailing underscore)
            target_folder_name = prefixes[i].rstrip('_')
            target_folder_path = Path(target_drive) / target_folder_name
            create_folder_structure(target_folder_path)

            # Path to the videos folder
            videos_folder_path = target_folder_path / 'PRI/CHAP'

            for file in source_path.glob('*.mp4'):
                # Construct the target file path with prefix
                target_file_name = f"{prefixes[i]}_{file.name}"
                target_file_path = videos_folder_path / target_file_name
                # Copy the file
                shutil.copy2(file, target_file_path)
                print(f"Copied {file} to {target_file_path}")
        else:
            print(f"Source path {source_path} does not exist. Skipping...")

def main():
    # Initialize Tkinter
    root = tk.Tk()
    root.withdraw()  # Hide the root window

    # Ask for the number of source drives
    num_drives = simpledialog.askinteger("Input", "Enter the number of external drives to copy from:")
    if not num_drives:
        print("Number of drives input canceled. Exiting.")
        return

    # Select source drives and get prefixes
    source_drives = []
    prefixes = []
    for i in range(1, num_drives + 1):
        print(f"Select drive {i}")
        drive = select_drive()
        if drive:
            source_drives.append(drive)
            prefix = simpledialog.askstring("Input", f"Enter the prefix for files from drive {i}:")
            if prefix is not None:
                prefixes.append(prefix)
            else:
                print(f"Prefix input for drive {i} canceled. Exiting.")
                return
        else:
            print(f"Drive {i} selection canceled. Exiting.")
            return

    # Select target drive
    print("Select the target drive")
    target_drive = select_drive()
    if not target_drive:
        print("Target drive selection canceled. Exiting.")
        return

    # Copy mp4 files
    copy_mp4_files(source_drives, prefixes, target_drive)

if __name__ == "__main__":
    main()