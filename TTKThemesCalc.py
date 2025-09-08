import tkinter as tk
from tkinter import ttk
from tkinter.ttk import *
from tkinter import messagebox
import math
try:
    from ttkthemes import ThemedTk, ThemedStyle
except ImportError:
    print("Please install ttkthemes: pip install ttkthemes")
    exit()

class TTKThemesCalculator:
    def __init__(self):
        # Create themed window
        self.window = ThemedTk(theme="arc")  # Options: arc, adapta, equilux, etc.
        self.window.geometry("400x600")
        self.window.resizable(False, False)
        self.window.title("TTK Themes Calculator")
        
        # Initialize variables
        self.current_expression = "0"
        self.total_expression = ""
        
        # Configure styles
        self.setup_styles()
        
        # Create UI
        self.create_widgets()
        self.bind_keys()
        
    def setup_styles(self):
        style = ttk.Style()
        
        # Configure custom styles
        style.configure("Display.TLabel", 
                       font=("Segoe UI", 24, "bold"),
                       foreground="#2c3e50",
                       background="#ecf0f1",
                       anchor="e",
                       padding=(20, 10))
        
        style.configure("History.TLabel",
                       font=("Segoe UI", 12),
                       foreground="#7f8c8d",
                       background="#ecf0f1",
                       anchor="e",
                       padding=(20, 5))
        
        style.configure("Number.TButton",
                       font=("Segoe UI", 16, "bold"),
                       padding=(10, 15))
        
        style.configure("Operator.TButton",
                       font=("Segoe UI", 16, "bold"),
                       padding=(10, 15))
        
        style.configure("Special.TButton",
                       font=("Segoe UI", 16, "bold"),
                       padding=(10, 15))
        
        # Map styles for button states
        style.map("Number.TButton",
                 background=[('active', '#3498db'),
                           ('pressed', '#2980b9')])
        
        style.map("Operator.TButton",
                 background=[('active', '#e74c3c'),
                           ('pressed', '#c0392b')])
        
        style.map("Special.TButton",
                 background=[('active', '#f39c12'),
                           ('pressed', '#e67e22')])
    
    def create_widgets(self):
        # Main container
        main_frame = ttk.Frame(self.window, padding="10")
        main_frame.grid(row=0, column=0, sticky="nsew")
        
        # Display frame
        display_frame = ttk.Frame(main_frame, relief="sunken", borderwidth=2)
        display_frame.grid(row=0, column=0, columnspan=4, sticky="ew", pady=(0, 10))
        
        # History label
        self.history_label = ttk.Label(display_frame, text="", style="History.TLabel")
        self.history_label.grid(row=0, column=0, sticky="ew")
        
        # Main display label
        self.display_label = ttk.Label(display_frame, text="0", style="Display.TLabel")
        self.display_label.grid(row=1, column=0, sticky="ew")
        
        display_frame.columnconfigure(0, weight=1)
        
        # Configure main frame grid
        for i in range(6):
            main_frame.rowconfigure(i+1, weight=1)
        for i in range(4):
            main_frame.columnconfigure(i, weight=1)
        
        # Create buttons
        self.create_buttons(main_frame)
        
        # Configure window grid
        self.window.rowconfigure(0, weight=1)
        self.window.columnconfigure(0, weight=1)
    
    def create_buttons(self, parent):
        # Row 1: Clear, backspace, square, divide
        ttk.Button(parent, text="AC", style="Special.TButton", 
                  command=self.clear_all).grid(row=1, column=0, sticky="nsew", padx=2, pady=2)
        ttk.Button(parent, text="⌫", style="Special.TButton", 
                  command=self.backspace).grid(row=1, column=1, sticky="nsew", padx=2, pady=2)
        ttk.Button(parent, text="x²", style="Operator.TButton", 
                  command=self.square).grid(row=1, column=2, sticky="nsew", padx=2, pady=2)
        ttk.Button(parent, text="÷", style="Operator.TButton", 
                  command=lambda: self.append_operator("/")).grid(row=1, column=3, sticky="nsew", padx=2, pady=2)
        
        # Row 2: 7, 8, 9, multiply
        ttk.Button(parent, text="7", style="Number.TButton", 
                  command=lambda: self.add_to_expression("7")).grid(row=2, column=0, sticky="nsew", padx=2, pady=2)
        ttk.Button(parent, text="8", style="Number.TButton", 
                  command=lambda: self.add_to_expression("8")).grid(row=2, column=1, sticky="nsew", padx=2, pady=2)
        ttk.Button(parent, text="9", style="Number.TButton", 
                  command=lambda: self.add_to_expression("9")).grid(row=2, column=2, sticky="nsew", padx=2, pady=2)
        ttk.Button(parent, text="×", style="Operator.TButton", 
                  command=lambda: self.append_operator("*")).grid(row=2, column=3, sticky="nsew", padx=2, pady=2)
        
        # Row 3: 4, 5, 6, subtract
        ttk.Button(parent, text="4", style="Number.TButton", 
                  command=lambda: self.add_to_expression("4")).grid(row=3, column=0, sticky="nsew", padx=2, pady=2)
        ttk.Button(parent, text="5", style="Number.TButton", 
                  command=lambda: self.add_to_expression("5")).grid(row=3, column=1, sticky="nsew", padx=2, pady=2)
        ttk.Button(parent, text="6", style="Number.TButton", 
                  command=lambda: self.add_to_expression("6")).grid(row=3, column=2, sticky="nsew", padx=2, pady=2)
        ttk.Button(parent, text="−", style="Operator.TButton", 
                  command=lambda: self.append_operator("-")).grid(row=3, column=3, sticky="nsew", padx=2, pady=2)
        
        # Row 4: 1, 2, 3, add
        ttk.Button(parent, text="1", style="Number.TButton", 
                  command=lambda: self.add_to_expression("1")).grid(row=4, column=0, sticky="nsew", padx=2, pady=2)
        ttk.Button(parent, text="2", style="Number.TButton", 
                  command=lambda: self.add_to_expression("2")).grid(row=4, column=1, sticky="nsew", padx=2, pady=2)
        ttk.Button(parent, text="3", style="Number.TButton", 
                  command=lambda: self.add_to_expression("3")).grid(row=4, column=2, sticky="nsew", padx=2, pady=2)
        ttk.Button(parent, text="+", style="Operator.TButton", 
                  command=lambda: self.append_operator("+")).grid(row=4, column=3, sticky="nsew", padx=2, pady=2)
        
        # Row 5: sqrt, 0, decimal, equals
        ttk.Button(parent, text="√", style="Operator.TButton", 
                  command=self.sqrt).grid(row=5, column=0, sticky="nsew", padx=2, pady=2)
        ttk.Button(parent, text="0", style="Number.TButton", 
                  command=lambda: self.add_to_expression("0")).grid(row=5, column=1, sticky="nsew", padx=2, pady=2)
        ttk.Button(parent, text=".", style="Number.TButton", 
                  command=lambda: self.add_to_expression(".")).grid(row=5, column=2, sticky="nsew", padx=2, pady=2)
        ttk.Button(parent, text="=", style="Special.TButton", 
                  command=self.evaluate).grid(row=5, column=3, sticky="nsew", padx=2, pady=2)
    
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
    
    def evaluate(self):
        if self.current_expression:
            self.total_expression += self.current_expression
        
        try:
            result = eval(self.total_expression.replace("×", "*").replace("÷", "/").replace("−", "-"))
            self.current_expression = str(result)
            self.total_expression = ""
            self.update_display()
            self.update_history()
        except:
            self.show_error()
    
    def show_error(self):
        self.current_expression = "Error"
        self.total_expression = ""
        self.update_display()
        self.update_history()
        self.window.after(2000, self.clear_all)
    
    def update_display(self):
        display_text = self.current_expression[:15] if len(self.current_expression) > 15 else self.current_expression
        self.display_label.config(text=display_text)
    
    def update_history(self):
        history_text = self.total_expression.replace("*", "×").replace("/", "÷").replace("-", "−")
        self.history_label.config(text=history_text[-30:])  # Show last 30 chars
    
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
    calc = TTKThemesCalculator()
    calc.run()
