# GUI -> Graphical User Interface = adalah yang berinteraksi dengan komputer/laptop kita contohnya vsc ini

import tkinter as tk

window = tk.Tk()
window.configure(bg="white")
window.geometry("300x200")
window.resizable(False,False)  # untuk lebar dan untuk tinggi
window.mainloop()
