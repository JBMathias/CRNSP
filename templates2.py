from Tkinter import *
from funcoes import cancel, treino


def main_window():
    
    root = Tk()
    root.title("CRNSP")
    root.geometry("500x500")

    mainframe= Frame(root)
    mainframe.grid()
        
    textframe = Frame(mainframe)
    textframe.grid(row= 1)
    
    buttonframe = Frame(mainframe)
    buttonframe.grid(row= 2)
    
    texto= Text(textframe, height=2, width=80, )
    texto.insert("1.0", "Bem Vindo ao classificador generico.\nTenha certeza de ter lido as instrucoes antes de proseguir.")
    texto.grid()
    
    new_button= Button(buttonframe, text= "Novo", command= train_window)
    new_button.grid(row= 1, column= 2)
    
    open_button= Button(buttonframe, text= "Abrir", command= load_window)
    open_button.grid(row= 1, column = 3)

    root.mainloop()

def train_window():
    sub= Toplevel()
    sub.title("Treino")
    
    diretory_name= StringVar()
    diretory= Entry(sub, textvariable= diretory_name)
    diretory.grid()

    train_button= Button(sub, text= "Treinar", command= lambda:treino())
    train_button.grid()

    cancel_button= Button(sub, text="Cancelar", command= lambda: cancel(sub))
    cancel_button.grid()

def load_window():
    load_window= Toplevel()
    load_window.title("Abrir")
        
    diretory_name= StringVar()
    diretory= Entry(load_window, textvariable= diretory_name)
    diretory.grid()

    train_button= Button(load_window, text= "Abrir")
    train_button.grid()

    cancel_button= Button(load_window, text="Cancelar", command= lambda: cancel(load_window))
    cancel_button.grid()

def clas_window():
    clas= Toplevel()
    clas.title("Classificar")
    
    diretory_name= StringVar()
    diretory= Entry(clas, textvariable= diretory_name)
    diretory.grid()

    train_button= Button(clas, text= "Classificar")
    train_button.grid()

    cancel_button= Button(clas, text="Cancelar")
    cancel_button.grid()

def save_window():
    load_window= Toplevel()
    load_window.title("Salvar")
        
    diretory_name= StringVar()
    diretory= Entry(load_window, textvariable= diretory_name)
    diretory.grid()

    train_button= Button(load_window, text= "Salvar")
    train_button.grid()

    cancel_button= Button(load_window, text="Cancelar")
    cancel_button.grid()
