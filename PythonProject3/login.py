import tkinter as tk
from register import RegisterWindow
from dashboard import DashboardWindow

PRIMARY_COLOR = "#6B8FB4"
ACCENT_COLOR = "#F4B6A6"
BG_COLOR = "#F7F9FC"

class LoginWindow:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("BusGo - Login")
        self.root.geometry("350x300")
        self.root.configure(bg=BG_COLOR)

        tk.Label(self.root, text="BUSGO",
                 font=("Arial", 22, "bold"),
                 bg=BG_COLOR, fg=PRIMARY_COLOR).pack(pady=10)

        tk.Label(self.root, text="Username").pack()
        self.user = tk.Entry(self.root)
        self.user.pack()

        tk.Label(self.root, text="Password").pack()
        self.pw = tk.Entry(self.root, show="*")
        self.pw.pack()

        tk.Button(self.root, text="LOGIN",
                  bg=PRIMARY_COLOR, fg="white",
                  command=self.login).pack(pady=10)

        tk.Button(self.root, text="REGISTER",
                  bg=ACCENT_COLOR,
                  command=self.open_register).pack()

        self.root.mainloop()

    def login(self):
        self.root.destroy()
        DashboardWindow()

    def open_register(self):
        self.root.destroy()
        RegisterWindow()
