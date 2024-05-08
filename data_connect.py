import sqlite3

# Conectar a la base de datos (creará la base de datos si no existe)
conn = sqlite3.connect('registros1.db')


if conn:

    # Crear un cursor para ejecutar comandos SQL
    cursor = conn.cursor()

    #Crear la tabla de categorías
    cursor.execute('''CREATE TABLE IF NOT EXISTS categorias (
                        idCategoria INTEGER PRIMARY KEY AUTOINCREMENT,
                        categoria TEXT
                    )''')

    #Crear la tabla de registro
    cursor.execute('''CREATE TABLE IF NOT EXISTS registro (
                        registro_id INTEGER PRIMARY KEY AUTOINCREMENT,
                        registro TEXT,
                        fechaRegistro TEXT,
                        fechaModificacion TEXT,
                        estatus TEXT,
    		    FOREIGN KEY (categoria_id) 
    	            REFERENCES categoria (categoria_id)
                    )''')

else:
    # Cerrar la conexión
    conn.close()

# Guardar los cambios
conn.commit()