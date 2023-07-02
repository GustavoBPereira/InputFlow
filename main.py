import tkinter as tk
from tkinter import filedialog
import os

selected_script_path = ""


def select_file():
    global selected_script_path
    selected_script_path = filedialog.askopenfilename()
    update_run_button_state()
    if selected_script_path:
        file_button.config(text=os.path.basename(selected_script_path))


def run_program():
    global selected_script_path


def update_run_button_state():
    if selected_script_path:
        run_button.config(state=tk.NORMAL)
    else:
        run_button.config(state=tk.DISABLED)


window = tk.Tk()
window.title("Input Flow")
window.geometry("473x627")

button_frame = tk.Frame(window)
button_frame.pack(pady=10)

file_button = tk.Button(button_frame, text="Selecionar...", command=select_file)
file_button.pack(side=tk.LEFT, padx=5)

run_button = tk.Button(button_frame, text="Executar", command=run_program, state=tk.DISABLED)
run_button.pack(side=tk.LEFT, padx=5)

window.mainloop()
