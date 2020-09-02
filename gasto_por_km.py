import tkinter
from tkinter import *

root=Tk()

class Funcoes():
    def Calcula(self):
        distancia=self.entry_dis.get()
        litro = self.entry_litro.get()
        convdistancia=int(distancia)
        conlitro=int(litro)
        media=convdistancia/conlitro
        self.lb_mostra['text']=(str('voce rodou uma media')+(' ')+str(media)+('KM'))


class Aplicacao(Funcoes):
    def __init__(self):
        self.root=root
        self.Tela()
        self.Frame()
        self.Label()
        root.mainloop()
    def Tela(self):
        self.root.title('Calculador de KM')
        self.root.geometry('800x700')
    def Frame(self):
        self.principal=Frame(self.root,bg='red')
        self.principal.place(relx=0.01,rely=0.01,relwidth=0.95,relheight=0.50)
    def Label(self):
        self.lb_dis=Label(self.principal,text='Distantica')
        self.lb_dis.place(relx=0.01,rely=0.01)

        self.lb_litro=Label(self.principal,text='Litro')
        self.lb_litro.place(relx=0.01,rely=0.10)

        self.entry_dis=Entry(self.principal)
        self.entry_dis.place(relx=0.10,rely=0.01)

        self.entry_litro=Entry(self.principal)
        self.entry_litro.place(relx=0.10,rely=0.10)

        self.bt_calc=Button(self.principal,text='Calcular',command=self.Calcula)
        self.bt_calc.place(relx=0.14,rely=0.20)

        self.lb_mostra=Label(self.principal,text='Resultado')
        self.lb_mostra.place(relx=0.27,rely=0.01,relwidth=0.25,relheight=0.15)

Aplicacao()



