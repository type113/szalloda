from szalloda import Szalloda
from szoba import EgyagyasSzoba, KetagyasSzoba
import tkinter as tk
from tkinter import messagebox
from datetime import datetime
from datetime import timedelta

def foglalas():
    success = False
    foglalas_szama_vagy_sikertelenseg_oka = "Hibás a dátum."
    try:
        datum = datum_entry.get()
        szobak_szama = szobak_szama_var.get()
        szoba_tipus = None
        if szobak_szama == "egyszobas":
            szoba_tipus = EgyagyasSzoba(klima_var.get() == "klimaval")
        elif szobak_szama == "ketszobas":
            szoba_tipus = KetagyasSzoba(erkely_var.get() == "erkelyes")
        success, foglalas_szama_vagy_sikertelenseg_oka = szalloda.foglalas(szoba_tipus, datetime.strptime(datum, "%Y%m%d"))
    except:
        pass
    if not success:
        messagebox.showinfo("Foglalás", "A foglalás sikertelen. Oka: " + foglalas_szama_vagy_sikertelenseg_oka)
    else:    
        messagebox.showinfo("Foglalás", "A foglalás sikeresen rögzítve. A foglalás száma: " + str(foglalas_szama_vagy_sikertelenseg_oka))

def lemondas():
    success = False
    try:
        success = szalloda.foglalas_lemondasa(int(foglalas_szam_entry.get()))
    except:
        pass    
    if success:
        messagebox.showinfo("Foglalás törlése", "A foglalás sikeresen törölve.")
    else:
        messagebox.showinfo("Foglalás törlése", "A foglalás nem található.")

def listazas():
    listazoablak = tk.Toplevel(root)
    listazoablak.title("Foglalások listája")
    foglalasok_text = tk.Text(listazoablak, height=20, width=85)
    foglalasok_text.pack()
    for foglalas_szam, foglalas in szalloda.osszes_foglalas_listazasa():
        foglalasok_text.insert(tk.END, f"{str(foglalas_szam)} - {str(foglalas)}\n")

def update_radio_buttons():
    klima_radio.grid(row=3, column=1)
    klima_nelkuli_radio.grid(row=3, column=2)
    erkely_radio.grid(row=4, column=1)
    erkely_nelkuli_radio.grid(row=4, column=2)
    klima_radio.config(state=tk.NORMAL)
    klima_nelkuli_radio.config(state=tk.NORMAL)
    erkely_radio.config(state=tk.NORMAL)
    erkely_nelkuli_radio.config(state=tk.NORMAL)
    if szobak_szama_var.get() == "egyszobas":
        erkely_radio.config(state=tk.DISABLED)
        erkely_nelkuli_radio.config(state=tk.DISABLED)
        klima_radio.deselect()
        klima_nelkuli_radio.select()
    elif szobak_szama_var.get() == "ketszobas":
        klima_radio.config(state=tk.DISABLED)
        klima_nelkuli_radio.config(state=tk.DISABLED)
        erkely_radio.deselect()
        erkely_nelkuli_radio.select()



szalloda = Szalloda("Hotel Dávid")
szalloda.uj_szoba_hozzaadasa(EgyagyasSzoba())
szalloda.uj_szoba_hozzaadasa(EgyagyasSzoba(klima=True))
szalloda.uj_szoba_hozzaadasa(KetagyasSzoba())
datum = datetime.now()
datum += timedelta(days=30)
siker1, foglalas1 = szalloda.foglalas(EgyagyasSzoba(), datum)
datum += timedelta(days=1)
siker2, foglalas2 = szalloda.foglalas(EgyagyasSzoba(klima=True), datum)
datum += timedelta(days=1)
siker3, foglalas3 = szalloda.foglalas(EgyagyasSzoba(klima=True), datum)
datum += timedelta(days=1)
siker4, foglalas4 = szalloda.foglalas(KetagyasSzoba(), datum)
datum += timedelta(days=1)
siker5, foglalas5 = szalloda.foglalas(KetagyasSzoba(), datum)

root = tk.Tk()
root.title("Szobafoglalás - " + szalloda.get_nev())

datum_label = tk.Label(root, text="Dátum (ÉÉÉÉHHNN):")
datum_label.grid(row=1, column=0)
datum_entry = tk.Entry(root)
datum_entry.grid(row=1, column=1)

szobak_szama_var = tk.StringVar()
szobak_szama_var.set("egyszobas") 
szobak_szama_label = tk.Label(root, text="Szobák száma:")
szobak_szama_label.grid(row=2, column=0)
egyszobas_radio = tk.Radiobutton(root, text="Egyszobás", variable=szobak_szama_var, value="egyszobas", command=update_radio_buttons)
egyszobas_radio.grid(row=2, column=1)
ketszobas_radio = tk.Radiobutton(root, text="Kétszobás", variable=szobak_szama_var, value="ketszobas", command=update_radio_buttons)
ketszobas_radio.grid(row=2, column=2)

foglalas_szam_label = tk.Label(root, text="Foglalás száma (lemondáshoz):")
foglalas_szam_label.grid(row=5, column=0)
foglalas_szam_entry = tk.Entry(root)
foglalas_szam_entry.grid(row=5, column=1)

foglalas_button = tk.Button(root, text="Foglalás", command=foglalas)
foglalas_button.grid(row=6, column=0)
lemondas_button = tk.Button(root, text="Lemondás", command=lemondas)
lemondas_button.grid(row=6, column=1)
listazas_button = tk.Button(root, text="Listázás", command=listazas)
listazas_button.grid(row=6, column=2)

klima_var = tk.StringVar()
klima_var.set("klima_nelkul") 
erkely_var = tk.StringVar()
erkely_var.set("erkely_nelkuli")
klima_radio = tk.Radiobutton(root, text="Klímával", variable=klima_var, value="klimaval")
klima_nelkuli_radio = tk.Radiobutton(root, text="Klíma nélkül", variable=klima_var, value="klima_nelkul")
erkely_radio = tk.Radiobutton(root, text="Erkélyes", variable=erkely_var, value="erkelyes")
erkely_nelkuli_radio = tk.Radiobutton(root, text="Erkély nélküli", variable=erkely_var, value="erkely_nelkuli")

update_radio_buttons()
root.mainloop()

