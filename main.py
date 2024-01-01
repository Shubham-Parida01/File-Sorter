import os
import shutil
import tkinter as tk
from tkinter import filedialog, ttk

def sort_files(source_folder):
    files = os.listdir(source_folder)
    total_files = len(files)

    # Set up the tkinter window
    root = tk.Tk()
    root.withdraw()  # Hide the main window

    destination_folder = filedialog.askdirectory(title="Select Destination Folder")

    if not destination_folder:
        print("Sorting canceled.")
        return

    # Create folders for different file types
    folders = {}

    for file_name in files:
        _, file_extension = os.path.splitext(file_name)
        file_extension = file_extension.lower()

        if file_extension not in folders:
            folders[file_extension] = os.path.join(destination_folder, file_extension[1:])

    for folder in folders.values():
        os.makedirs(folder, exist_ok=True)

    # Set up the tkinter window for progress bar
    progress_label = ttk.Label(root, text="Sorting Files:")
    progress_label.pack(pady=10)

    progress_bar = ttk.Progressbar(root, length=300, mode="determinate", maximum=total_files)
    progress_bar.pack(pady=10)

    # Sort files and update progress bar
    for i, file_name in enumerate(files, 1):
        file_path = os.path.join(source_folder, file_name)

        # Determine the file type based on extension
        _, file_extension = os.path.splitext(file_name)
        file_extension = file_extension.lower()

        destination_folder = folders.get(file_extension, os.path.join(destination_folder, "Others"))

        destination_path = os.path.join(destination_folder, file_name)

        # Move the file to the destination folder
        shutil.move(file_path, destination_path)

        # Update progress bar
        progress_bar['value'] = i
        root.update()

    progress_label.config(text="Sorting Completed!")
    root.mainloop()

# Example usage:
source_folder = filedialog.askdirectory(title="Select Source Folder")
if source_folder:
    sort_files(source_folder)
