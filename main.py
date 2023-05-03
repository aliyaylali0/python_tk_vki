from tkinter import *

window = Tk()

window.minsize(width=300,height=300)
window.title("Vki Hesaplama")

kilo_label = Label(text="Kilonuzu giriniz")
kilo_label.pack()

kilo_entry = Entry(width=20)
kilo_entry.pack()

boy_label = Label(text="Boyunuzu giriniz")
boy_label.pack()


boy_entry = Entry(width=20)
boy_entry.pack()

sonuc_label = Label(text="")
sonuc_label.pack()


def hesapla():

    boy = boy_entry.get()
    kilo = kilo_entry.get()
    if boy == '' or kilo == '':
        sonuc_label.config(text="Lütfen boy ve kilo girin!")
        return
    boy = float(boy)
    kilo = float(kilo)
    vki = kilo / ((boy / 100) ** 2)
    if vki < 17:
        sonuc = "VKİ: {:.2f} - Zayıf".format(vki)
    elif vki < 24:
        sonuc = "VKİ: {:.2f} - Normal".format(vki)
    elif vki < 30:
        sonuc = "VKİ: {:.2f} - Kilolu".format(vki)
    else:
        sonuc = "VKİ: {:.2f} - Obez".format(vki)
    sonuc_label.config(text=sonuc)


hesapla_buton = Button(text="hesapla",command=hesapla)
hesapla_buton.pack()



window.mainloop()