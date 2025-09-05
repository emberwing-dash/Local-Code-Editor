from tkinter import Tk
from ui.editor import CodeEditorUI

def main():
    root = Tk()
    root.title("Multi-Language Code Editor")
    root.geometry("900x700")
    app = CodeEditorUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()
