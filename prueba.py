class elemento:
    def __init__(self,numero):
        self.siguiente = None
        self.anterior = None
        self.numero = numero


def prueba1():
    e1 = elemento(1)
    e2 = elemento(2)
    e3 = elemento(3)
    e4 = e3
    e5 = e4
    e3.numero = 10


    e1.siguiente = e2
    e2.siguiente = e3

    print(e3.numero)
    print(e4.numero)
    print(e5.numero)
    #print(e2.siguiente)

def prueba2():
    e1 = elemento(1)
    e2 = elemento(2)
    e3 = elemento(3)
    e4 = elemento(3)
    

    e1.siguiente = e2
    e2.siguiente = e3
    e3.siguiente = e4

    puntero = e1
    while puntero != None:
        print(puntero)
        puntero = puntero.siguiente
    
    print("afuera")
    print(e1)

def prueba3():
    e1 = elemento(1)
    e2 = elemento(2)
    e3 = elemento(3)
    e4 = elemento(3)
    

    e1.siguiente = e2
    e2.siguiente = e3
    e3.siguiente = e4

   
    print(e4)
    print(e1.siguiente.siguiente.siguiente)
def prueba4():
    e1 = elemento(1)
    e2 = elemento(2)
    e3 = elemento(3)
    e4 = elemento(3)
    

    e1.siguiente = e2
    e2.anterior = e1

   
    print(e2.anterior)
    print(e1.siguiente.anterior)

def prueba5():
    r="hola"
    contador=0
    for i in range(r):
        print(i)




prueba5()