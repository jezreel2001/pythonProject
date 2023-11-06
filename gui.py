import tkinter as tk
from tkinter.ttk import *
import subprocess
from tkinter import messagebox
import os
def run_trainer(): #Calling the model trainer
    try:
        subprocess.run(["python", "face_trainer.py"], check=True)
    except subprocess.CalledProcessError as e:
        result_label.config(text=f"Error: {e}")
    else:
        result_label.config(text="Face Trainer Executed Successfully")

def export_img():
    os.system("python img_import.py")
    os.system("python gui.py")


root = tk.Tk()
root.geometry('987x556')
root.resizable(False,False)
title = Label(root, text="Team Omsim")
title.pack()


# Create a button
run_script_button = tk.Button(root, text="Run Face Trainer", width=20, height=2, bg='black',fg="white", command=run_trainer)
run_script_button.place(x=87, y=341)

export_button = tk.Button(root, text="Import Images", width=20, height=2, bg='black',fg="white", command=export_img)
export_button.place(x=387, y=341)

run_system_button = tk.Button(root, text="Start", width=20, height=2,bg='black',fg="white")
run_system_button.place(x=707, y=341)


# Create a label to display the result
result_label = tk.Label(root, text="")
result_label.pack()


root.mainloop()