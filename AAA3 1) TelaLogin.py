from tkinter import *

master = Tk()
master.title("Login Chapa")
master.geometry("395x376")
master.resizable(width=1, height=1)

def nova_janela():
  master1 = Tk()
  master1.title("Bem vindo ao Chapa, integrante")
  master1.geometry("395x376")

  master.destroy()







esconda_senha = StringVar()

img_fundo = PhotoImage(file="chapa.png")
img_botao = PhotoImage(file="login.png")

lab_fundo = Label(master, image=img_fundo)
lab_fundo.pack()

en_token = Entry(master, bd=2, font=("Calibri", 15), justify=CENTER)
en_token.place(width=327, height=53, x=35, y=100)

en_token = Entry(master, textvariable=esconda_senha, show='*', bd=2, font=("Calibri", 15), justify=CENTER)
en_token.place(width=320, height=40, x=40, y=190)

bt_entrar = Button(master, bd=0, image=img_botao, command=nova_janela)
bt_entrar.place(width=148, height=81, x=127, y=280)


master.mainloop()