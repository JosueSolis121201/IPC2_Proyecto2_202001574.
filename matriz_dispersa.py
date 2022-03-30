from graphviz import Digraph

class nodo:
    def __init__(self):
        self.dato=None
        #Coordenadas
        self.posVertical =None
        self.posHorizontal =None
        #Apuntadores
        self.arriba =None
        self.abajo=None
        self.izquierda =None
        self.derecha =None

class matrizOrtogonal:
    def __init__(self):
        #crear nodo raiz
        self.raiz = nodo()
        self.raiz.posVertical=0
        self.raiz.posHorizontal=0

    def crearIndiceVertical(self,posocion):
        #recorrer nodos de manera vertical 
        #crear un temporal
        #tmp=temporal
        tmp = self.raiz
        while tmp != None:
            #No existe el indice, solo hay menores
            if tmp.abajo == None and tmp.posVertical < posocion:
                #ya no hay mas nodos verticales
                #insertarlo al final
                nuevo=nodo()
                nuevo.posVertical = posocion
                nuevo.posHorizontal =0      #<--- debido a que esta en la cabecera
                nuevo.arriba = tmp # donde venia
                tmp.abajo = nuevo
                return  tmp.abajo
            #indice actual es igual al nuevo
            if  tmp.posVertical == posocion:
                #no hacer nada
                return tmp

            #indice actual es el menor y el siguiente es el mayor( en medio)
            if tmp.posVertical < posocion and tmp.abajo.posVertical > posocion:
                #insertar nodo en meido del acutal y abajo 
                nuevo = nodo()
                nuevo.posHorizontal = 0
                nuevo.posVertical = posocion
                # asignar abajo y arriba para el  nuevo
                nuevo.abajo = tmp.abajo
                nuevo.arriba=tmp
                tmp.abajo.arriba = nuevo
                tmp.abajo = nuevo
                return tmp.abajo
            #pasar al siguiente nodo de abajo si no cumplio ninguna validacion
            tmp= tmp.abajo

    def crearIndiceHorizontal(self,pos):
        #recorrer los nodos ( horizontal)
        tmp=self.raiz
        while tmp != None:
            #no existe el nodo de la posicion
            if tmp.derecha == None and tmp.posHorizontal < pos:
                #ya no hay nodos al final insertar al final
                nuevo= nodo()
                nuevo.posHorizontal = pos 
                nuevo.posVertical = 0
                #enlace
                nuevo.izquierda =tmp
                tmp.derecha = nuevo 
                return tmp.derecha
            #indice actual es igual al nuevo 
            if tmp.posHorizontal == pos:
                # no hacer nada
                return tmp
            #indice actual es menor , pero pero siguiente   mayor ( caso tipo posicionar en medio)
            if tmp.posHorizontal < pos and tmp.derecha.posHorizontal >pos:
                # se inserta en medio
                nuevo= nodo()
                nuevo.posHorizontal= pos
                nuevo.posVertical =0
                #asignar apuntadores 
                nuevo.derecha = tmp.derecha
                nuevo.izquierda=tmp
                tmp.derecha.izquierda = nuevo
                tmp.derecha = nuevo
                return tmp.derecha
        # no encontro nodo pasar al siguiente para que no se encicle indefinidamente    
        tmp= tmp.derecha
    
    def insertarVertical(self, nodo, indiceHorizontal): #indiceHorizontal es de tipo nodo
        #recorrer nodo de forma horizontal 
        tmp=indiceHorizontal
        while tmp != None:
            #no existe el nodo, esta hasta el final 
            if tmp.abajo ==None and tmp.posVertical < nodo.posVertical:
                #ya no hay nodos abajo
                nodo.arriba = tmp
                tmp.abajo = nodo
                return tmp.abajo 
            #indice actual es igual al nuevo nodo
            if tmp.posVertical == nodo.posVertical:
                #no hacer nada, se sobre escribe 
                tmp.dato = nodo.dato
                return tmp

            #indice actual es menor y el siguiente es mayor
            if tmp.posVertical < nodo.posVertical and tmp.abajo.posVertical > nodo.posVertical:
                
                nodo.abajo = tmp.abajo
                nodo.arriba = tmp
                tmp.abajo.arriba =nodo
                tmp.abajo = nodo
            # pasar al siguiente nodo
            tmp= tmp.abajo
    
    def insertarHorizontal(self, nodo,indiceVertical ):#indiceVertical es de tipo nodo
        #recorrer los nodos
        tmp=indiceVertical
        while tmp != None:
            if tmp.derecha == None and tmp.posHorizontal < nodo.posHorizontal:
                nodo.izquierda = tmp
                tmp.derecha = nodo 
                return tmp.derecha

            if tmp.posHorizontal == nodo.posHorizontal:
                tmp.dato = nodo.dato
                return tmp
            if tmp.posHorizontal < nodo.posHorizontal and tmp.derecha.posHorizontal > nodo.posHorizontal:
                nodo.derecha = tmp.derecha 
                nodo.izquierda = tmp
                tmp.derecha.izquierda = nodo
                tmp.derecha = nodo
                return tmp.derecha
            tmp= tmp.derecha

    def insertarDato(self, dato,posVertical, posHorizontal):
        #crear cabeceras
        indiceVertical = self.crearIndiceVertical(posVertical)
        indiceHorizontal =self.crearIndiceHorizontal(posHorizontal)

        nuevoDato = nodo()
        nuevoDato.posHorizontal = posHorizontal
        nuevoDato.posVertical = posVertical
        nuevoDato.dato = dato

        self.insertarVertical(nuevoDato,indiceHorizontal)
        self.insertarHorizontal(nuevoDato,indiceVertical)
        print("nodo incertado.....")

    def recorrerMatriz(self):
        print("Graficando lista...")
        
        dot = Digraph('G', filename='dot', engine='dot',format='svg')
        dot.node_attr.update(shape="box")
        dot.attr(rankdir = "TB")
        contSubgrap = 1
        
        #iniciamos en el nodo raiz
        tmpV = self.raiz

        #vamos bajando en vertical
        while tmpV != None:
            tmpH = tmpV

            #creamos subgrafos para alinearlos            
            c = Digraph('child'+str(contSubgrap))
            c.attr(rank='same')
            contSubgrap += 1

            #nos vamos a la derecha 
            while tmpH != None:
                self.graficarNodos(c, tmpH)
                tmpH = tmpH.derecha

            #se termino una fila, agregamos el subgrafo
            dot.subgraph(c)
            tmpV = tmpV.abajo


        #vuelvo a recorrer para mostrar las flechas
        tmpV = self.raiz
        #vamos bajando en vertical
        while tmpV != None:
            tmpH = tmpV

            #nos vamos a la derecha 
            while tmpH != None:
                self.graficarFlechas(dot, tmpH)
                tmpH = tmpH.derecha

            tmpV = tmpV.abajo
        dot.view()
        pass

    def graficarNodos(self, grafo, nodoE):
        
        nodo = nodoE
        id = str(nodo.posVertical)+"_"+str(nodo.posHorizontal)
        grafo.node(id, nodo.dato,group=str(nodo.posHorizontal))
        

    def graficarFlechas(self, grafo, nodoE):
        nodo = nodoE
        id = str(nodo.posVertical)+"_"+str(nodo.posHorizontal)
        if nodo.posVertical != 0 and nodo.posHorizontal != 0:
            #Graficamos la flecha vertical
            idV1 = nodo.arriba.posVertical
            idV2 = nodo.arriba.posHorizontal
            idV = str(idV1)+"_"+str(idV2)
            grafo.edge(idV, id)
            grafo.edge(id, idV)

            #Ahora graficamos la flecha horizontal
            idH1 = nodo.izquierda.posVertical
            idH2 = nodo.izquierda.posHorizontal
            idH = str(idH1)+"_"+str(idH2)
            grafo.edge(idH,id)
            grafo.edge(id,idH)
        elif nodo.posVertical == 0 and nodo.posHorizontal != 0:
            #es una cabecera horizontal
            idAnterior = str(nodo.izquierda.posVertical)+"_"+str(nodo.izquierda.posHorizontal)
            grafo.edge(idAnterior, id)   
        elif nodo.posHorizontal == 0 and nodo.posVertical != 0:
            #es una cabecera vertical
            idAnterior = str(nodo.arriba.posVertical)+"_"+str(nodo.arriba.posHorizontal)
            grafo.edge(idAnterior, id)
        pass
                             













                 





         

