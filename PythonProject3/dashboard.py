import tkinter as tk
from booking import BookingWindow
from admin import AdminWindow

PRIMARY_COLOR = "#6B8FB4"
ACCENT_COLOR = "#F4B6A6"
BG_COLOR = "#F7F9FC"

class DashboardWindow:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("BusGo - Dashboard")
        self.root.geometry("400x350")
        self.root.configure(bg=BG_COLOR)

        tk.Label(self.root, text="User Dashboard",
                 font=("Arial", 18, "bold"),
                 bg=BG_COLOR).pack(pady=10)

        tk.Button(self.root, text="Book Ticket",
                  width=20, bg=PRIMARY_COLOR, fg="white",
                  command=self.open_booking).pack(pady=5)

        tk.Button(self.root, text="Admin Panel",
                  width=20, bg=ACCENT_COLOR,
                  command=self.open_admin).pack(pady=5)

        tk.Button(self.root, text="Exit",
                  width=20, bg="gray",
                  command=self.root.destroy).pack(pady=5)

        self.root.mainloop()

    def open_booking(self):
        self.root.destroy()
        BookingWindow()

    def open_admin(self):
        self.root.destroy()
        AdminWindow()
