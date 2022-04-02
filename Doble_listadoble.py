class Nodo:
    def __init__(self, dato):
        self.dato = dato
        #coordenadas
        self.siguiente = None
        self.anterior = None
        

class ListaDoble_X:
    def __init__(self):
        #apuntadores
        self.derecha = None
        self.izquierda = None

    def agregar(self, dato):
        nuevoNodo = Nodo(dato)
       #Validamos si la lista esta vacia
        if self.derecha == None:
            self.derecha = nuevoNodo
            self.izquierda = nuevoNodo
        #Si por lo menos hay un nodo, insertamos al inicio
        else:
            self.derecha.anterior = nuevoNodo
            nuevoNodo.siguiente = self.derecha
            self.derecha = nuevoNodo
            
    
ListaDoble_X()

    