import os
import shutil
import tkinter as tk
from tkinter import filedialog, messagebox


APP_NAME = "007 FirstLight Ultrawide Cutscenes Fix"


def select_folder():
    folder = filedialog.askdirectory(title="Select 007 First Light game folder")
    if folder:
        path_entry.delete(0, tk.END)
        path_entry.insert(0, folder)


def install_fix():
    game_path = path_entry.get().strip()

    if not game_path:
        messagebox.showerror("Error", "Please select the game folder.")
        return

    if not os.path.exists(game_path):
        messagebox.showerror("Error", "Selected folder does not exist.")
        return

    source_folder = os.path.join(os.getcwd(), "files")

    if not os.path.exists(source_folder):
        messagebox.showerror("Error", "Fix files folder not found.")
        return

    try:
        for item in os.listdir(source_folder):
            source = os.path.join(source_folder, item)
            destination = os.path.join(game_path, item)

            if os.path.isdir(source):
                shutil.copytree(source, destination, dirs_exist_ok=True)
            else:
                shutil.copy2(source, destination)

        messagebox.showinfo("Success", "Ultrawide fix installed successfully!")

    except Exception as e:
        messagebox.showerror("Installation Error", str(e))


root = tk.Tk()
root.title(APP_NAME)
root.geometry("560x260")
root.resizable(False, False)

title = tk.Label(
    root,
    text=APP_NAME,
    font=("Segoe UI", 16, "bold")
)
title.pack(pady=15)

subtitle = tk.Label(
    root,
    text="Removes black bars and improves ultrawide cutscenes support.",
    font=("Segoe UI", 10)
)
subtitle.pack(pady=5)

frame = tk.Frame(root)
frame.pack(pady=20)

path_entry = tk.Entry(frame, width=55)
path_entry.pack(side=tk.LEFT, padx=5)

browse_button = tk.Button(frame, text="Browse", command=select_folder)
browse_button.pack(side=tk.LEFT)

install_button = tk.Button(
    root,
    text="Install Fix",
    font=("Segoe UI", 11, "bold"),
    width=20,
    command=install_fix
)
install_button.pack(pady=10)

footer = tk.Label(
    root,
    text="Download latest version from GitHub Releases",
    font=("Segoe UI", 8)
)
footer.pack(side=tk.BOTTOM, pady=10)

root.mainloop()
