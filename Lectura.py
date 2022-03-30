from xml.dom import minidom
from tkinter import Tk                               #Libreria para explorador de archivos (Se usara para leer data e instrucciones)
from tkinter.filedialog import askopenfilename

from matplotlib.pyplot import xkcd       #complemento para el explorador ^^^







class lectura():
    def __init__(self):
        
        self.analizarXML()

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
        ciudad = doc.getElementsByTagName("ciudad")
        robot = doc.getElementsByTagName("robot")

        #ciudades
        for ciudad in ciudad:
            x=0
            nombre = ciudad.getElementsByTagName("nombre")
            #ID coluimna y fila
            for nombre in nombre:
                nombre_ciudad = ciudad.getElementsByTagName("nombre")[0].firstChild.data     
                IDfilas  = nombre.getAttribute("filas")
                IDcolumnas  = nombre.getAttribute("columnas")
                print("nombre_ciudad:%s" % nombre_ciudad)
                print("IDfilas:%s" % IDfilas)
                print("IDcolumnas:%s" % IDcolumnas)
            fila = ciudad.getElementsByTagName("fila")



            for fila in fila:
                fila = ciudad.getElementsByTagName("fila")[x].firstChild.data
                #num_fila=ciudad.getAttribute("numero")
                x=x+1
                print("fila:%s" % fila )
                #print("num_fila:%s" % num_fila)
        #robots
        for robot in robot:
            nombre = robot.getElementsByTagName("nombre")
            for nombre in nombre:
                nametag = robot.getElementsByTagName("nombre")[0].firstChild.data
                print("nametag:%s" % nametag)
                IDtipo  = nombre.getAttribute("tipo")
                IDcapacidad  = nombre.getAttribute("capacidad")
                print("IDtipo:%s" % IDtipo)
                if IDcapacidad != "":
                    print("IDcapacidad:%s" % IDcapacidad)
                
                

        
          
        

            


            

        
            
a=lectura()