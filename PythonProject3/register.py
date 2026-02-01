import tkinter as tk
from login import LoginWindow

PRIMARY_COLOR = "#6B8FB4"
ACCENT_COLOR = "#F4B6A6"
BG_COLOR = "#F7F9FC"

class RegisterWindow:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Register")
        self.root.geometry("350x350")
        self.root.configure(bg=BG_COLOR)

        tk.Label(self.root, text="Create Account",
                 font=("Arial", 18, "bold"),
                 bg=BG_COLOR).pack(pady=10)

        self.name = tk.Entry(self.root)
        self.name.pack()
        self.user = tk.Entry(self.root)
        self.user.pack()
        self.pw = tk.Entry(self.root, show="*")
        self.pw.pack()

        tk.Button(self.root, text="REGISTER",
                  bg=PRIMARY_COLOR, fg="white").pack(pady=10)

        tk.Button(self.root, text="BACK",
                  bg=ACCENT_COLOR,
                  command=self.back).pack()

        self.root.mainloop()

    def back(self):
        self.root.destroy()
        LoginWindow()
