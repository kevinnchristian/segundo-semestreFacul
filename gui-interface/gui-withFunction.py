from tkinter import Tk, Label, Button
from tkinter.messagebox import showinfo  # Janela que informa data e hora
from time import strftime, localtime  # Obter data e hora e formatar na tela para o usuário

def clicked():
    time = strftime('Day: %d %b %Y \nTime: %H:%M:%S%p \n', localtime())  # Pegando a data e hora, no formato indicado
    showinfo(message=time)  # Exibir a informão

root = Tk()
button = Button(root, text='Clique', command=clicked)  # Criando botão com função
button.pack()

root.mainloop()