import tkinter as tk
from tkinter import ttk, scrolledtext
from compiler.comp import Compiler
import threading

class CodeEditorUI:
    def __init__(self, root):
        self.root = root
        self.compiler = Compiler()
        self.language = tk.StringVar(value="Python")
        self.code_memory = {}

        self.setup_ui()
        self.load_code_for_language(self.language.get())

    def setup_ui(self):
        # Language selection
        tk.Label(self.root, text="Language:").pack(pady=5)
        lang_dropdown = ttk.Combobox(self.root, textvariable=self.language, values=["Python", "Java", "C++"])
        lang_dropdown.pack()
        lang_dropdown.bind("<<ComboboxSelected>>", self.switch_language)

        # Code editor
        self.editor = scrolledtext.ScrolledText(self.root, wrap=tk.WORD, font=("Courier", 12))
        self.editor.pack(expand=True, fill=tk.BOTH, padx=10, pady=10)

        # Input box
        tk.Label(self.root, text="Program Input (optional):").pack(pady=5)
        self.input_box = scrolledtext.ScrolledText(self.root, height=5, wrap=tk.WORD)
        self.input_box.pack(expand=False, fill=tk.BOTH, padx=10, pady=5)

        # Buttons
        btn_frame = tk.Frame(self.root)
        btn_frame.pack(pady=5)
        tk.Button(btn_frame, text="Run", command=self.run_code_thread).pack(side=tk.LEFT, padx=5)
        tk.Button(btn_frame, text="Reset", command=lambda: self.load_code_for_language()).pack(side=tk.LEFT, padx=5)

        # Output console
        self.output = scrolledtext.ScrolledText(self.root, height=10, wrap=tk.WORD, font=("Courier", 12))
        self.output.pack(expand=False, fill=tk.BOTH, padx=10, pady=10)
        self.output.config(state=tk.DISABLED)

    # ---------------- Language Switching -----------------
    def switch_language(self, event=None):
        prev_code = self.editor.get(1.0, tk.END)
        self.code_memory[self.language.get()] = prev_code
        self.load_code_for_language(self.language.get())

    def load_code_for_language(self, lang=None):
        lang = lang or self.language.get()
        self.compiler.language = lang
        defaults = {
            "Python": 'print("Hello, World!")',
            "Java": 'public class Main {\n    public static void main(String[] args) {\n        System.out.println("Hello, World!");\n    }\n}',
            "C++": '#include <iostream>\nusing namespace std;\n\nint main() {\n    cout << "Hello, World!" << endl;\n    return 0;\n}'
        }
        code = self.code_memory.get(lang, defaults.get(lang, ""))
        self.editor.delete(1.0, tk.END)
        self.editor.insert(tk.END, code)

    # ---------------- Run Code -----------------
    def run_code_thread(self):
        threading.Thread(target=self.run_code).start()

    def run_code(self):
        code = self.editor.get(1.0, tk.END)
        user_input = self.input_box.get(1.0, tk.END)
        self.output.config(state=tk.NORMAL)
        self.output.delete(1.0, tk.END)
        self.output.insert(tk.END, "Running...")
        self.output.config(state=tk.DISABLED)

        result = self.compiler.run_code(code, user_input)

        self.output.config(state=tk.NORMAL)
        self.output.delete(1.0, tk.END)
        self.output.insert(tk.END, result)
        self.output.config(state=tk.DISABLED)
