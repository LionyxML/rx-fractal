#!/usr/bin/python3
# Arquivo : rfractal.py
# Programa: Gerador Fractal através de números aleatórios
# Autor   : Rahul Martim Juliato
# Versão  : 0.1  - 16.10.2018


#---===[0. Bibliotecas]===---
import tkinter as tk
from tkinter import messagebox as mb
from tkinter import ttk
from tkinter import Canvas
import math
#import numpy as np
import random
#---===[0. Fim das Bibliotecas]===---


#---===[0.5 Variáveis Globais]===---
#---===[0.5 Fim das Variáveis Globais]===---


#---===[1. Funções]===---
def quit():
    """ Sai do programa destruindo o necessário
    """
    global janela
    janela.destroy()


def sobre():
    """ Mostra as informações do programa
    """
    mb.showinfo("r[SISLIN]X",'''

r[SISLIN]X
Solucionador de Sistemas Lineares

Versão: 0.1

Autor: Rahul Martim Juliato
(rahul.juliato@gmail.com)

''')

def gerar(x=250, y=250):
    """Place holder para a futura implementação
    """

    stringona = []
    stringona.append([int(ent_pix.get()),500-int(ent_piy.get())])
    stringona.append([int(ent_pax.get()),500-int(ent_pay.get())])
    stringona.append([int(ent_pbx.get()),500-int(ent_pby.get())])
    stringona.append([int(ent_pcx.get()),500-int(ent_pcy.get())])

    xnovo=stringona[0][0]
    ynovo=stringona[0][1]
    posax=stringona[1][0]
    posay=stringona[1][1]
    posbx=stringona[2][0]
    posby=stringona[2][1]
    poscx=stringona[3][0]
    poscy=stringona[3][1]

    quantidade=sca_amo.get()
    
    
    for ii in range(quantidade):
        sorteio = random.randint(1,4)
        if sorteio == 1:
            xnovo=(xnovo-posax)/2+posax
            ynovo=(ynovo-posay)/2+posay
        elif sorteio == 2:
            xnovo=(xnovo-posbx)/2+posbx
            ynovo=(ynovo-posby)/2+posby
        else:
            xnovo=(xnovo-poscx)/2+poscx
            ynovo=(ynovo-poscy)/2+poscy
        stringona.append([xnovo, ynovo])
        
    
    for ii in range(len(stringona)):
        pontua(stringona[ii][0],stringona[ii][1])
        

def erro(mensagem):
    """Sobre uma messagebox de erro com a mensagem
    passada"""
    mb.showerror("Erro!", mensagem)



def pontua(x, y):
    verde = "#476042"
    x1, y1 = (x - 1), (y - 1)
    x2, y2 = (x + 1), (y + 1)
    fig.create_oval(x1, y1, x2, y2, fill=verde)

def limpar():
    fig.delete("all")
    
    
#---===[1. Fim das Funções]===---



#---===[2. Início da geração da Janela]===---
# 2.0. Definições principais da janela
janela = tk.Tk()
#janela.geometry("500x200")
janela.wm_title('r[fractal]X v0.1')
janela.wm_minsize(380,220)
janela.grid_anchor(anchor='c')
#janela.tk_setPalette('gray')


# 2.0. Barra de menu
barramenu = tk.Menu(janela)
arquivo = tk.Menu(barramenu, tearoff=800)
arquivo.add_command(label="Sobre", command=sobre)
arquivo.add_separator()
arquivo.add_command(label="Sair", command=quit)
barramenu.add_cascade(label="Arquivo", menu=arquivo)
                    
janela.config(menu=barramenu)

# 2.0 Título dentro da janela principal
#titulo = tk.Label(janela, text="r[Sistemas Lineares]X", font="Arial 16 bold", height=2)
#titulo.grid(column = 0, row = 0, sticky="NSEW")

separador = tk.ttk.Separator()

lab_x = tk.Label(janela, text="x")
lab_x.grid(row=0, column=1)
lab_y = tk.Label(janela, text="y")
lab_y.grid(row=0, column=2)

lab_pi = tk.Label(janela, text="Ponto Inicial:")
lab_pi.grid(row=1, column=0)
ent_pix = tk.Entry(janela)
ent_pix.configure(width=5)
ent_pix.grid(row=1, column=1)
ent_piy = tk.Entry(janela)
ent_piy.configure(width=5)
ent_piy.grid(row=1,column=2)

lab_pa = tk.Label(janela, text="Ponto A:")
lab_pa.grid(row=2, column=0)
ent_pax = tk.Entry(janela)
ent_pax.configure(width=5)
ent_pax.grid(row=2, column=1)
ent_pay = tk.Entry(janela)
ent_pay.configure(width=5)
ent_pay.grid(row=2,column=2)

lab_pb = tk.Label(janela, text="Ponto B:")
lab_pb.grid(row=3, column=0)
ent_pbx = tk.Entry(janela)
ent_pbx.configure(width=5)
ent_pbx.grid(row=3, column=1)
ent_pby = tk.Entry(janela)
ent_pby.configure(width=5)
ent_pby.grid(row=3,column=2)

lab_pc = tk.Label(janela, text="Ponto C:")
lab_pc.grid(row=4, column=0)
ent_pcx = tk.Entry(janela)
ent_pcx.configure(width=5)
ent_pcx.grid(row=4, column=1)
ent_pcy = tk.Entry(janela)
ent_pcy.configure(width=5)
ent_pcy.grid(row=4,column=2)

lab_amo = tk.Label(janela, text="Amostras:")
lab_amo.grid(row=5, column=0)
sca_amo = tk.Scale(janela, from_=1, to=10000, orient=tk.HORIZONTAL)
sca_amo.grid(row=5, column=1, columnspan=2)

fig = Canvas(width=500, height=500, bg='white')
fig.grid(row=1, column=3, rowspan=100)

but_ger = tk.Button(janela, text="Iniciar Geração", command=gerar)
but_ger.grid(row=8, column=0, columnspan=3)

but_lim = tk.Button(janela, text="Limpar Desenho", command=limpar)
but_lim.grid(row=9, column=0, columnspan=3)


tk.mainloop()
#---===[2 Fim da Geração da Janela]===---
