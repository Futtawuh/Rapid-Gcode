import importlib
import subprocess
import tkinter as tk
from tkinter import messagebox

def close_terminal():
    root.destroy()

# Check if requests is installed
try:
    importlib.import_module('requests')
    messagebox.showinfo('Installation Status', 'Requests library is already installed.')
except ImportError:
    messagebox.showinfo('Installation Status', 'Requests library is not found. Installing...')

    # Install requests library using pip
    try:
        subprocess.check_call(['pip', 'install', 'requests'])
        messagebox.showinfo('Installation Status', 'Requests library has been installed successfully.')
    except subprocess.CalledProcessError:
        messagebox.showerror('Installation Status', 'Failed to install Requests library.')

# Create a tkinter root window
root = tk.Tk()
root.withdraw()

# Call the close_terminal function when the OK button is pressed
root.after(0, close_terminal)

# Start the tkinter event loop
root.mainloop()
