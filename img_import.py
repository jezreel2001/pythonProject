import tkinter as tk
from tkinter.ttk import *
import os
import shutil
from tkinter import filedialog

def pick_folder():
    global selected_folder
    selected_folder = filedialog.askdirectory(title="Select a Folder")
    if selected_folder:
        selected_folder_label.config(text=f"Selected Folder: {selected_folder}")
    else:
        selected_folder_label.config(text="Folder selection canceled")

def save_folder():
    if selected_folder:
        folder_name = folder_name_entry.get().strip()
        if not folder_name:
            result_label.config(text="Please enter a folder name")
            return

        # Define the destination folder path here
        destination_folder = "C:/Users/pc/PycharmProjects/pythonProject/image_data"  # Change this to your desired destination

        new_folder_path = os.path.join(destination_folder, folder_name)

        try:
            os.mkdir(new_folder_path)
            shutil.copytree(selected_folder, new_folder_path)
            result_label.config(text=f"Folder saved to: {new_folder_path}")
        except Exception as e:
            result_label.config(text=f"Error: {str(e)}")
    else:
        result_label.config(text="Please select a folder to save")

root = tk.Tk()
root.geometry('400x300')
root.title("Folder Picker and Saver")

# Create button to pick a folder
pick_folder_button = tk.Button(root, text="Pick a Folder", command=pick_folder)
pick_folder_button.pack(pady=10)

# Label to display the selected folder
selected_folder_label = tk.Label(root, text="")
selected_folder_label.pack()

# Entry to enter folder name
folder_name_label = tk.Label(root, text="Enter Your Name")
folder_name_label.pack()

folder_name_entry = tk.Entry(root)
folder_name_entry.pack()

# Create button to save the folder
save_button = tk.Button(root, text="Save", command=save_folder)
save_button.pack(pady=10)

# Label to display the result
result_label = tk.Label(root, text="")
result_label.pack()

root.mainloop()
