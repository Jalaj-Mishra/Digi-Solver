from tkinter import *
root = Tk()
root.title("Tkinter Calculator App")
root.geometry("282x402")





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


# creating impuyt box.
e = Entry(root, width=33, borderwidth=5, textvar=scval).grid(row=0, column=0, columnspan=4, padx=4)



# defining buttons of calculator.
b1 = Button(root, text='1', padx=35, pady=15).grid(row=3, column=0)
b2 = Button(root, text='2', padx=35, pady=15).grid(row=3, column=1)
b3 = Button(root, text='3', padx=35, pady=15).grid(row=3, column=2)
b4 = Button(root, text='4', padx=35, pady=15).grid(row=2, column=0)
b5 = Button(root, text='5', padx=35, pady=15).grid(row=2, column=1)
b6 = Button(root, text='6', padx=35, pady=15).grid(row=2, column=2)
b7 = Button(root, text='7', padx=35, pady=15).grid(row=1, column=0)
b8 = Button(root, text='8', padx=35, pady=15).grid(row=1, column=1)
b9 = Button(root, text='9', padx=35, pady=15).grid(row=1, column=2)
b0 = Button(root, text='0', padx=35, pady=15).grid(row=4, column=0)

#functional buttons
b_add = Button(root, text='+', padx=34, pady=15).grid(row=4, column=1)
b_sub = Button(root, text='-', padx=36, pady=15).grid(row=4, column=2)
b_mul = Button(root, text='*', padx=36, pady=15).grid(row=5, column=0)
b_div = Button(root, text='/', padx=36.2, pady=15).grid(row=5, column=1)

# additional buttons
b_equal = Button(root, text='=', padx=34, pady=45).grid(row=5, column=2, rowspan=2)
b_clear = Button(root, text='clear', padx=71, pady=15).grid(row=6, column=0, columnspan=2)










root.mainloop()