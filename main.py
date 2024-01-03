import difflib
import tkinter as tk
from tkinter import Entry, Label, Button, Listbox, Scrollbar, END

# Belirli bir kelime setini kullanarak örnek bir kelime seti oluşturun
kelime_seti = set(["python", "programlama", "veri", "makine", "öğrenme", "yapay", "zeka", "ileri", "İrtica", "İltica", "geri" , "Layık" ,"iğne" ,"uzay" , " Laik" , "Nüfuz" ,"Nüfus" , "Çekimser" , "Çekingen" , "Çekirge"])

def benzer_kelimeleri_bul(kelime):
    benzer_kelimeler = difflib.get_close_matches(kelime, kelime_seti, n=5, cutoff=0.6)
    return benzer_kelimeler

def benzer_kelimeleri_goster():
    kullanici_kelimesi = kelime_giris.get()
    benzer_kelimeler = benzer_kelimeleri_bul(kullanici_kelimesi)

    # Listbox içeriğini temizle
    benzer_kelimeler_listbox.delete(0, END)

    if benzer_kelimeler:
        for benzer_kelime in benzer_kelimeler:
            benzer_kelimeler_listbox.insert(END, benzer_kelime)
    else:
        benzer_kelimeler_listbox.insert(END, f"{kullanici_kelimesi}'e benzer bir kelime bulunamadı.")

# Tkinter penceresini oluşturun
root = tk.Tk()
root.title("Benzer Kelimeler Bulma Uygulaması")

# Etiket (Label) oluşturun
etiket = Label(root, text="Bir kelime girin:")
etiket.pack(pady=10)

# Giriş kutusu (Entry) oluşturun
kelime_giris = Entry(root, width=30)
kelime_giris.pack(pady=10)

# Buton oluşturun ve fonksiyonu bağlayın
benzer_kelimeler_buton = Button(root, text="Benzer Kelimeleri Bul", command=benzer_kelimeleri_goster)
benzer_kelimeler_buton.pack(pady=10)

# Listbox ve Scrollbar oluşturun
benzer_kelimeler_listbox = Listbox(root, width=50, height=10)
benzer_kelimeler_listbox.pack(pady=10)

scrollbar = Scrollbar(root)
scrollbar.pack(side="right", fill="y")

# Listbox ve Scrollbar'ı birbirine bağlayın
benzer_kelimeler_listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=benzer_kelimeler_listbox.yview)

# Tkinter penceresini çalıştırın
root.mainloop()
