from libro import Libro
from lector import Lector
from funcionesBD import *
conexion = conectar()

print("------ MENU BIBLIOTECA:-------\n 1 - Cargar libro nuevo\n 2 - Listar libros \n 3 - Cargar lector \n 4 - Registrar préstamo\n 5-Registrar devolución\n 6- Ver libros por usuario \n 7 - Salir")
opc = int(input(""))
while opc!=7:
    if opc == 1:
        print("Ingrese título del nuevo libro:")
        titLib = input("")
        print("Ingrese autor:")
        autLib = input("")
        print("Ingrese editorial:")
        edLib = input("")
        
        miLib = Libro(titLib, autLib, edLib)
        miLib.crearLib()
        print("Libro cargado con éxito")
    elif opc == 2:
        print("Listado de libros:")
        lista, ids = Libro.listarLibros()
        for i in range(len(lista)):
            print(lista[i])
    elif opc == 3:
        print("Ingrese documento del lector:")
        docu = int(input(""))
        print("Ingrese nombre:")
        nom = input("")
        print("Ingrese apellido:")
        ape = input("")
        lec = Lector(docu, nom, ape)
        lec.crearLector()
        print("Lector cargado con éxito")
    elif opc == 4:
        print("Listado de lectores registrados")
        lista, docs = Lector.verLectores()
        for i in range(len(lista)):
            print(lista[i])
        print("Ingrese documento del lector a quien desea cargarle un nuevo préstamo :")
        docTarg = int(input(""))
        while docTarg not in docs:
            print("Documento inválido, ingrese nuevamente...")
            docTarg = int(input(""))
        miLec = Lector.buscarPorDoc(docTarg)
        lista, ids = Libro.listarLibros()
        print("Ingrese el código del libro que desea retirar (si lo necesita, mire la lista en el menú principal) o 0 (CERO) para dejar de registrar:")
        codLib = int(input(""))
        while codLib !=0:
            while codLib not in ids:
                print("Código inexistente, ingrese otro...")
                codLib = int(input(""))
            dispo = Libro.disponible(codLib)
            if dispo == 1:
                print("Lamentablemente ese libro ya se encuentra retirado")
            else:
                miLib = Libro.buscarPorId(codLib)
                #print(miLib)
                miLec.tomarPrestado(miLib)
                print("Retiro registrado con éxito")
                
            print("Ingrese el código del libro que desea retirar (si lo necesita, mire la lista en el menú principal) o 0 (CERO) para dejar de registrar:")
            codLib = int(input(""))
    elif opc == 5:
        print("Listado de lectores registrados que tienen libros retirados:")
        lista, docs = Lector.verLectores(1)
        for i in range(len(lista)):
            print(lista[i])
        print("Ingrese documento del lector de quien desea registrar una devolución:")
        docTarg = int(input(""))
        while docTarg not in docs:
            print("Documento inválido, ingrese nuevamente...")
            docTarg = int(input(""))
        miLec = Lector.buscarPorDoc(docTarg)
        print("Libros retirados por este lector:")
        miL = miLec.verLibros()
        for i in range(len(miL)):
            print ("Código: " +str(miL[i].idL))
        print("Ingrese el código que desea devolver:")
        miCod = int(input(""))

        libroHallado = Libro.buscarPorId(miCod)
        miLec.devolverLibro(libroHallado)
        print("Devolucion registrada con éxito...")
    elif opc == 6:
        print("Listado de lectores:")
        listaLec, lid = Lector.verLectores()
        for i in range(len(listaLec)):
            print(listaLec[i])
        print("Ingrese un documento para ver sus libros retirados...")
        miDoc = int(input(""))
        while miDoc not in lid:
            print("Ingrese nuevamente...")
            miDoc = int(input(""))
        miLec = Lector.buscarPorDoc(miDoc)
        listaLibros = miLec.verLibros()
        for i in range(len(listaLibros)):
            print ("Código: " +str(listaLibros[i].idL)+ " | Título:  "+listaLibros[i].titulo + " | Autor: "+listaLibros[i].autor + " | Editorial: "+listaLibros[i].editorial)
            
        

        
        
        
    print("------ MENU BIBLIOTECA:-------\n 1 - Cargar libro nuevo\n 2 - Listar libros \n 3 - Cargar lector \n 4 - Registrar préstamo\n 5-Registrar devolución\n 6- Ver libros por usuario \n 7 - Salir")
    opc = int(input(""))
cerrar(conexion)