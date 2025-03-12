# ------------------ TALLER INTEGRADOR DE PYTHON (UNLZ) ------------------
# CLASE: 
# PROFESOR: GABRIEL NIGLIO
# CUATRIMESTRE: 1ER CUATRIMESTRE
# AÑO: 2025
# 

# ------------------------- [OPERADORES LÓGICOS] -------------------------

'''
Los operadores lógicos se usan en estructuras condicionales para combinar dos o más comparaciones. Dependiendo del operador, nos devolverán un valor booleano (True o False). Los operadores lógicos son:

- and: Todas las condiciones deben ser verdaderas. Si alguna no lo es, el resultado final será False.
- or: Con que una condición sea verdadera, el resultado final será True.
- not: Invierte el valor de la comparación (True -> False, False -> True).
'''

# Definimos dos variables para los ejemplos
a = 7
b = 12

# ------------------------- [AND] -------------------------
'''
Ejemplo de AND:

- a > 5: Esta comparación es True.
- b < 15: Esta comparación es True.

Al usar AND, ambas comparaciones deben ser True para que el resultado final sea True.
'''
print("AND:", a > 5 and b < 15)  # True

# ------------------------- [OR] -------------------------
'''
Ejemplo de OR:

- a == 10: Esta comparación es False.
- b >= 10: Esta comparación es True.

Al usar OR, basta con que una de las comparaciones sea True para que el resultado final sea True.
'''
print("OR:", a == 10 or b >= 10)  # True

# ------------------------- [NOT] -------------------------
'''
Ejemplo de NOT:

- a < b: Esta comparación es True.

El operador NOT invierte el valor de la comparación. Si la comparación es True, NOT la convierte en False, y viceversa.
'''
print("NOT:", not(a < b))  # False