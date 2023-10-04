# color_selector.py
import tkinter as tk
from tkinter import colorchooser

class ColorSelector(tk.Toplevel):
    def __init__(self, master=None):
        super().__init__(master)
        self.title("Color Selector")

        self.color_button = tk.Button(self, text="Select Color", command=self.select_color)
        self.color_button.pack(padx=20, pady=20)

        self.selected_color_label = tk.Label(self, text="Selected Color:")
        self.selected_color_label.pack()

    def select_color(self):
        color = colorchooser.askcolor()[1]
        if color:
            self.selected_color_label.config(text=f"Selected Color: {color}")

# If this script is run directly, create an instance of ColorSelector
if __name__ == "__main__":
    root = tk.Tk()
    app = ColorSelector(root)
    root.mainloop()
