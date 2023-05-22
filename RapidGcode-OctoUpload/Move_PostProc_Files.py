import os
import getpass
import shutil
import tkinter as tk
from tkinter import messagebox

# Define the source directory and files to be moved
source_dir = os.getcwd()  # Assuming the files are in the current working directory
files_to_move = ["MPCNC Klipper Fusion 360.cps", "MPCNC Klipper Fusion 360.mch", "Klipper.js"]

# Get the username of the logged-in user
username = getpass.getuser()

# Define the destination directory
destination_dir = f"C:\\Users\\{username}\\AppData\\Roaming\\Autodesk\\Fusion 360 CAM\\Posts"

# Move the files to the destination directory
moved_files = []
for file in files_to_move:
    source_path = os.path.join(source_dir, file)
    destination_path = os.path.join(destination_dir, file)

    # Create the destination directory if it doesn't exist
    os.makedirs(destination_dir, exist_ok=True)

    try:
        shutil.move(source_path, destination_path)
        moved_files.append(f"{file} to {destination_path}")
    except Exception as e:
        print(f"Error moving {file}: {str(e)}")

# Display a popup window with the message
message = "Klipper Post Processor files for Fusion move to post proc. folder. You can find it in the Post library in Fusion 360."
messagebox.showinfo("Files Moved", message)

# Terminate the script
raise SystemExit
