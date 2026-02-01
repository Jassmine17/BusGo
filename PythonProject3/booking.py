import tkinter as tk
from dashboard import DashboardWindow

PRIMARY_COLOR = "#6B8FB4"
ACCENT_COLOR = "#F4B6A6"
BG_COLOR = "#F7F9FC"

class BookingWindow:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Book Ticket")
        self.root.geometry("350x350")
        self.root.configure(bg=BG_COLOR)

        tk.Label(self.root, text="Ticket Booking",
                 font=("Arial", 18, "bold"),
                 bg=BG_COLOR).pack(pady=10)

        tk.Entry(self.root).pack()
        tk.Entry(self.root).pack()
        tk.Entry(self.root).pack()

        tk.Button(self.root, text="Confirm Booking",
                  bg=PRIMARY_COLOR, fg="white").pack(pady=10)

        tk.Button(self.root, text="Back",
                  bg=ACCENT_COLOR,
                  command=self.back).pack()

        self.root.mainloop()

    def back(self):
        self.root.destroy()
        DashboardWindow()
