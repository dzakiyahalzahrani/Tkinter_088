import tkinter as tk
from tkinter import messagebox

def hasil_prediksi():
    try:
        # Validasi input
        for entry in entries:
            nilai = int(entry.get())
            if not (0 <= nilai <= 100):
                raise ValueError("Nilai harus antara 0 dan 100.")
        # Menampilkan hasil prediksi
        hasil_label.config(text="Prediksi Prodi: Teknologi Informasi", bg="#E0FBFC", fg="#293241")
    except ValueError:
        messagebox.showerror("Input Error", "Pastikan semua input adalah angka antara 0 dan 100.")

# Membuat window utama
root = tk.Tk()
root.title("Aplikasi Prediksi Prodi Pilihan")
root.geometry("500x650")
root.configure(bg="#293241")  # Warna latar belakang utama (Biru kehitaman)

# Label Judul
judul_label = tk.Label(root, text="Aplikasi Prediksi Prodi Pilihan", 
                       font=("Arial", 18, "bold"), bg="#293241", fg="#E0FBFC")
judul_label.pack(pady=20)

# Frame untuk input nilai
frame_input = tk.Frame(root, bg="#3D5A80")
frame_input.pack(pady=10)

entries = []
for i in range(10):
    label = tk.Label(frame_input, text=f"Nilai Mata Pelajaran {i+1}:", 
                     font=("Arial", 12), bg="#3D5A80", fg="#E0FBFC")
    label.grid(row=i, column=0, padx=10, pady=5, sticky="e")
    entry = tk.Entry(frame_input, width=10, font=("Arial", 12), bg="#E0FBFC", fg="#293241")
    entry.grid(row=i, column=1, padx=10, pady=5)
    entries.append(entry)

# Tombol Hasil Prediksi
prediksi_button = tk.Button(root, text="Hasil Prediksi", command=hasil_prediksi, 
                            font=("Arial", 12, "bold"), bg="#EE6C4D", fg="#E0FBFC", relief="raised")
prediksi_button.pack(pady=20)

# Label untuk hasil prediksi
hasil_label = tk.Label(root, text="", font=("Arial", 14), bg="#293241", fg="#E0FBFC")
hasil_label.pack(pady=20)

# Menjalankan aplikasi
root.mainloop()
