from funcionesBD import *
from libro import Libro
class Lector:
    def __init__(self, dni, nombre, apellido, id = 0, lista=0):
        self.id = id
        self.listaPrestamos = []
        if lista!=0:
            self.listaPrestamos = lista
        self.documento = dni
        self.nombre = nombre
        self.apellido = apellido
    def crearLector(self):
        conexion = conectar()
        insProd = "insert into lectores (nombre, apellido, documento) values (%s,%s,%s);"
        data = (self.nombre, self.apellido, self.documento)
        c = ejecutar(insProd, data, conexion)
        cerrar(conexion)
    @staticmethod
    def buscarPorDoc(docu):
        conexion = conectar()
        c = ejecutar("select * from lectores where documento = '"+str(docu)+"';", 0, conexion)
        c2 = ejecutar("select libros.libro_id, libros.titulo, libros.editorial, libros.autor from lectores inner join retiros on retiros.lector_id = lectores.lector_id inner join libros on retiros.libro_id = libros.libro_id where documento ='"+str(docu)+"';", 0, conexion)
        listaLibros = []
        for elem2 in c2:
            miLib = Libro(elem2[1], elem2[3], elem2[2], elem2[0])
            listaLibros.append(miLib)
        for elem in c:
            lector = Lector(elem[3], elem[1], elem[2], elem[0], listaLibros)
        cerrar(conexion)
        return lector
    @staticmethod
    def verLectores(opc=0):
        conexion = conectar()
        if opc == 0:
            c = ejecutar("select * from lectores", 0, conexion)
        else:
            c = ejecutar("select * from lectores inner join retiros on retiros.lector_id = lectores.lector_id", 0, conexion)
        lRes = []
        lDocs = []
        for elem in c:
            result = "Documento: " + str(elem[3]) + " | Nombre: " + elem[1] + " | Apellido: " + elem[2]
            lDocs.append(elem[3])
            lRes.append(result)
        return lRes, lDocs
    
    def tomarPrestado(self, idL):
        conexion = conectar()
        self.listaPrestamos.append(idL)
        insPres = "insert into retiros (lector_id, libro_id) values (%s,%s);"
        data = (self.id, idL.idL)
        c = ejecutar(insPres, data, conexion)
        cerrar(conexion)
    def devolverLibro(self, idL):
        conexion = conectar()
        nuevaLista = []
        for i in range(len(self.listaPrestamos)):
            if self.listaPrestamos[i].idL != idL:
                nuevaLista.append(self.listaPrestamos[i])
        self.listaPrestamos = nuevaLista
        
        insPres = "delete from retiros where libro_id = %s and lector_id = %s;"
        data = (idL.idL, self.id)
        c = ejecutar(insPres, data, conexion)
        cerrar(conexion)
    def verLibros(self):
        return self.listaPrestamos
        