import os
import shutil
import tkinter as tk
from tkinter import filedialog, ttk

def reverse_sort(destination_folder):
    folders = os.listdir(destination_folder)

    # Set up the tkinter window
    root = tk.Tk()
    root.withdraw()  # Hide the main window

    source_folder = filedialog.askdirectory(title="Select Source Folder")

    if not source_folder:
        print("Reverse sorting canceled.")
        return

    # Set up the tkinter window for progress bar
    progress_label = ttk.Label(root, text="Reversing Sorting:")
    progress_label.pack(pady=10)

    progress_bar = ttk.Progressbar(root, length=300, mode="determinate", maximum=len(folders))
    progress_bar.pack(pady=10)

    # Reverse sort folders and update progress bar
    for i, folder_name in enumerate(folders, 1):
        folder_path = os.path.join(destination_folder, folder_name)

        # Get files in the folder
        files = os.listdir(folder_path)

        # Move files back to the source folder
        for file_name in files:
            file_path = os.path.join(folder_path, file_name)
            destination_path = os.path.join(source_folder, file_name)

            # Move the file back to the source folder
            shutil.move(file_path, destination_path)

        # Remove the now-empty folder
        os.rmdir(folder_path)

        # Update progress bar
        progress_bar['value'] = i
        root.update()

    progress_label.config(text="Reverse Sorting Completed!")
    root.mainloop()

# Example usage:
destination_folder = filedialog.askdirectory(title="Select Destination Folder for Reverse Sorting")
if destination_folder:
    reverse_sort(destination_folder)
