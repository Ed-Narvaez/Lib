import psycopg2
from psycopg2 import Error
        
def conectar():
    try:
        # Connect to an existing database
        connection = psycopg2.connect(user="postgres",
                                      password="124675",
                                      host="127.0.0.1",
                                      port="5432",
                                      database="postgres")

        cursor = connection.cursor()

        cursor.execute("SELECT version();")
 
        record = cursor.fetchone()
        
        return connection
    except (Exception, Error) as error:
        print("Error while connecting to PostgreSQL", error)
def cerrar(con):
    miCur = con.cursor()
    miCur.close()
    con.close()
    return("Conexión finalizada")

def ejecutar(estrTabla, datos, con):

    try:
        estrTabla = estrTabla.lower()
        
            
        curs = con.cursor()
        if("select" in estrTabla):
            curs.execute(estrTabla)
        else:
            curs.execute(estrTabla, datos)
        con.commit()
        return curs
    except (Exception, psycopg2.Error) as error :
        if(con):
            print("Error en tiempo de ejecución, reinicie el programa. A programador: ", error)
