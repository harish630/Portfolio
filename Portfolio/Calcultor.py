import tkinter as tk
from tkinter import font

class Calculator:
    def __init__(self, master):
        self.master = master
        self.master.title("Colorful Calculator")
        self.master.configure(bg="#f0f0f0")

        # Entry widget to display input and output
        self.entry = tk.Entry(master, width=30, font=("Helvetica", 14), bd=10, relief=tk.FLAT)
        self.entry.grid(row=0, column=0, columnspan=4, pady=10)

        # Define button colors
        button_bg = "#4CAF50"
        button_fg = "#FFFFFF"

        # Create buttons
        buttons = [
            ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
            ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
            ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
            ("0", 4, 0), (".", 4, 1), ("=", 4, 2), ("+", 4, 3),
            ("C", 5, 0)
        ]

        # Create buttons and assign them to grid
        for (text, row, col) in buttons:
            btn = tk.Button(master, text=text, width=5, height=2, bg=button_bg, fg=button_fg,
                            font=("Helvetica", 12, "bold"), bd=2, relief=tk.RAISED,
                            command=lambda t=text: self.on_button_click(t))
            btn.grid(row=row, column=col, padx=5, pady=5)

    def on_button_click(self, text):
        if text == "=":
            try:
                result = eval(self.entry.get())
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, str(result))
            except Exception as e:
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, "Error")
        elif text == "C":
            self.entry.delete(0, tk.END)
        else:
            self.entry.insert(tk.END, text)


def main():
    root = tk.Tk()
    calculator = Calculator(root)
    root.mainloop()

if __name__ == "__main__":
    main()
