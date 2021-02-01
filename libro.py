from funcionesBD import *

class Libro:
    def __init__(self, titulo, autor, editorial, idL = 0):
        self.idL = idL
        self.titulo = titulo
        self.autor = autor
        self.editorial = editorial
    def crearLib(self):
        conexion = conectar()
        insProd = "insert into libros (editorial, autor, titulo) values (%s,%s,%s);"
        data = (self.editorial, self.autor, self.titulo)
        c = ejecutar(insProd, data, conexion)
        cerrar(conexion)
    @staticmethod
    def disponible(libId):
        conexion = conectar()
        c2 = ejecutar("select * from retiros where libro_id = '"+str(libId)+"';", 0, conexion)
        cuenta = 0
        for elem2 in c2:
            cuenta = cuenta+1
        return cuenta
        
        cerrar(conexion)
    @staticmethod
    def listarLibros():
        conexion = conectar()
        c = ejecutar("select * from libros", 0, conexion)
        lRes = []
        lIds = []
        for elem in c:
            if Libro.disponible(elem[0]) == 0:
                tomado = "disponible"
            else:
                tomado = "PRESTADO"
            result = "Código: " + str(elem[0]) + " | Título: " + elem[3] + " | Autor: " + elem[2] + " | Editorial: " + elem[1] + " | Estado: " +tomado
            lRes.append(result)
            lIds.append(elem[0])
        return lRes, lIds
    @staticmethod
    def buscarPorId(docu):
        conexion = conectar()
        c = ejecutar("select * from libros where libro_id = '"+str(docu)+"';", 0, conexion)
        for elem in c:
            lector = Libro(elem[3], elem[2], elem[1], elem[0])
        cerrar(conexion)
        return lector    