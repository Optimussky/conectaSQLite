import sqlite3
from datetime import datetime

# Conectarse a la base de datos (o crearla si no existe)
conn = sqlite3.connect('registros1.db')
cursor = conn.cursor()

# Definir los nuevos valores que queremos actualizar
registro = input("Introduce Nuevo valor del registro: ")
fechaModificacion = datetime.now().strftime('%Y-%m-%d %H:%M:%S')  # Fecha y hora actual
estatus = int(input("Introduce número de estatus [1] Activo,[2] Inactivo: "))
categoria_id = int(input("Introduce número de estatus [1,2,3]: "))

# ID del registro que queremos actualizar
registro_id = int(input("Introduce el número de id de registro: "))

# Sentencia SQL para actualizar los campos en la tabla
sql = '''UPDATE registro
         SET registro = ?,
             fechaModificacion = ?,
             estatus = ?,
             categoria_id = ?
         WHERE registro_id = ?'''

# Ejecutar la sentencia SQL con los nuevos valores
valores = (registro, fechaModificacion, estatus, categoria_id, registro_id)
cursor.execute(sql, valores)

# Confirmar la actualización de la base de datos
conn.commit()

# Cerrar la conexión con la base de datos
conn.close()

print("¡Actualización completada!")