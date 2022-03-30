from pip import main
from matriz_dispersa import MatrizOrtogonal

class Main ():

    matrizOrtogonal = MatrizOrtogonal()
    matrizOrtogonal.insertarDato("juan.1-1",1,1)
    matrizOrtogonal.insertarDato("juan.5-5",5,5)
    matrizOrtogonal.recorrerMatriz()

a=Main()