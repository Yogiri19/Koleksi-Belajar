# GUI -> Graphical User Interface = adalah yang berinteraksi dengan komputer/laptop kita contohnya vsc ini

import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo

# init
window = tk.Tk()
window.configure(bg="white") # mengatur warna bg putih
window.geometry("300x200") # ukuran jendela
window.resizable(False,False)  # jendela tidak diubah ukurannya
window.title("Sapa Dia!") # judul jendela

# Variable dan Fungsi
#NAMA_DEPAN = tk.StringVar()
NAMA_BELAKANG = tk.StringVar()

def tombol_click():
    '''fungsi ini akan dipanggil oleh tombol'''
    pesan = f"halo {NAMA_BELAKANG.get()}, GANTENGG"
    showinfo(title="whazzup!",message=pesan)
    
# x = horizontal. y = vertikal
# frame input
input_frame = ttk.Frame(window)
# penempatan Grid, Pack, Place
input_frame.pack(padx=10,pady=10,fill="x",expand=True)

# komponen-komponen
# 1. Label nama depan
nama_depan_label = ttk.Label(input_frame,text="Nama depan")
nama_depan_label.pack(padx=10,fill="x",expand=True)
# # 2. entry nama depan
# nama_depan_entry = ttk.Entry(input_frame,textvariable=NAMA_DEPAN)
# nama_depan_entry.pack(padx=10,fill="x",expand=True)
# 3. Label nama belakang
nama_belakang_label = ttk.Label(input_frame,text="Nama belakang")
nama_belakang_label.pack(padx=10,fill="x",expand=True)
# 4. entry nama belakang
nama_belakang_entry = ttk.Entry(input_frame,textvariable=NAMA_BELAKANG)
nama_belakang_entry.pack(padx=10,fill="x",expand=True)
# 5. Tombol
tombol_sapa = ttk.Button(input_frame,text="sapa!",command=tombol_click)
tombol_sapa.pack(fill='x',expand=True,padx=10,pady=10)

# main loop windows
window.mainloop()
