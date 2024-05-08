import data_connect
import sqlite3
from datetime import datetime

conn = sqlite3.connect('registros1.db')

cursor = conn.cursor()


def select_admin(cursor):
	print("Selecciona todos los registros de la tabla - Modo Administrador")
	cursor.execute('''
		SELECT r.registro_id,
			r.registro,
			r.fechaRegistro,
			r.fechaModificacion,
			CASE WHEN r.estatus = 1 
			then 'Activo'
			else 'Borrado'
			END as estatus,
			c.categoria
			FROM registro r
			inner join categorias c on c.idCategoria = r.registro_id
			ORDER BY r.fechaRegistro DESC;
		''')
	# cursor.execute('''
	# 	select r.registro,r.fechaRegistro,DATETIME(r.fechaModificacion,'localtime'),
	# CASE WHEN r.estatus = 1 
	# then 'Activo'
	# else 'Inactivo'
	# END as estatus,
	# c.categoria
	# from registro r 
	# inner join categorias c on c.idCategoria = r.registro_id 
	# ORDER by r.fechaRegistro DESC
	#  ''')
	registros = cursor.fetchall()

	try:

		if registros > 0:
			for oneByOne in registros:
				print(f"Esto es: {oneByOne}")
	except:
		print("No se encontraron resultados")
		

def select_all(cursor):
	print("Selecciona todos los registros de la tabla")
	cursor.execute('''
		SELECT r.registro_id,
			r.registro,
			r.fechaRegistro,
			r.fechaModificacion,
			CASE WHEN r.estatus = 1 
			then 'Activo'
			else 'Borrado'
			END as estatus,
			c.categoria
			FROM registro r
			inner join categorias c on c.idCategoria = r.registro_id
			WHERE r.estatus != 2
			ORDER BY r.fechaRegistro DESC;
		''')
	# cursor.execute('''
	# 	select r.registro,r.fechaRegistro,DATETIME(r.fechaModificacion,'localtime'),
	# CASE WHEN r.estatus = 1 
	# then 'Activo'
	# else 'Inactivo'
	# END as estatus,
	# c.categoria
	# from registro r 
	# inner join categorias c on c.idCategoria = r.registro_id 
	# ORDER by r.fechaRegistro DESC
	#  ''')
	
	registros = cursor.fetchall()

	try:

		if registros > 0:
			for oneByOne in registros:
				print(f"Esto es: {oneByOne}")
	except:
		print("No se encontraron resultados")

	


def select_detalle():
	print("Selecciona el id X")



	id_a_buscar = 1
	id_a_buscar = int(input("Introduce el id de registro a buscar: "))
	cursor.execute('''
	select r.registro,r.fechaRegistro,
	CASE WHEN r.estatus = 1 
	then 'Activo'
	else 'Inactivo'
	END as estatus,
	c.categoria
	from registro r 
	inner join categorias c on c.idCategoria = r.registro_id 
	where r.registro_id = ?
	and r.estatus != 2''', (id_a_buscar,))
	resultado = cursor.fetchone()
	print(resultado)

def select_detalle_admin():
	print("Selecciona el id X")

	id_a_buscar = 1
	id_a_buscar = int(input("Introduce el id de registro a buscar: "))
	cursor.execute('''
	select r.registro,r.fechaRegistro,
	CASE WHEN r.estatus = 1 
	then 'Activo'
	else 'Borrado'
	END as estatus,
	c.categoria
	from registro r 
	inner join categorias c on c.idCategoria = r.registro_id 
	where r.registro_id = ?''', (id_a_buscar,))
	resultado = cursor.fetchone()
	print(resultado)


def insert_by_id():
	print("Inserta un registro")
	print("Actualiza un registro por id X")
	
	registro = input("Introduce Nuevo valor del registro: ")
	fechaRegistro = datetime.now().strftime('%Y-%m-%d %H:%M:%S')  # Fecha y hora actual
	estatus = int(input("Introduce número de estatus [1] Activo,[2] Inactivo: "))
	categoria_id = int(input("Introduce número de categoría [1,2,3]: "))

	# ID del registro que queremos actualizar

	"""
	 fecha_actual = datetime.now().strftime('%Y-%m-%d %H:%M:%S')  # Obtener fecha y hora actual
    
    # Sentencia SQL para realizar la inserción
    sql = '''INSERT INTO registros (registro, fechaRegistro, fechaModificacion, estatus, categoria_id)
             VALUES (?, ?, ?, ?, ?)'''
    
    # Valores para la inserción
    valores = (registro, fecha_actual, fecha_actual, estatus, categoria_id)

	"""
	

	# Sentencia SQL para actualizar los campos en la tabla
	sql = '''INSERT INTO registro (registro, fechaRegistro, fechaModificacion, estatus, categoria_id)
             VALUES (?, ?, ?, ?, ?)'''
	# Ejecutar la sentencia SQL con los nuevos valores
	valores = (registro, fechaRegistro,'', estatus, categoria_id)
	cursor.execute(sql, valores)
	# Confirmar la Inserción a la base de datos
	conn.commit()
	


def update_by_id():
	print("Actualiza un registro por id X")
	registro_id = int(input("Introduce el número de id de registro: "))
	registro = input("Introduce Nuevo valor del registro: ")
	fechaModificacion = datetime.now().strftime('%Y-%m-%d %H:%M:%S')  # Fecha y hora actual
	estatus = int(input("Introduce número de estatus [1] Activo,[2] Inactivo: "))
	categoria_id = int(input("Introduce número de categoría [1,2,3]: "))

	# ID del registro que queremos actualizar
	

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
	

	print("¡Actualización completada!")





	# id_a_actualizar = int(input("Introduce el id de registro a Actualizar : "))
	# registro = input("Introduce el registro : ")
	# #fechaRegistro = ''
	# estatus = int(input("Introduce el número de estatus: [1] Activo, [2] Inactivo: "))
	# categoria_id = int(input("""Introduce el número de categoría: 1,2,3,ETC.: """))
	# #id_a_actualizar = 1
	# cursor.execute('''UPDATE registro 
	# 				SET registro = ?,
	# 				fechaModificacion = DATETIME(CURRENT_TIMESTAMP,'localtime'),
	# 				estatus = ?, 
	# 				categoria = ? WHERE registro_id = ?''', 
	# 				(id_a_actualizar,registro,'','',estatus,categoria_id, ))


def delete_by_id():
	print("Borra un registro por id X")
	"""
	Hacer TRUNCATE(VACIAR CONTENIDO DE UNA TABLA SQLITE)
	delete from `TABLE`; 
	update sqlite_sequence set seq=0 where name=`TABLE`;

	"""
	registro_id = int(input("Introduce el número de id de registro: "))
	estatus = 2
	fechaModificacion = datetime.now().strftime('%Y-%m-%d %H:%M:%S')  # Fecha y hora actual

	# ID del registro que queremos actualizar
	

	# Sentencia SQL para actualizar los campos en la tabla
	sql = '''UPDATE registro
	         SET fechaModificacion = ?,estatus = ?
	         WHERE registro_id = ?'''

	# Ejecutar la sentencia SQL con los nuevos valores
	valores = (fechaModificacion,estatus, registro_id)
	cursor.execute(sql, valores)

	# Confirmar la actualización de la base de datos
	conn.commit()

	# Cerrar la conexión con la base de datos
	

	print("¡Actualización completada!")


def menu():
	while True:
		print("""
			MENÚ:
			¿Bienvenido: Qué desea hacer?

			[0] SELECCIONAR TODOS LOS REGISTROS - MODO ADMIN
			[1] SELECCIONAR TODOS LOS REGISTROS
			[2] INSERTAR UN REGISTRO
			[3] BUSCAR UN REGISTRO
			[30] BUSCAR UN REGISTRO
			[4] ACTUALIZAR UN REGISTRO
			[5] BORRAR UN REGISTRO
			[6] SALIR DEL SISTEMA
	 """)

		op = int(input("Elige una opción del 1 - 6: "))	


		if op == 0:
			print("Eligió la opción [0] SELECCIONAR TODOS LOS REGISTROS - MODO ADMIN")
			select_admin(cursor)

		if op == 1:
			print("Eligió la opción [1] SELECCIONAR TODOS LOS REGISTROS")
			select_all(cursor)

		elif op == 2:
			print("Eligió la opción [2] INSERTAR UN REGISTRO")
			insert_by_id()
			
			
		elif op == 3:
			print("Eligió la opción [3] BUSCAR UN REGISTRO")
			select_detalle()

		elif op == 30:
			print("Eligió la opción [3] BUSCAR UN REGISTRO")
			select_detalle_admin()

		elif op == 4:
			print("Eligió la opción [4] ACTUALIZAR UN REGISTRO")
			update_by_id()

		elif op == 5:
			print("Eligió la opción [5] BORRAR UN REGISTRO")
			delete_by_id()

		elif op == 6:
			print("Eligió la opción [6] SALIR DEL SISTEMA")
			print("Ha elegido Salir del sistema")
			conn.close()
			break

		else:
			print(f"--- Opción: {op} inválida  ---")
			




if __name__ == "__main__":	

	menu()



