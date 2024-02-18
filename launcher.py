import tkinter as tk
from tkinter import filedialog
import subprocess
import sys
import os

import cv2

import drawMask

root = tk.Tk()

def show_image(image_path):
    img = cv2.imread(image_path)
    # larger_img = cv2.resize(img, None, fx=3, fy=3, interpolation=cv2.INTER_CUBIC)
    cv2.imshow('Image', img)
    cv2.waitKey(0)  # Wait until a key is pressed
    cv2.destroyAllWindows()
def open_file_dialog():
    file_path = filedialog.askopenfilename(
        title="Select a video file", filetypes=[("Video files", "*.mp4")]
    )
    if file_path:
        drawMask.subBack(file_path)
        # Path to the LAMA script in the LAMA project
        lama_script_path = "C:/Users/User/Desktop/lama2try/lama/bin/run_lama.py"
        # Path to the Python interpreter in the LAMA environment
        lama_python_interpreter = "C:/Users/User/AppData/Local/Programs/Python/Python38/python.exe"  # Example path, replace with actual path
        subprocess.run([lama_python_interpreter, lama_script_path])
        show_image("C:/Users/User/Desktop/lama2try/lama/output/img-M_mask.png")
        root.destroy()
        main_script = os.path.join(os.path.dirname(__file__), "main.py")
        subprocess.run([sys.executable, main_script, file_path])
        root.destroy()


# Create a simple GUI
root.title("MSKing Launcher")

def open_dialog():
    button.config(state=tk.DISABLED)
    open_file_dialog()
    button.config(state=tk.DISABLED)

button = tk.Button(root, text="Select Video File", command=open_file_dialog)
button.pack(pady=20)

root.mainloop()
