from tkinter import *
from os import *

from algoritmoQuineMcClusky import *

def abrirVentanaError(ventanaPrincipal):
    ventanaError = Toplevel(ventanaPrincipal)
    ventanaError.geometry('300x100')
    ventanaError.resizable(False, False)
    ventanaError.title('Error')
    labelError = Label(ventanaError, text="Error en los mintérminos colocados.\nInténtelo nuevamente.", font=("Arial",10)).pack(pady=(30,0))
    ventanaError.mainloop

def ejecutarAlgoritmoQuineMcClusky(ventanaPrincipal, numeroVariables, sumaMinterminos):
    posiblesMinterminos = []
    for posibleMintermino in range(0, 2**int(numeroVariables)):
        posiblesMinterminos.append(posibleMintermino)
    minterminoInvalido = False
    minterminosColocados = []
    for minterminoColocado in sumaMinterminos.split(","):
        try:
            if int(minterminoColocado) in posiblesMinterminos:
                minterminosColocados.append(int(minterminoColocado))
            else:
                minterminoInvalido = True
        except:
            minterminoInvalido = True
    if (minterminoInvalido):
        abrirVentanaError(ventanaPrincipal)
    else:
        resultado = algoritmoQuineMcClusky(cantidadVariables, sumaMinterminos)
        print(resultado)

def definirCaracteristicasVentanaPrincipal(ventanaPrincipal):
    ventanaPrincipal.geometry('400x350')
    ventanaPrincipal.resizable(False, False)
    ventanaPrincipal.title('Proyecto I - EL3307')

def agregarComponentesVentanaPrincipal(ventanaPrincipal):
    labelTitulo = Label(ventanaPrincipal, text="Algoritmo Quine-McClusky", font=("Arial",15)).pack(pady=(10,0))
    labelNumeroVariables = Label(ventanaPrincipal, text="Seleccione el número de variables:", font=("Arial",10)).pack(pady=(20,0))
    variableNumeroVariables = StringVar(ventanaPrincipal, "4")
    botonCuatroVariables = Radiobutton(ventanaPrincipal, text="4 variables", variable=variableNumeroVariables, value="4").pack()
    botonCincoVariables = Radiobutton(ventanaPrincipal, text="5 variables", variable=variableNumeroVariables, value="5").pack()
    botonSeisVariables = Radiobutton(ventanaPrincipal, text="6 variables", variable=variableNumeroVariables, value="6").pack()
    labelSumaMinterminos = Label(ventanaPrincipal, text="Coloque los mintérminos (separados por coma):", font=("Arial",10)).pack(pady=(20,0))
    entrySumaMinterminos = Entry(ventanaPrincipal, width=40)
    entrySumaMinterminos.pack(pady=(10,0))
    botonEjecutarAlgoritmoQuineMcClusky = Button(ventanaPrincipal, text="Ejecutar algoritmo Quine-McClusky", command=lambda:ejecutarAlgoritmoQuineMcClusky(ventanaPrincipal,variableNumeroVariables.get(),entrySumaMinterminos.get())).pack(pady=(30,0))
    botonCompararAlgoritmosQuineMcCluskyExpresso = Button(ventanaPrincipal, text="Comparar algoritmos Quine-McClusky con Expresso", command=lambda:compararAlgoritmosQuineMcCluskyExpresso()).pack(pady=(10,0))

def main():
    ventanaPrincipal = Tk()
    definirCaracteristicasVentanaPrincipal(ventanaPrincipal)
    agregarComponentesVentanaPrincipal(ventanaPrincipal)
    ventanaPrincipal.mainloop()

main()