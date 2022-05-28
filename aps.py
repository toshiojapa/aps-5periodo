#Importando Bicliotecas para criar a tela e 
import tkinter as tk
from tkinter import ttk

oJanela = tk.Tk()
#Dando o titulo da tela 
oJanela.title("Cadastro de Produtos")
#Ddefenindo as medidas da tela
oJanela.geometry("800x600")
#Definindo a cor de fundo da tela
oJanela.configure(background="#C0C0C0")
#Inserindo o texto para definir o titulo da entrada
oData = tk.Label(oJanela, text="Data da reclamação:", background="#C0C0C0", foreground="#000000", anchor='w')
#Definindo as medidas e posionamento do texto
oData.place(x=68, y=50, width=150, height=30)

oProduto = tk.Label(oJanela, text="Produto:", background="#C0C0C0", foreground="#000000", anchor='w')

oProduto.place(x=68, y=100, width=150, height=30)

































oJanela.mainloop()