"""Hello World application for Tkinter"""


import tkinter as tk
from tkinter import ttk

root = tk.Tk()
label = ttk.Label(root, text="Hello World")
button = ttk.Button(root, text="Lick to join")
entry = ttk.Entry(root, text="Test me!")
label.pack()
button.pack()
entry.pack()
root.mainloop()
