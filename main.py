from tkinter import Tk, Button
from ui.editor import CodeEditorUI

def main():
    root = Tk()
    root.title("Multi-Language Code Editor")
    root.geometry("900x700")

    app = CodeEditorUI(root)

    # Add a button in main.py to print the last terminal output
    def print_last_output():
        output = app.get_last_output()
        print("=== Last Terminal Output ===")
        print(output)
        print("============================")

    # Optional: add a button in the GUI to print it
    Button(root, text="Print Last Output", command=print_last_output).pack(pady=5)

    root.mainloop()

if __name__ == "__main__":
    main()
