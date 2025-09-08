import tkinter as tk
from tkinter import messagebox
import math
try:
    import ttkbootstrap as ttk
    from ttkbootstrap.constants import *
except ImportError:
    print("Please install ttkbootstrap: pip install ttkbootstrap")
    exit()

class TTKBootstrapCalculator:
    def __init__(self):
        # Create bootstrap styled window
        self.window = ttk.Window(themename="darkly")  # Options: flatly, darkly, cosmo, etc.
        self.window.geometry("450x650")
        self.window.resizable(False, False)
        self.window.title("Bootstrap Calculator")
        
        # Initialize variables
        self.current_expression = "0"
        self.total_expression = ""
        
        # Create UI
        self.create_widgets()
        self.bind_keys()
        
    def create_widgets(self):
        # Main container with padding
        main_frame = ttk.Frame(self.window, padding=20)
        main_frame.pack(fill=BOTH, expand=True)
        
        # Display frame with card styling
        display_frame = ttk.Frame(main_frame, bootstyle="dark", padding=15)
        display_frame.pack(fill=X, pady=(0, 20))
        
        # History display
        self.history_label = ttk.Label(
            display_frame, 
            text="", 
            font=("Segoe UI", 14),
            bootstyle="secondary",
            anchor="e"
        )
        self.history_label.pack(fill=X)
        
        # Main display
        self.display_label = ttk.Label(
            display_frame, 
            text="0", 
            font=("Segoe UI", 36, "bold"),
            bootstyle="light",
            anchor="e"
        )
        self.display_label.pack(fill=X, pady=(10, 0))
        
        # Buttons frame
        buttons_frame = ttk.Frame(main_frame)
        buttons_frame.pack(fill=BOTH, expand=True)
        
        # Configure grid
        for i in range(6):
            buttons_frame.rowconfigure(i, weight=1)
        for i in range(4):
            buttons_frame.columnconfigure(i, weight=1)
        
        # Create buttons with Bootstrap styling
        self.create_buttons(buttons_frame)
    
    def create_buttons(self, parent):
        btn_config = {"width": 8, "padding": (10, 15)}
        
        # Row 0: Clear, backspace, square, divide
        ttk.Button(parent, text="AC", bootstyle="danger", command=self.clear_all, **btn_config).grid(
            row=0, column=0, sticky="nsew", padx=2, pady=2)
        ttk.Button(parent, text="⌫", bootstyle="warning", command=self.backspace, **btn_config).grid(
            row=0, column=1, sticky="nsew", padx=2, pady=2)
        ttk.Button(parent, text="x²", bootstyle="info", command=self.square, **btn_config).grid(
            row=0, column=2, sticky="nsew", padx=2, pady=2)
        ttk.Button(parent, text="÷", bootstyle="info", command=lambda: self.append_operator("/"), **btn_config).grid(
            row=0, column=3, sticky="nsew", padx=2, pady=2)
        
        # Row 1: 7, 8, 9, multiply
        ttk.Button(parent, text="7", bootstyle="secondary", command=lambda: self.add_to_expression("7"), **btn_config).grid(
            row=1, column=0, sticky="nsew", padx=2, pady=2)
        ttk.Button(parent, text="8", bootstyle="secondary", command=lambda: self.add_to_expression("8"), **btn_config).grid(
            row=1, column=1, sticky="nsew", padx=2, pady=2)
        ttk.Button(parent, text="9", bootstyle="secondary", command=lambda: self.add_to_expression("9"), **btn_config).grid(
            row=1, column=2, sticky="nsew", padx=2, pady=2)
        ttk.Button(parent, text="×", bootstyle="info", command=lambda: self.append_operator("*"), **btn_config).grid(
            row=1, column=3, sticky="nsew", padx=2, pady=2)
        
        # Row 2: 4, 5, 6, subtract
        ttk.Button(parent, text="4", bootstyle="secondary", command=lambda: self.add_to_expression("4"), **btn_config).grid(
            row=2, column=0, sticky="nsew", padx=2, pady=2)
        ttk.Button(parent, text="5", bootstyle="secondary", command=lambda: self.add_to_expression("5"), **btn_config).grid(
            row=2, column=1, sticky="nsew", padx=2, pady=2)
        ttk.Button(parent, text="6", bootstyle="secondary", command=lambda: self.add_to_expression("6"), **btn_config).grid(
            row=2, column=2, sticky="nsew", padx=2, pady=2)
        ttk.Button(parent, text="−", bootstyle="info", command=lambda: self.append_operator("-"), **btn_config).grid(
            row=2, column=3, sticky="nsew", padx=2, pady=2)
        
        # Row 3: 1, 2, 3, add
        ttk.Button(parent, text="1", bootstyle="secondary", command=lambda: self.add_to_expression("1"), **btn_config).grid(
            row=3, column=0, sticky="nsew", padx=2, pady=2)
        ttk.Button(parent, text="2", bootstyle="secondary", command=lambda: self.add_to_expression("2"), **btn_config).grid(
            row=3, column=1, sticky="nsew", padx=2, pady=2)
        ttk.Button(parent, text="3", bootstyle="secondary", command=lambda: self.add_to_expression("3"), **btn_config).grid(
            row=3, column=2, sticky="nsew", padx=2, pady=2)
        ttk.Button(parent, text="+", bootstyle="info", command=lambda: self.append_operator("+"), **btn_config).grid(
            row=3, column=3, sticky="nsew", padx=2, pady=2)
        
        # Row 4: special functions and 0
        ttk.Button(parent, text="√", bootstyle="info", command=self.sqrt, **btn_config).grid(
            row=4, column=0, sticky="nsew", padx=2, pady=2)
        ttk.Button(parent, text="0", bootstyle="secondary", command=lambda: self.add_to_expression("0"), **btn_config).grid(
            row=4, column=1, sticky="nsew", padx=2, pady=2)
        ttk.Button(parent, text=".", bootstyle="secondary", command=lambda: self.add_to_expression("."), **btn_config).grid(
            row=4, column=2, sticky="nsew", padx=2, pady=2)
        ttk.Button(parent, text="=", bootstyle="success", command=self.evaluate, **btn_config).grid(
            row=4, column=3, sticky="nsew", padx=2, pady=2)
        
        # Row 5: Additional functions
        ttk.Button(parent, text="π", bootstyle="info", command=lambda: self.add_to_expression(str(math.pi)), **btn_config).grid(
            row=5, column=0, sticky="nsew", padx=2, pady=2)
        ttk.Button(parent, text="e", bootstyle="info", command=lambda: self.add_to_expression(str(math.e)), **btn_config).grid(
            row=5, column=1, sticky="nsew", padx=2, pady=2)
        ttk.Button(parent, text="log", bootstyle="info", command=self.log, **btn_config).grid(
            row=5, column=2, sticky="nsew", padx=2, pady=2)
        ttk.Button(parent, text="±", bootstyle="info", command=self.toggle_sign, **btn_config).grid(
            row=5, column=3, sticky="nsew", padx=2, pady=2)
    
    def add_to_expression(self, value):
        if self.current_expression == "0" or self.current_expression == "Error":
            self.current_expression = str(value)
        else:
            self.current_expression += str(value)
        self.update_display()
    
    def append_operator(self, operator):
        if self.current_expression:
            self.total_expression += self.current_expression + operator
            self.current_expression = ""
            self.update_history()
            self.display_label.config(text="0")
    
    def clear_all(self):
        self.current_expression = "0"
        self.total_expression = ""
        self.update_display()
        self.update_history()
    
    def backspace(self):
        if len(self.current_expression) > 1:
            self.current_expression = self.current_expression[:-1]
        else:
            self.current_expression = "0"
        self.update_display()
    
    def square(self):
        try:
            result = float(self.current_expression) ** 2
            self.current_expression = str(result)
            self.update_display()
        except:
            self.show_error()
    
    def sqrt(self):
        try:
            result = math.sqrt(float(self.current_expression))
            self.current_expression = str(result)
            self.update_display()
        except:
            self.show_error()
    
    def log(self):
        try:
            result = math.log10(float(self.current_expression))
            self.current_expression = str(result)
            self.update_display()
        except:
            self.show_error()
    
    def toggle_sign(self):
        if self.current_expression and self.current_expression != "0":
            if self.current_expression.startswith("-"):
                self.current_expression = self.current_expression[1:]
            else:
                self.current_expression = "-" + self.current_expression
            self.update_display()
    
    def evaluate(self):
        if self.current_expression:
            self.total_expression += self.current_expression
        
        try:
            result = eval(self.total_expression.replace("×", "*").replace("÷", "/").replace("−", "-"))
            self.current_expression = str(result)
            self.total_expression = ""
            self.update_display()
            self.update_history()
            
            # Show success animation by temporarily changing button style
            self.window.after(100, lambda: self.flash_success())
        except:
            self.show_error()
    
    def flash_success(self):
        # Simple success indication
        original_text = self.display_label.cget("text")
        self.display_label.config(bootstyle="success")
        self.window.after(300, lambda: self.display_label.config(bootstyle="light"))
    
    def show_error(self):
        self.current_expression = "Error"
        self.total_expression = ""
        self.display_label.config(bootstyle="danger")
        self.update_display()
        self.update_history()
        self.window.after(2000, lambda: (
            self.clear_all(),
            self.display_label.config(bootstyle="light")
        ))
    
    def update_display(self):
        display_text = self.current_expression[:20] if len(self.current_expression) > 20 else self.current_expression
        self.display_label.config(text=display_text)
    
    def update_history(self):
        history_text = self.total_expression.replace("*", "×").replace("/", "÷").replace("-", "−")
        self.history_label.config(text=history_text[-40:])  # Show last 40 chars
    
    def bind_keys(self):
        self.window.bind("<Return>", lambda e: self.evaluate())
        self.window.bind("<BackSpace>", lambda e: self.backspace())
        self.window.bind("<Escape>", lambda e: self.clear_all())
        
        # Number keys
        for i in range(10):
            self.window.bind(str(i), lambda e, digit=str(i): self.add_to_expression(digit))
        
        # Operator keys
        self.window.bind("+", lambda e: self.append_operator("+"))
        self.window.bind("-", lambda e: self.append_operator("-"))
        self.window.bind("*", lambda e: self.append_operator("*"))
        self.window.bind("/", lambda e: self.append_operator("/"))
        self.window.bind(".", lambda e: self.add_to_expression("."))
    
    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    calc = TTKBootstrapCalculator()
    calc.run()
