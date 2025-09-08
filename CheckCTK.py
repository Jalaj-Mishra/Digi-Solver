import customtkinter as ctk

ctk.set_appearance_mode("dark")  # "light" or "system"
ctk.set_default_color_theme("blue")  # "green", "dark-blue" etc.

app = ctk.CTk()
app.geometry("400x300")

btn = ctk.CTkButton(app, text="Click Me", corner_radius=10)
btn.pack(pady=20)

app.mainloop()