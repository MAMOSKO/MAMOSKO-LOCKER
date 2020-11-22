try:
    from os import startfile
    from tkinter import Label,Button,mainloop,Tk,Entry,FALSE,Frame,messagebox

    def kontrol():
        if entry.get()==514 or entry.get()=="514":
            file=open("licance", "w")
            file.write("Licance.514")
            file.close()
            messagebox.showinfo("Onaylandı","Lisansınız başarıyla onaylanmıştır!")
            startfile("locker.py")
            pencere.quit()
        else:
            messagebox.showerror("Yanlış Lisans","Hatalı lisans kodu!",detail="Hatalı bir lisans kodu girdiniz lütfen lisans kodunuzu kontrol ediniz.")

    pencere = Tk()
    pencere.geometry("400x200+500+100")
    pencere.resizable(width=FALSE, height=FALSE)
    pencere.title("Lisans")
    bosluk = Frame()
    bosluk2 = Frame()
    etiket = Label(text="Lütfen Lisans Numaranızı Giriniz")
    etiket2= Label(text="->Bu bir tanıtım uygulamasıdır lisans sadece\ntesterlera ve geliştiricilere verilir<--",fg="red",bg="black")

    entry = Entry(width=30)
    buton = Button(text="Kontrol Et", command=kontrol)

    etiket2.pack()
    etiket.pack()
    bosluk.pack()
    entry.pack()
    bosluk2.pack(pady=10)
    buton.pack()

    try:
        file=open("licance", "r")
        l=file.read()
        file.close()
    except:
        file=open("licance", "w")
        file.close()
        file=open("licance", "r")
        l=file.read()
        file.close()
    if l=="Licance.514":
        startfile("locker.py")
        pencere.quit()
    else:
        mainloop()
except:
    pass
