from tkinter import *
from tkinter import ttk

class calculator:
    def __init__(self):
        self.window = Tk()
        self.window.geometry("375x667")
        self.window.resizable(0,0)
        self.window.title("Modern Calculator")
        
        # Modern color scheme
        self.colors = {
            'bg_main': '#1e1e2e',           # Dark background
            'bg_display': '#2a2a3e',        # Display background
            'bg_numbers': '#3c3c54',        # Number buttons
            'bg_operators': '#6c7086',      # Operator buttons
            'bg_special': '#89b4fa',        # Special buttons (clear, equals)
            'bg_hover': '#585875',          # Hover effect
            'text_primary': '#cdd6f4',      # Primary text
            'text_secondary': '#bac2de',    # Secondary text
            'text_accent': '#1e1e2e',       # Text on accent buttons
            'accent': '#89b4fa',            # Accent color
            'error': '#f38ba8'              # Error color
        }
        
        # Configure window
        self.window.configure(bg=self.colors['bg_main'])
        
        # Add subtle shadow effect using a frame
        self.shadow_frame = Frame(self.window, bg='#11111b', height=10)
        self.shadow_frame.pack(fill='x', side='bottom')

        self.total_expression = ""
        self.current_expression = ""
        self.display_frame = self.create_display_frame()

        self.total_label, self.label = self.create_display_labels()

        self.digits = {
            7:(1,1), 8:(1,2), 9:(1,3),
            4:(2,1), 5:(2,2), 6:(2,3), 
            1:(3,1), 2:(3,2), 3:(3,3), 
            0:(4,2), ".":(4,1)
        }

        self.operations = {
            "/":"\u00F7", "*":"\u00D7", "-":"-", "+":"+"
        }

        self.buttons_frame = self.create_buttons_frame()

        self.buttons_frame.rowconfigure(0, weight=1)

        for i in range(1,5):
            self.buttons_frame.rowconfigure(i, weight=1)
            self.buttons_frame.columnconfigure(i, weight=1)

        
        self.create_digit_buttons()
        self.create_operation_buttons()
        self.create_clear_button()
        self.create_equal_button()
        self.create_square_button()
        self.create_sqrt_button()
        self.bind_keys()

    def bind_keys(self):
        self.window.bind("<Return>", lambda event: self.evaluate())
        for keys in self.digits:
            self.window.bind(str(keys), lambda event, digit=keys: self.add_to_expression(digit))

        for keys in self.operations:
            self.window.bind(str(keys), lambda event, operator=keys: self.append_operator(operator))

    def create_display_labels(self):    
        total_label = Label(self.display_frame, text=self.total_expression, anchor=E, 
                           bg=self.colors['bg_display'], fg=self.colors['text_secondary'], 
                           padx=24, font=("Segoe UI", 16))
        total_label.pack(expand=True, fill="both")

        label = Label(self.display_frame, text=self.current_expression, anchor=E, 
                     bg=self.colors['bg_display'], fg=self.colors['text_primary'], 
                     padx=24, font=("Segoe UI", 40, "bold"))
        label.pack(expand=True, fill="both")

        return total_label, label
    
    def create_display_frame(self):
        frame = Frame(self.window, height=221, bg=self.colors['bg_display'], 
                     relief='flat', bd=0)
        frame.pack(expand=True, fill="both", padx=10, pady=(10, 5))
        
        # Add a subtle border
        border_frame = Frame(frame, bg=self.colors['accent'], height=2)
        border_frame.pack(fill='x', side='bottom')
        
        return frame

    def add_to_expression(self, value):
        self.current_expression += str(value)
        self.update_label()
    
    def append_operator(self, operator):
        self.current_expression += operator
        self.total_expression += self.current_expression
        self.current_expression = ""
        self.update_total_lable()
        self.update_label()
    
    
    def create_digit_buttons(self):
        for digit, grid_val in self.digits.items():
            button = Button(self.buttons_frame, text=str(digit), 
                           bg=self.colors['bg_numbers'], fg=self.colors['text_primary'], 
                           font=("Segoe UI", 24, "bold"), borderwidth=0, relief='flat',
                           activebackground=self.colors['bg_hover'], 
                           activeforeground=self.colors['text_primary'],
                           cursor='hand2',
                           command=lambda x=digit: self.add_to_expression(x))
            button.grid(row=grid_val[0], column=grid_val[1], sticky=NSEW, padx=2, pady=2)
            
            # Add hover effects
            button.bind("<Enter>", lambda e, btn=button: btn.configure(bg=self.colors['bg_hover']))
            button.bind("<Leave>", lambda e, btn=button: btn.configure(bg=self.colors['bg_numbers']))
    
    def create_operation_buttons(self): 
        for i, (operator, symbol) in enumerate(self.operations.items()):
            op_button = Button(self.buttons_frame, text=symbol, 
                             bg=self.colors['bg_operators'], fg=self.colors['text_primary'], 
                             font=("Segoe UI", 20, "bold"), borderwidth=0, relief='flat',
                             activebackground=self.colors['bg_hover'], 
                             activeforeground=self.colors['text_primary'],
                             cursor='hand2',
                             command=lambda x=operator: self.append_operator(x))
            op_button.grid(row=i, column=4, sticky=NSEW, padx=2, pady=2)
            
            # Add hover effects
            op_button.bind("<Enter>", lambda e, btn=op_button: btn.configure(bg=self.colors['bg_hover']))
            op_button.bind("<Leave>", lambda e, btn=op_button: btn.configure(bg=self.colors['bg_operators']))

    def clear(self):
        self.current_expression = ""
        self.total_expression = ""
        self.update_total_lable()
        self.update_label()

    def create_clear_button(self):
        clear = Button(self.buttons_frame, text="C", 
                      bg=self.colors['bg_special'], fg=self.colors['text_accent'], 
                      font=("Segoe UI", 20, "bold"), borderwidth=0, relief='flat',
                      activebackground='#74c0fc', activeforeground=self.colors['text_accent'],
                      cursor='hand2',
                      command=self.clear)
        clear.grid(row=0, column=1, sticky=NSEW, padx=2, pady=2)
        
        # Add hover effects
        clear.bind("<Enter>", lambda e: clear.configure(bg='#74c0fc'))
        clear.bind("<Leave>", lambda e: clear.configure(bg=self.colors['bg_special']))

    def evaluate(self):
        self.total_expression += self.current_expression
        self.update_total_lable()
        try:
            self.current_expression = str(eval(self.total_expression))
            self.total_expression = ""
        except Exception as e:
            self.current_expression = "Error"
            # Change display color to error color temporarily
            self.label.config(fg=self.colors['error'])
            self.window.after(2000, lambda: self.label.config(fg=self.colors['text_primary']))
        finally:
            self.update_label()
    
    def create_equal_button(self):
        equal = Button(self.buttons_frame, text="=", 
                      bg=self.colors['bg_special'], fg=self.colors['text_accent'], 
                      font=("Segoe UI", 20, "bold"), borderwidth=0, relief='flat',
                      activebackground='#74c0fc', activeforeground=self.colors['text_accent'],
                      cursor='hand2',
                      command=self.evaluate)
        equal.grid(row=4, column=3, columnspan=2, sticky=NSEW, padx=2, pady=2)
        
        # Add hover effects
        equal.bind("<Enter>", lambda e: equal.configure(bg='#74c0fc'))
        equal.bind("<Leave>", lambda e: equal.configure(bg=self.colors['bg_special']))
    
    def square(self):
        self.current_expression = str(eval(f"{self.current_expression}**2"))
        self.update_label()


    def create_square_button(self):
        square = Button(self.buttons_frame, text="x²", 
                       bg=self.colors['bg_operators'], fg=self.colors['text_primary'], 
                       font=("Segoe UI", 20, "bold"), borderwidth=0, relief='flat',
                       activebackground=self.colors['bg_hover'], 
                       activeforeground=self.colors['text_primary'],
                       cursor='hand2',
                       command=self.square)
        square.grid(row=0, column=2, sticky=NSEW, padx=2, pady=2)
        
        # Add hover effects
        square.bind("<Enter>", lambda e: square.configure(bg=self.colors['bg_hover']))
        square.bind("<Leave>", lambda e: square.configure(bg=self.colors['bg_operators']))


    
    def sqrt(self):
        self.current_expression = str(eval(f"{self.current_expression}**0.5"))
        self.update_label()

        
    def create_sqrt_button(self):
        sqrt = Button(self.buttons_frame, text="√x", 
                     bg=self.colors['bg_operators'], fg=self.colors['text_primary'], 
                     font=("Segoe UI", 20, "bold"), borderwidth=0, relief='flat',
                     activebackground=self.colors['bg_hover'], 
                     activeforeground=self.colors['text_primary'],
                     cursor='hand2',
                     command=self.sqrt)
        sqrt.grid(row=0, column=3, sticky=NSEW, padx=2, pady=2)
        
        # Add hover effects
        sqrt.bind("<Enter>", lambda e: sqrt.configure(bg=self.colors['bg_hover']))
        sqrt.bind("<Leave>", lambda e: sqrt.configure(bg=self.colors['bg_operators']))


    
    def create_buttons_frame(self):
        frame = Frame(self.window, bg=self.colors['bg_main'])
        frame.pack(expand=True, fill="both", padx=10, pady=(5, 10))
        return frame
    
    def update_total_lable(self):
        expression = self.total_expression
        for operator, symbol in self.operations.items():
            expression = expression.replace(operator, f"{symbol}")
        self.total_label.config(text=expression)

    def update_label(self):
        self.label.config(text=self.current_expression[:11])
    
    
    
    def run(self):
        self.window.mainloop()

c = calculator()
c.run()