# This is a sample Python script.
import os
import sys
import drawMask


# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    if getattr(sys, 'frozen', False) and hasattr(sys, '_MEIPASS'):
        base_path = sys._MEIPASS
    else:
        base_path = os.path.dirname(os.path.abspath(__file__))

    os.chdir(base_path)
    print("Current working directory:", os.getcwd())
    print("Executable path:", sys.executable)


    drawMask.open_file_dialog()
    # path="C:/Users/Win10-01/Desktop/masKingPro/realyShort.mp4"
    # drawMask.subBack(path)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
