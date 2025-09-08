from tkinter import *

# Create the main window with modern styling
root = Tk()
root.title("Modern Simple Calculator")
root.geometry("320x450")
root.configure(bg='#1a1a2e')
root.resizable(False, False)

# Modern color scheme
colors = {
    'bg_main': '#1a1a2e',
    'bg_display': '#16213e',
    'bg_numbers': '#533483',
    'bg_operators': '#e94560',
    'bg_special': '#f39c12',
    'text_light': '#ffffff',
    'text_dark': '#000000'
}





# defining functionality.
def entry(event): 
    text = StringVar()
    text = event.widget.cget('text')
    if text == "=":
        if scval.get().isdigit():
            value = int(scval.get())
        else:
            try:
                value = eval(scval.get())
            except Exception as e:
                print(e)
                value = "Error"
                scval.set(value)
        scval.set(value)
        
    elif text == "clear":
        scval.set("")
    else:
         scval.set(scval.get() + text)

    

# binding function to all.
root.bind_all("<Button-1>", entry)


# creating a global variable.
global scval
scval = StringVar()
scval.set("")


# creating input box with modern styling
e = Entry(root, width=25, borderwidth=3, textvar=scval, 
          font=('Segoe UI', 16, 'bold'), justify='right',
          bg=colors['bg_display'], fg=colors['text_light'],
          insertbackground=colors['text_light'])
e.grid(row=0, column=0, columnspan=4, padx=10, pady=20, ipady=10)

# Define button creation function for consistency
def create_button(text, row, col, color_type='numbers', width=2, height=1, columnspan=1):
    if color_type == 'numbers':
        bg_color = colors['bg_numbers']
        fg_color = colors['text_light']
    elif color_type == 'operators':
        bg_color = colors['bg_operators']
        fg_color = colors['text_light']
    else:  # special
        bg_color = colors['bg_special']
        fg_color = colors['text_dark']
    
    btn = Button(root, text=text, padx=20, pady=15,
                font=('Segoe UI', 14, 'bold'),
                bg=bg_color, fg=fg_color,
                borderwidth=0, relief='flat',
                activebackground=bg_color, activeforeground=fg_color,
                cursor='hand2')
    btn.grid(row=row, column=col, columnspan=columnspan, padx=2, pady=2, sticky='nsew')
    return btn



# Configure grid weights for responsive design
for i in range(7):
    root.rowconfigure(i, weight=1)
for i in range(4):
    root.columnconfigure(i, weight=1)

# defining buttons of calculator with modern styling
create_button('7', 1, 0)
create_button('8', 1, 1)
create_button('9', 1, 2)
create_button('/', 1, 3, 'operators')

create_button('4', 2, 0)
create_button('5', 2, 1)
create_button('6', 2, 2)
create_button('*', 2, 3, 'operators')

create_button('1', 3, 0)
create_button('2', 3, 1)
create_button('3', 3, 2)
create_button('-', 3, 3, 'operators')

create_button('0', 4, 0, columnspan=2)
create_button('.', 4, 2)
create_button('+', 4, 3, 'operators')

# special buttons
create_button('=', 5, 2, 'special', columnspan=2)
create_button('clear', 5, 0, 'special', columnspan=2)










root.mainloop()