# ------------------ TALLER INTEGRADOR DE PYTHON (UNLZ) ------------------
# CLASE: 
# PROFESOR: GABRIEL NIGLIO
# CUATRIMESTRE: 1ER CUATRIMESTRE
# AÑO: 2025
# 

# ------------------------- [OPERADORES DE ASIGNACIÓN] -------------------------

'''
Los operadores de asignación permiten asignar un valor a una variable. Además, algunos operadores combinan una operación matemática con la asignación. Los operadores de asignación son:

- Igual (=)
- Incremento (+=)
- Decremento (-=)
- Multiplica y asigna (*=)
- Divide y asigna (/=)
- Módulo y asigna (%=)
'''

# ------------------------- [IGUAL] -------------------------
# Asignamos un valor a una variable
x = 100
print("Valor inicial de x:", x)  # 100

# ------------------------- [INCREMENTO] -------------------------
# Incrementamos el valor de x en 15
x += 15  # x = 100 + 15 = 115
print("Incremento de x:", x)  # 115

# ------------------------- [DECREMENTO] -------------------------
# Decrementamos el valor de x en 20
x -= 20  # x = 115 - 20 = 95
print("Decremento de x:", x)  # 95

# ------------------------- [MULTIPLICA Y ASIGNA] -------------------------
# Multiplicamos el valor de x por 3
x *= 3  # x = 95 * 3 = 285
print("Multiplicación de x:", x)  # 285

# ------------------------- [DIVIDE Y ASIGNA] -------------------------
# Dividimos el valor de x entre 5
x /= 5  # x = 285 / 5 = 57.0
print("División de x:", x)  # 57.0

# ------------------------- [MÓDULO Y ASIGNA] -------------------------
# Calculamos el módulo de x con 7
x %= 7  # x = 57.0 % 7 = 1.0
print("Módulo de x:", x)  # 1.0

# ------------------------- [NOTA SOBRE INCREMENTO Y DECREMENTO] -------------------------
'''
En Python, los operadores de incremento y decremento en 1 (como `a++` o `a--`) NO EXISTEN en su forma simplificada como en otros lenguajes. La única forma válida es:

a += 1  # Incremento en 1
a -= 1  # Decremento en 1
'''