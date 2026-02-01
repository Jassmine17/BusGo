import tkinter as tk
from dashboard import DashboardWindow

PRIMARY_COLOR = "#6B8FB4"
ACCENT_COLOR = "#F4B6A6"
BG_COLOR = "#F7F9FC"

class AdminWindow:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Admin Dashboard")
        self.root.geometry("400x350")
        self.root.configure(bg=BG_COLOR)

        tk.Label(self.root, text="Admin Panel",
                 font=("Arial", 18, "bold"),
                 bg=BG_COLOR).pack(pady=10)

        tk.Button(self.root, text="Manage Users",
                  width=20, bg=PRIMARY_COLOR, fg="white").pack(pady=5)

        tk.Button(self.root, text="Manage Buses",
                  width=20, bg=PRIMARY_COLOR, fg="white").pack(pady=5)

        tk.Button(self.root, text="Reports",
                  width=20, bg=PRIMARY_COLOR, fg="white").pack(pady=5)

        tk.Button(self.root, text="Back",
                  width=20, bg=ACCENT_COLOR,
                  command=self.back).pack(pady=5)

        self.root.mainloop()

    def back(self):
        self.root.destroy()
        DashboardWindow()
