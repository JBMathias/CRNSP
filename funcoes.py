from Tkinter import *
from PyWANN.WiSARD import WiSARD
from pickle import *
from os import *
from loader2 import *
import cv2


#Destroi a janela quando o botao cancelar ao pressionado
def cancel(window):
    window.destroy()

###Pega o diretorio que foi provido pelo usuario
##def get_path():
##    path= diretory.get()
##    return path

###salvar configuracoes da wisard
##def salvando(wisard):
##    var={}
##
##    var[tam_retina]= wisard.tam_retina
##    var[num_bits_addr]= wisard.num_bits_addr
##    var[seed]= wisard.seed
##    var[discriminators]= wisard.discriminators
##    var[classes]= wisard.classes
##
##    nome_arq= get_path()
##    arquivo = open(nome_arq, "wb")
##    pickle.dump(var, arquivo)
##    arquivo.close()
    
    
def treino():
    #Carregar base de dados e configuracoes da wisard + binarizacao
    dados = MNIST('./')
    X,y = dados.load_training()
    X_test,y_test = dados.load_testing()


    
    #pegando as caracteristicas salvas
    nome_arq= get_path()
    arquivo= open(nome_arq, 'r')
    var= pickle.load(arquivo)

    #montando a wisard
    w= WiSARD(var[tam_retina], var[num_bits_addr])
    w.seed= var[seed]
    w.discriminators= var[discriminators]
    w.classes= var[classes]
    

    #Treinar(fit)
    w.fit(X,y)

    #Classificar(predict)

##def treino():
##    pasta= get_path()
##    classes= os.listdir(path)
