from matriz_dispersa import MatrizOrtogonal, ListaDoble
matrizortogonal=ListaDoble
class Main ():
    def __init__(self): 
        while True:
                x=input('''
        1. Iniciar programa
        2. Salir
        Escoja una opcion:''')
                if x =="1":
                    matrizortogonal.graficar_original(input("Nombre de la ciudad"))
                elif x =="2":
                    print("saliendo...")
                    break
                else:
                    print("Escoja un dato valido porfavor:")
a=Main()