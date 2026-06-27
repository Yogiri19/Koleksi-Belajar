# GUI -> Graphical User Interface = adalah yang berinteraksi dengan komputer/laptop kita contohnya vsc ini

import tkinter as tk
from tkinter import ttk
window = tk.Tk()
window.configure(bg="white")
window.geometry("300x200")
window.resizable(False,False)  # untuk lebar dan untuk tinggi
window.title("Sapa Dia!")

# x = horizontal. y = vertikal
# frame input
input_frame = ttk.Frame(window)
# penempatan Grid, Pack, Place
input_frame.pack(padx=10,pady=10,fill="x",expand=True)

# komponen-komponen
# 1. Label nama depan
nama_depan_label = ttk.Label(input_frame,text="Nama depan")
nama_depan_label.pack(padx=10,pady=10,fill="y",expand=True)
window.mainloop()
