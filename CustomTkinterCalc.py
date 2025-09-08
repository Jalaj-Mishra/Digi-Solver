import math
try:
    import customtkinter as ctk
    from customtkinter import *
except ImportError:
    print("Please install customtkinter: pip install customtkinter")
    exit()

class CustomTkinterCalculator:
    def __init__(self):
        # Set appearance mode and color theme
        ctk.set_appearance_mode("dark")  # Options: "dark", "light", "system"
        ctk.set_default_color_theme("blue")  # Options: "blue", "green", "dark-blue"
        
        # Create main window
        self.window = ctk.CTk()
        self.window.geometry("420x700")
        self.window.resizable(False, False)
        self.window.title("CustomTkinter Calculator")
        
        # Initialize variables
        self.current_expression = "0"
        self.total_expression = ""
        
        # Create UI
        self.create_widgets()
        self.bind_keys()
        
    def create_widgets(self):
        # Main container
        main_frame = ctk.CTkFrame(self.window, corner_radius=20)
        main_frame.pack(fill="both", expand=True, padx=20, pady=20)
        
        # Title label
        title_label = ctk.CTkLabel(
            main_frame, 
            text="Calculator Pro", 
            font=ctk.CTkFont(size=24, weight="bold"),
            text_color=("#1f538d", "#14375e")
        )
        title_label.pack(pady=(20, 10))
        
        # Display frame
        display_frame = ctk.CTkFrame(main_frame, corner_radius=15, fg_color=("gray90", "gray13"))
        display_frame.pack(fill="x", padx=20, pady=(0, 20))
        
        # History display
        self.history_label = ctk.CTkLabel(
            display_frame,
            text="",
            font=ctk.CTkFont(size=16),
            text_color=("gray50", "gray70"),
            anchor="e"
        )
        self.history_label.pack(fill="x", padx=20, pady=(15, 0))
        
        # Main display
        self.display_label = ctk.CTkLabel(
            display_frame,
            text="0",
            font=ctk.CTkFont(size=42, weight="bold"),
            text_color=("gray10", "gray90"),
            anchor="e"
        )
        self.display_label.pack(fill="x", padx=20, pady=(5, 20))
        
        # Buttons frame
        buttons_frame = ctk.CTkFrame(main_frame, fg_color="transparent")
        buttons_frame.pack(fill="both", expand=True, padx=20, pady=(0, 20))
        
        # Configure grid
        for i in range(6):
            buttons_frame.grid_rowconfigure(i, weight=1)
        for i in range(4):
            buttons_frame.grid_columnconfigure(i, weight=1)
        
        # Create buttons
        self.create_buttons(buttons_frame)
    
    def create_buttons(self, parent):
        # Button configuration
        btn_width = 80
        btn_height = 60
        btn_font = ctk.CTkFont(size=20, weight="bold")
        
        # Row 0: Clear, backspace, square, divide
        ctk.CTkButton(parent, text="AC", width=btn_width, height=btn_height, font=btn_font,
                     fg_color=("#dc2626", "#b91c1c"), hover_color=("#b91c1c", "#991b1b"),
                     command=self.clear_all).grid(row=0, column=0, padx=5, pady=5, sticky="nsew")
        
        ctk.CTkButton(parent, text="⌫", width=btn_width, height=btn_height, font=btn_font,
                     fg_color=("#ea580c", "#c2410c"), hover_color=("#c2410c", "#9a3412"),
                     command=self.backspace).grid(row=0, column=1, padx=5, pady=5, sticky="nsew")
        
        ctk.CTkButton(parent, text="x²", width=btn_width, height=btn_height, font=btn_font,
                     fg_color=("#7c3aed", "#6d28d9"), hover_color=("#6d28d9", "#5b21b6"),
                     command=self.square).grid(row=0, column=2, padx=5, pady=5, sticky="nsew")
        
        ctk.CTkButton(parent, text="÷", width=btn_width, height=btn_height, font=btn_font,
                     fg_color=("#7c3aed", "#6d28d9"), hover_color=("#6d28d9", "#5b21b6"),
                     command=lambda: self.append_operator("/")).grid(row=0, column=3, padx=5, pady=5, sticky="nsew")
        
        # Row 1: 7, 8, 9, multiply
        ctk.CTkButton(parent, text="7", width=btn_width, height=btn_height, font=btn_font,
                     fg_color=("#374151", "#4b5563"), hover_color=("#4b5563", "#6b7280"),
                     command=lambda: self.add_to_expression("7")).grid(row=1, column=0, padx=5, pady=5, sticky="nsew")
        
        ctk.CTkButton(parent, text="8", width=btn_width, height=btn_height, font=btn_font,
                     fg_color=("#374151", "#4b5563"), hover_color=("#4b5563", "#6b7280"),
                     command=lambda: self.add_to_expression("8")).grid(row=1, column=1, padx=5, pady=5, sticky="nsew")
        
        ctk.CTkButton(parent, text="9", width=btn_width, height=btn_height, font=btn_font,
                     fg_color=("#374151", "#4b5563"), hover_color=("#4b5563", "#6b7280"),
                     command=lambda: self.add_to_expression("9")).grid(row=1, column=2, padx=5, pady=5, sticky="nsew")
        
        ctk.CTkButton(parent, text="×", width=btn_width, height=btn_height, font=btn_font,
                     fg_color=("#7c3aed", "#6d28d9"), hover_color=("#6d28d9", "#5b21b6"),
                     command=lambda: self.append_operator("*")).grid(row=1, column=3, padx=5, pady=5, sticky="nsew")
        
        # Row 2: 4, 5, 6, subtract
        ctk.CTkButton(parent, text="4", width=btn_width, height=btn_height, font=btn_font,
                     fg_color=("#374151", "#4b5563"), hover_color=("#4b5563", "#6b7280"),
                     command=lambda: self.add_to_expression("4")).grid(row=2, column=0, padx=5, pady=5, sticky="nsew")
        
        ctk.CTkButton(parent, text="5", width=btn_width, height=btn_height, font=btn_font,
                     fg_color=("#374151", "#4b5563"), hover_color=("#4b5563", "#6b7280"),
                     command=lambda: self.add_to_expression("5")).grid(row=2, column=1, padx=5, pady=5, sticky="nsew")
        
        ctk.CTkButton(parent, text="6", width=btn_width, height=btn_height, font=btn_font,
                     fg_color=("#374151", "#4b5563"), hover_color=("#4b5563", "#6b7280"),
                     command=lambda: self.add_to_expression("6")).grid(row=2, column=2, padx=5, pady=5, sticky="nsew")
        
        ctk.CTkButton(parent, text="−", width=btn_width, height=btn_height, font=btn_font,
                     fg_color=("#7c3aed", "#6d28d9"), hover_color=("#6d28d9", "#5b21b6"),
                     command=lambda: self.append_operator("-")).grid(row=2, column=3, padx=5, pady=5, sticky="nsew")
        
        # Row 3: 1, 2, 3, add
        ctk.CTkButton(parent, text="1", width=btn_width, height=btn_height, font=btn_font,
                     fg_color=("#374151", "#4b5563"), hover_color=("#4b5563", "#6b7280"),
                     command=lambda: self.add_to_expression("1")).grid(row=3, column=0, padx=5, pady=5, sticky="nsew")
        
        ctk.CTkButton(parent, text="2", width=btn_width, height=btn_height, font=btn_font,
                     fg_color=("#374151", "#4b5563"), hover_color=("#4b5563", "#6b7280"),
                     command=lambda: self.add_to_expression("2")).grid(row=3, column=1, padx=5, pady=5, sticky="nsew")
        
        ctk.CTkButton(parent, text="3", width=btn_width, height=btn_height, font=btn_font,
                     fg_color=("#374151", "#4b5563"), hover_color=("#4b5563", "#6b7280"),
                     command=lambda: self.add_to_expression("3")).grid(row=3, column=2, padx=5, pady=5, sticky="nsew")
        
        ctk.CTkButton(parent, text="+", width=btn_width, height=btn_height, font=btn_font,
                     fg_color=("#7c3aed", "#6d28d9"), hover_color=("#6d28d9", "#5b21b6"),
                     command=lambda: self.append_operator("+")).grid(row=3, column=3, padx=5, pady=5, sticky="nsew")
        
        # Row 4: Special functions and 0
        ctk.CTkButton(parent, text="√", width=btn_width, height=btn_height, font=btn_font,
                     fg_color=("#059669", "#047857"), hover_color=("#047857", "#065f46"),
                     command=self.sqrt).grid(row=4, column=0, padx=5, pady=5, sticky="nsew")
        
        ctk.CTkButton(parent, text="0", width=btn_width, height=btn_height, font=btn_font,
                     fg_color=("#374151", "#4b5563"), hover_color=("#4b5563", "#6b7280"),
                     command=lambda: self.add_to_expression("0")).grid(row=4, column=1, padx=5, pady=5, sticky="nsew")
        
        ctk.CTkButton(parent, text=".", width=btn_width, height=btn_height, font=btn_font,
                     fg_color=("#374151", "#4b5563"), hover_color=("#4b5563", "#6b7280"),
                     command=lambda: self.add_to_expression(".")).grid(row=4, column=2, padx=5, pady=5, sticky="nsew")
        
        ctk.CTkButton(parent, text="=", width=btn_width, height=btn_height, font=btn_font,
                     fg_color=("#059669", "#047857"), hover_color=("#047857", "#065f46"),
                     command=self.evaluate).grid(row=4, column=3, padx=5, pady=5, sticky="nsew")
        
        # Row 5: Advanced functions
        ctk.CTkButton(parent, text="π", width=btn_width, height=btn_height, font=btn_font,
                     fg_color=("#0891b2", "#0e7490"), hover_color=("#0e7490", "#155e75"),
                     command=lambda: self.add_to_expression(str(round(math.pi, 8)))).grid(row=5, column=0, padx=5, pady=5, sticky="nsew")
        
        ctk.CTkButton(parent, text="e", width=btn_width, height=btn_height, font=btn_font,
                     fg_color=("#0891b2", "#0e7490"), hover_color=("#0e7490", "#155e75"),
                     command=lambda: self.add_to_expression(str(round(math.e, 8)))).grid(row=5, column=1, padx=5, pady=5, sticky="nsew")
        
        ctk.CTkButton(parent, text="log", width=btn_width, height=btn_height, font=btn_font,
                     fg_color=("#0891b2", "#0e7490"), hover_color=("#0e7490", "#155e75"),
                     command=self.log).grid(row=5, column=2, padx=5, pady=5, sticky="nsew")
        
        ctk.CTkButton(parent, text="±", width=btn_width, height=btn_height, font=btn_font,
                     fg_color=("#0891b2", "#0e7490"), hover_color=("#0e7490", "#155e75"),
                     command=self.toggle_sign).grid(row=5, column=3, padx=5, pady=5, sticky="nsew")
    
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
            self.display_label.configure(text="0")
    
    def clear_all(self):
        self.current_expression = "0"
        self.total_expression = ""
        self.update_display()
        self.update_history()
        self.display_label.configure(text_color=("gray10", "gray90"))
    
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
            
            # Success animation
            self.display_label.configure(text_color=("#047857", "#10b981"))
            self.window.after(500, lambda: self.display_label.configure(text_color=("gray10", "gray90")))
            
            self.update_display()
            self.update_history()
        except:
            self.show_error()
    
    def show_error(self):
        self.current_expression = "Error"
        self.total_expression = ""
        self.display_label.configure(text_color=("#dc2626", "#ef4444"))
        self.update_display()
        self.update_history()
        self.window.after(2000, lambda: (
            self.clear_all(),
            self.display_label.configure(text_color=("gray10", "gray90"))
        ))
    
    def update_display(self):
        display_text = self.current_expression[:15] if len(self.current_expression) > 15 else self.current_expression
        self.display_label.configure(text=display_text)
    
    def update_history(self):
        history_text = self.total_expression.replace("*", "×").replace("/", "÷").replace("-", "−")
        self.history_label.configure(text=history_text[-35:])  # Show last 35 chars
    
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
    calc = CustomTkinterCalculator()
    calc.run()
