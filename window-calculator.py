from tkinter import *
class calculator:
    def __init__(self):
        self.window = Tk()
        self.window.geometry("375x667")
        self.window.resizable(0,0)
        self.window.title("Calculator")

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
        total_label = Label(self.display_frame, text=self.total_expression, anchor=E, bg="#F5F5F5", fg="#000000", padx=24, font=("Arial", 16))
        total_label.pack(expand=True, fill="both")

        label = Label(self.display_frame, text=self.current_expression, anchor=E, bg="#F5F5F5", fg="#000000", padx=24, font=("Arial", 40, "bold"))
        label.pack(expand=True, fill="both")

        return total_label, label
    
    def create_display_frame(self):
        frame = Frame(self.window, height=221, bg="#F5F5F5")
        frame.pack(expand=True, fill="both")
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
            button = Button(self.buttons_frame, text=str(digit), bg="#FFFFFF", fg="#000000", font=("Arial", 24, "bold"), borderwidth=0, command=lambda x = digit: self.add_to_expression(x))
            button.grid(row=grid_val[0], column=grid_val[1], sticky=NSEW)
    
    def create_operation_buttons(self): 
        i = 0
        for operator, symbol in self.operations.items():
            operator = Button(self.buttons_frame, text=symbol, bg="#F8FAFF", fg="#000000", font=("Arial", 20), borderwidth=0, command=lambda x = operator: self.append_operator(x))
            operator.grid(row=i, column=4, sticky=NSEW)
            i+=1

    def clear(self):
        self.current_expression = ""
        self.total_expression = ""
        self.update_total_lable()
        self.update_label()

    def create_clear_button(self):
        clear = Button(self.buttons_frame, text="C", bg="#F8FAFF", fg="#000000", font=("Arial", 20), borderwidth=0, command=self.clear)
        clear.grid(row=0, column=1, sticky=NSEW)

    def evaluate(self):
        self.total_expression += self.current_expression
        self.update_total_lable()
        try:
            self.current_expression = str(eval(self.total_expression))
            self.total_expression = ""
        except Exception as e:
            self.current_expression = "Error"
        finally:
            self.update_label()
    
    def create_equal_button(self):
        equal = Button(self.buttons_frame, text="=", bg="lightblue", fg="#000000", font=("Arial", 20), borderwidth=0, command=self.evaluate)
        equal.grid(row=4, column=3, columnspan=2, sticky=NSEW)
    
    def square(self):
        self.current_expression = str(eval(f"{self.current_expression}**2"))
        self.update_label()


    def create_square_button(self):
        clear = Button(self.buttons_frame, text="x\u00b2", bg="#F8FAFF", fg="#000000", font=("Arial", 20), borderwidth=0, command=self.square)
        clear.grid(row=0, column=2, sticky=NSEW)


    
    def sqrt(self):
        self.current_expression = str(eval(f"{self.current_expression}**0.5"))
        self.update_label()

        
    def create_sqrt_button(self):
        clear = Button(self.buttons_frame, text="\u221ax", bg="#F8FAFF", fg="#000000", font=("Arial", 20), borderwidth=0, command=self.sqrt)
        clear.grid(row=0, column=3, sticky=NSEW)


    
    def create_buttons_frame(self):
        frame = Frame(self.window)
        frame.pack(expand=True, fill="both")
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