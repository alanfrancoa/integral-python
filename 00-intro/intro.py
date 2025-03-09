# ------------------ TALLER DE PYTHON (UNLZ) ------------------
# CLASE: 
# PROFESOR: GABRIEL NIGLIO
# CUATRIMESTRE: 1ER CUATRIMESTRE
# AÑO: 2025
# 

# ------------------------- [COMENTARIOS] -------------------------

# Para comentar en una sola linea, se utiliza #. 

'''
Un metodo alternativo para el comentario multilinea, es el uso de comillas triples.
Aunque no es de uso oficial, nos permite comentar.
'''

# ------------------------- [MOSTRAR POR PANTALLA] -------------------------

# En Python la función print() se utiliza para imprimir en la consola ya sea un texto, numeros y variables.
print("Hola mundo!")

# Para imprimir más de un valor, utilizaremos la concatenacion. 

mascota = "cabra"
nombre = "GOAT"


# 1ra forma de Concatenación: UNIÓN
print(mascota + " " + nombre)

# 2da forma de Concatenación: INTERPOLACIÓN
print(f"{mascota} {nombre}") 

# Debido a la interpolación podemos insertar valores en un string
print(f"Mi {mascota} se llama {nombre}") 


# ------------------------- [SINTAXIS] -------------------------

'''
La sintaxis de Python es sencilla, las características principales para escribir el codigo son:
    - No se usan llaves {} para bloques de código
    - No es necesario el uso del punto y coma (;)
    - La IDENTACIÓN es fundamental en Python!!!

if True: 
    print("Este bloque está indentado correctamente")  <--- Se debe usar la misma indentación

Error si la indentación es incorrecta:

if True:
print("Error de indentación") <--- ERROR de indentación

'''