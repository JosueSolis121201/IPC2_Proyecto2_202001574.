from os import sep
from xml.dom import minidom
from tkinter import Tk                               #Libreria para explorador de archivos (Se usara para leer data e instrucciones)
from tkinter.filedialog import askopenfilename

from matplotlib.pyplot import xkcd       #complemento para el explorador ^^^
from matriz_dispersa import MatrizOrtogonal , ListaDoble








class lectura():
    def __init__(self):
        self.lista = ListaDoble()
        self.nombre_robot=""
        
        self.analizarXML()

        nombre = input("ingrese nombre ")
        self.lista.graficar(nombre)

    def leerXML(self):
        Tk().withdraw()
        archivoxml=""
        try:
            filename = askopenfilename(title="Seleccione un archivo",
                                            filetypes=[("Archivos","*.xml"), 
                                                        ("All files","*")])
                                                        
            print(filename)
            with open(filename) as infile:
                archivoxml=infile.read().strip()       #limpia cualquier carracter "corrupto"
                return archivoxml

        except:
            print("no se selecciono ningun archivo")
            print("error")

    def analizarXML(self):
        doc = minidom.parseString(self.leerXML())
        ciudades = doc.getElementsByTagName("ciudad")
        robot = doc.getElementsByTagName("robot")
        matrizOrtogonal = MatrizOrtogonal()

        #robots aliados
       
        a = ""
        vida_robot_figther =0
        for robot in robot:
            nombre = robot.getElementsByTagName("nombre")
            for nombre in nombre:
                IDtipo  = nombre.getAttribute("tipo")
                nametag = robot.getElementsByTagName("nombre")[0].firstChild.data
                IDcapacidad  = nombre.getAttribute("capacidad")
                
                if IDtipo.lower()  == "chapinrescue" and a == 1:
                    print("Se encontro : " + nametag + " como chapinrescue")
                
               # print("IDtipo:%s" % IDtipo)
                if IDtipo.lower()  == "chapinfighter" and a == 2:
                    print("Se encontro : " + nametag + " como chapinfighter con capacidad de: "+ IDcapacidad)
        #self.nombre_robot = input("Nombre del robot que desea utilizar: ")

        #ciudades
        for ciudad in ciudades:
            matrizOrtogonal = MatrizOrtogonal()
            x=0
            nombres = ciudad.getElementsByTagName("nombre")
            #ID coluimna y fila
            for nombre in nombres:
                nombre_ciudad = ciudad.getElementsByTagName("nombre")[0].firstChild.data     
                matrizOrtogonal.nombre_ciudad = nombre_ciudad
                
                IDfilas  = nombre.getAttribute("filas")
                IDcolumnas  = nombre.getAttribute("columnas")
                
                print("nombre_ciudad: " + nombre_ciudad)
                """print("IDfilas:%s" % IDfilas)
                print("IDcolumnas:%s" % IDcolumnas)"""
            #Contenido de filas y enumeracion
            filas = ciudad.getElementsByTagName("fila")
            for fila in filas:
                fila_num=fila.getAttribute("numero")
                fila_texto = ciudad.getElementsByTagName("fila")[x].firstChild.data
                fila_texto_correjido = fila_texto.replace('\"','')
                contador_letra = 1
                for letra in fila_texto_correjido:
                    y = fila_num
                    if fila_texto_correjido=="2":
                        print("corregido",letra,sep=" ---- ")
                    matrizOrtogonal.insertarDato(str(letra),int(y),int(contador_letra)) 
                    contador_letra = contador_letra +  1
                x=x+1
               # print("num_fila:%s" % fila_num +"fila_texto:%s" % fila_texto )

            unidad_militar = ciudad.getElementsByTagName("unidadMilitar")
            for unidad_militar in unidad_militar:
                unidad_militar_vida = ciudad.getElementsByTagName("unidadMilitar")[0].firstChild.data     
                unidad_militar_posFila  = unidad_militar.getAttribute("fila")
                unidad_militar_poscolumna  = unidad_militar.getAttribute("columna")

                matrizOrtogonal.insertarDato(str(unidad_militar_vida),int(unidad_militar_posFila),int(unidad_militar_poscolumna))

                """print("unidad_militar_vida:%s" % unidad_militar_vida)
                print("unidad_militar_posFila:%s" % unidad_militar_posFila)
                print("unidad_militar_poscolumna:%s" % unidad_militar_poscolumna)"""
        
            self.lista.agregar(matrizOrtogonal)

        
        
     



                

        
          
        

            


            

        
            
a=lectura()