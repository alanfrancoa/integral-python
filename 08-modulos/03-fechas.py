# ------------------ TALLER INTEGRADOR DE PYTHON (UNLZ) ------------------
# CLASE: 
# PROFESOR: GABRIEL NIGLIO
# CUATRIMESTRE: 1ER CUATRIMESTRE
# AÑO: 2025
# 

# ------------------------- [MÓDULO DE FECHAS] -------------------------

'''
Python incluye un módulo estándar llamado `datetime` que nos permite trabajar con fechas y horas de manera eficiente. Este módulo es muy útil para manipular, formatear y realizar operaciones con fechas y horas.
'''

# ------------------------- [IMPORTAR EL MÓDULO DATETIME] -------------------------
# Ejemplo 1: Importar el módulo `datetime`

import datetime

# ------------------------- [MOSTRAR LA FECHA ACTUAL] -------------------------
# Ejemplo 2: Obtener la fecha actual

# Mostrar la fecha actual (solo fecha, sin hora)
fecha_actual = datetime.date.today()
print("Fecha actual:", fecha_actual)  # Salida: YYYY-MM-DD

# Mostrar la fecha y hora actuales
fecha_completa = datetime.datetime.now()
print("Fecha y hora actuales:", fecha_completa)  # Salida: YYYY-MM-DD HH:MM:SS.microsegundos

# ------------------------- [ACCEDER A PROPIEDADES DE LA FECHA] -------------------------
# Ejemplo 3: Acceder a propiedades específicas de la fecha

'''
Como `fecha_completa` es un objeto de tipo `datetime`, podemos acceder a sus propiedades, como el año, mes y día.
'''

print("Año:", fecha_completa.year)  # Salida: Año actual (ej: 2025)
print("Mes:", fecha_completa.month)  # Salida: Mes actual (1-12)
print("Día:", fecha_completa.day)  # Salida: Día actual (1-31)

# ------------------------- [FORMATEAR LA FECHA] -------------------------
# Ejemplo 4: Formatear la fecha según nuestras necesidades

'''
Podemos formatear la fecha utilizando el método `strftime()`, que permite definir un formato personalizado.
'''

fecha_personalizada = fecha_completa.strftime("%d/%m/%y")
print("Fecha personalizada:", fecha_personalizada)  # Salida: DD/MM/YY (ej: 25/10/25)

# ------------------------- [ACCEDER A LA HORA ACTUAL] -------------------------
# Ejemplo 5: Obtener la hora actual

'''
Podemos acceder a la hora actual utilizando el método `time()`.
'''

hora_actual = datetime.datetime.now().time()
print("Hora actual:", hora_actual)  # Salida: HH:MM:SS.microsegundos