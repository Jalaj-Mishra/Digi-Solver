from tkinter import *
from tkinter import ttk
import math

class ModernCalculator:
    def __init__(self):
        self.window = Tk()
        self.window.geometry("400x700")
        self.window.resizable(0, 0)
        self.window.title("Modern Calculator")
        
        # Enhanced modern color scheme with gradients
        self.colors = {
            'bg_main': '#0f0f23',           # Very dark background
            'bg_display': '#1e1e3f',        # Display background
            'bg_numbers': '#2d2d44',        # Number buttons
            'bg_operators': '#5865f2',      # Operator buttons (Discord blue)
            'bg_special': '#57f287',        # Special buttons (green)
            'bg_danger': '#ed4245',         # Clear/danger buttons (red)
            'bg_hover_num': '#3c3c5a',      # Number hover
            'bg_hover_op': '#4752c4',       # Operator hover
            'bg_hover_special': '#51e77f',  # Special hover
            'bg_hover_danger': '#d63638',   # Danger hover
            'text_primary': '#ffffff',      # Primary text
            'text_secondary': '#b9bbbe',    # Secondary text
            'text_accent': '#ffffff',       # Text on accent buttons
            'accent': '#5865f2',            # Accent color
            'error': '#ed4245',             # Error color
            'success': '#57f287'            # Success color
        }
        
        # Configure window
        self.window.configure(bg=self.colors['bg_main'])
        
        # Initialize variables
        self.total_expression = ""
        self.current_expression = ""
        
        # Create UI components
        self.setup_ui()
        self.bind_keys()
        
    def setup_ui(self):
        # Title bar simulation
        title_frame = Frame(self.window, bg=self.colors['accent'], height=40)
        title_frame.pack(fill='x')
        title_frame.pack_propagate(False)
        
        title_label = Label(title_frame, text="Modern Calculator", 
                           bg=self.colors['accent'], fg=self.colors['text_accent'],
                           font=("Segoe UI", 16, "bold"))
        title_label.pack(expand=True)
        
        # Main container
        main_frame = Frame(self.window, bg=self.colors['bg_main'])
        main_frame.pack(expand=True, fill='both', padx=15, pady=15)
        
        # Display frame
        self.display_frame = self.create_display_frame(main_frame)
        self.total_label, self.label = self.create_display_labels()
        
        # Buttons frame
        self.buttons_frame = self.create_buttons_frame(main_frame)
        self.setup_grid()
        self.create_all_buttons()
        
    def create_display_frame(self, parent):
        frame = Frame(parent, bg=self.colors['bg_display'], height=150, relief='flat', bd=0)
        frame.pack(fill='x', pady=(0, 20))
        frame.pack_propagate(False)
        
        # Add accent border at bottom
        border = Frame(frame, bg=self.colors['accent'], height=3)
        border.pack(fill='x', side='bottom')
        
        return frame
        
    def create_display_labels(self):
        # History/total expression label
        total_label = Label(self.display_frame, text=self.total_expression, 
                           anchor=E, bg=self.colors['bg_display'], 
                           fg=self.colors['text_secondary'], 
                           padx=20, font=("Segoe UI", 14))
        total_label.pack(expand=True, fill="both")
        
        # Current expression label
        label = Label(self.display_frame, text="0", anchor=E, 
                     bg=self.colors['bg_display'], fg=self.colors['text_primary'], 
                     padx=20, font=("Segoe UI", 36, "bold"))
        label.pack(expand=True, fill="both")
        
        return total_label, label
        
    def create_buttons_frame(self, parent):
        frame = Frame(parent, bg=self.colors['bg_main'])
        frame.pack(expand=True, fill='both')
        return frame
        
    def setup_grid(self):
        # Configure grid weights for responsive design
        for i in range(6):
            self.buttons_frame.rowconfigure(i, weight=1)
        for i in range(4):
            self.buttons_frame.columnconfigure(i, weight=1)
            
    def create_button(self, text, row, col, colspan=1, rowspan=1, bg_color='bg_numbers', 
                     command=None, font_size=18):
        button = Button(self.buttons_frame, text=text,
                       bg=self.colors[bg_color], fg=self.colors['text_primary'],
                       font=("Segoe UI", font_size, "bold"), borderwidth=0, relief='flat',
                       activebackground=self.colors[f'bg_hover_{bg_color.split("_")[1]}'] if f'bg_hover_{bg_color.split("_")[1]}' in self.colors else self.colors['bg_hover_num'],
                       activeforeground=self.colors['text_primary'],
                       cursor='hand2', command=command)
        
        button.grid(row=row, column=col, columnspan=colspan, rowspan=rowspan, 
                   sticky=NSEW, padx=3, pady=3)
        
        # Add hover effects
        hover_color = self.colors.get(f'bg_hover_{bg_color.split("_")[1]}', self.colors['bg_hover_num'])
        original_color = self.colors[bg_color]
        
        button.bind("<Enter>", lambda e: button.configure(bg=hover_color))
        button.bind("<Leave>", lambda e: button.configure(bg=original_color))
        
        return button
        
    def create_all_buttons(self):
        # Row 0: Function buttons
        self.create_button("AC", 0, 0, bg_color='bg_danger', command=self.clear_all)
        self.create_button("⌫", 0, 1, bg_color='bg_danger', command=self.backspace)
        self.create_button("x²", 0, 2, bg_color='bg_operators', command=self.square)
        self.create_button("÷", 0, 3, bg_color='bg_operators', command=lambda: self.append_operator("/"))
        
        # Row 1: More functions
        self.create_button("√x", 1, 0, bg_color='bg_operators', command=self.sqrt)
        self.create_button("x³", 1, 1, bg_color='bg_operators', command=self.cube)
        self.create_button("±", 1, 2, bg_color='bg_operators', command=self.toggle_sign)
        self.create_button("×", 1, 3, bg_color='bg_operators', command=lambda: self.append_operator("*"))
        
        # Row 2: Numbers 7, 8, 9 and subtraction
        self.create_button("7", 2, 0, command=lambda: self.add_to_expression("7"))
        self.create_button("8", 2, 1, command=lambda: self.add_to_expression("8"))
        self.create_button("9", 2, 2, command=lambda: self.add_to_expression("9"))
        self.create_button("−", 2, 3, bg_color='bg_operators', command=lambda: self.append_operator("-"))
        
        # Row 3: Numbers 4, 5, 6 and addition
        self.create_button("4", 3, 0, command=lambda: self.add_to_expression("4"))
        self.create_button("5", 3, 1, command=lambda: self.add_to_expression("5"))
        self.create_button("6", 3, 2, command=lambda: self.add_to_expression("6"))
        self.create_button("+", 3, 3, bg_color='bg_operators', command=lambda: self.append_operator("+"))
        
        # Row 4: Numbers 1, 2, 3
        self.create_button("1", 4, 0, command=lambda: self.add_to_expression("1"))
        self.create_button("2", 4, 1, command=lambda: self.add_to_expression("2"))
        self.create_button("3", 4, 2, command=lambda: self.add_to_expression("3"))
        
        # Row 5: 0, decimal point
        self.create_button("0", 5, 0, colspan=2, command=lambda: self.add_to_expression("0"))
        self.create_button(".", 5, 2, command=lambda: self.add_to_expression("."))
        
        # Equals button (spans multiple rows)
        self.create_button("=", 4, 3, rowspan=2, bg_color='bg_special', 
                          command=self.evaluate, font_size=24)
        
    def add_to_expression(self, value):
        if self.current_expression == "0" or self.current_expression == "Error":
            self.current_expression = str(value)
        else:
            self.current_expression += str(value)
        self.update_label()
        
    def append_operator(self, operator):
        if self.current_expression:
            self.current_expression += operator
            self.total_expression += self.current_expression
            self.current_expression = ""
            self.update_total_label()
            self.update_label()
            
    def clear_all(self):
        self.current_expression = "0"
        self.total_expression = ""
        self.update_total_label()
        self.update_label()
        # Reset label color
        self.label.config(fg=self.colors['text_primary'])
        
    def backspace(self):
        if len(self.current_expression) > 1:
            self.current_expression = self.current_expression[:-1]
        else:
            self.current_expression = "0"
        self.update_label()
        
    def square(self):
        if self.current_expression and self.current_expression != "0":
            try:
                result = float(self.current_expression) ** 2
                self.current_expression = str(result)
                self.update_label()
            except:
                self.show_error()
                
    def cube(self):
        if self.current_expression and self.current_expression != "0":
            try:
                result = float(self.current_expression) ** 3
                self.current_expression = str(result)
                self.update_label()
            except:
                self.show_error()
                
    def sqrt(self):
        if self.current_expression and self.current_expression != "0":
            try:
                result = math.sqrt(float(self.current_expression))
                self.current_expression = str(result)
                self.update_label()
            except:
                self.show_error()
                
    def toggle_sign(self):
        if self.current_expression and self.current_expression != "0":
            if self.current_expression.startswith("-"):
                self.current_expression = self.current_expression[1:]
            else:
                self.current_expression = "-" + self.current_expression
            self.update_label()
            
    def evaluate(self):
        if self.current_expression:
            self.total_expression += self.current_expression
            self.update_total_label()
            
        try:
            # Replace display symbols with actual operators
            expression = self.total_expression.replace("×", "*").replace("÷", "/").replace("−", "-")
            result = eval(expression)
            self.current_expression = str(result)
            self.total_expression = ""
            
            # Show success animation
            self.label.config(fg=self.colors['success'])
            self.window.after(500, lambda: self.label.config(fg=self.colors['text_primary']))
            
        except Exception as e:
            self.show_error()
        finally:
            self.update_label()
            
    def show_error(self):
        self.current_expression = "Error"
        self.total_expression = ""
        self.label.config(fg=self.colors['error'])
        self.window.after(2000, lambda: (
            setattr(self, 'current_expression', '0'),
            self.label.config(fg=self.colors['text_primary']),
            self.update_label(),
            self.update_total_label()
        ))
        
    def update_total_label(self):
        # Display friendly symbols in history
        expression = self.total_expression.replace("*", "×").replace("/", "÷").replace("-", "−")
        self.total_label.config(text=expression)
        
    def update_label(self):
        # Truncate long numbers
        display_text = self.current_expression[:12] if len(self.current_expression) > 12 else self.current_expression
        self.label.config(text=display_text)
        
    def bind_keys(self):
        # Keyboard bindings
        self.window.bind("<Return>", lambda event: self.evaluate())
        self.window.bind("<KP_Enter>", lambda event: self.evaluate())
        self.window.bind("<BackSpace>", lambda event: self.backspace())
        self.window.bind("<Escape>", lambda event: self.clear_all())
        
        # Number keys
        for i in range(10):
            self.window.bind(str(i), lambda event, digit=str(i): self.add_to_expression(digit))
            self.window.bind(f"<KP_{i}>", lambda event, digit=str(i): self.add_to_expression(digit))
            
        # Operator keys
        self.window.bind("+", lambda event: self.append_operator("+"))
        self.window.bind("<KP_Add>", lambda event: self.append_operator("+"))
        self.window.bind("-", lambda event: self.append_operator("-"))
        self.window.bind("<KP_Subtract>", lambda event: self.append_operator("-"))
        self.window.bind("*", lambda event: self.append_operator("*"))
        self.window.bind("<KP_Multiply>", lambda event: self.append_operator("*"))
        self.window.bind("/", lambda event: self.append_operator("/"))
        self.window.bind("<KP_Divide>", lambda event: self.append_operator("/"))
        self.window.bind(".", lambda event: self.add_to_expression("."))
        self.window.bind("<KP_Decimal>", lambda event: self.add_to_expression("."))
        
    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    calc = ModernCalculator()
    calc.run()
