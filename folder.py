import tkinter as tk
from tkinter import filedialog, messagebox
import os

def select_source_folder():
    global source_folder
    folder = filedialog.askdirectory(title='Select Source Folder')
    if folder:
        source_folder = folder
        source_label.config(text=f"Source Folder: {source_folder}")

def select_destination_folder():
    global destination_folder
    folder = filedialog.askdirectory(title='Select Destination Folder')
    if folder:
        destination_folder = folder
        destination_label.config(text=f"Destination Folder: {destination_folder}")

def duplicate_folder_structure():
    if not source_folder or not destination_folder:
        messagebox.showerror("Error", "Please select both source and destination folders.")
        return
    try:
        max_depth = int(depth_entry.get())
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid integer for depth.")
        return
    for root_dir, dirs, _ in os.walk(source_folder):
        # Calculate the depth
        relative_path = os.path.relpath(root_dir, source_folder)
        current_depth = relative_path.count(os.sep)
        if max_depth > 0 and current_depth >= max_depth:
            # Skip deeper directories
            dirs[:] = []
            continue
        # Recreate the directory structure in destination
        dest_dir = os.path.join(destination_folder, relative_path)
        os.makedirs(dest_dir, exist_ok=True)
    messagebox.showinfo("Success", "Folder structure duplicated successfully.")

# Initialize the main window
root = tk.Tk()
root.title("Folder Structure Duplicator")

source_folder = ''
destination_folder = ''

# Source folder selection
source_button = tk.Button(root, text="Select Source Folder", command=select_source_folder)
source_button.pack(pady=5)
source_label = tk.Label(root, text="Source Folder: Not selected")
source_label.pack()

# Destination folder selection
destination_button = tk.Button(root, text="Select Destination Folder", command=select_destination_folder)
destination_button.pack(pady=5)
destination_label = tk.Label(root, text="Destination Folder: Not selected")
destination_label.pack()

# Depth selection
depth_label = tk.Label(root, text="Max Depth (0 for unlimited):")
depth_label.pack()
depth_entry = tk.Entry(root)
depth_entry.insert(0, "0")
depth_entry.pack()

# Start duplication button
start_button = tk.Button(root, text="Start Duplication", command=duplicate_folder_structure)
start_button.pack(pady=10)

root.mainloop()
