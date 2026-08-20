###
# 01- Sentencias condicionales (if, elif, else)
# Permiten ejecutar bloques de código solo si se cumplen ciertas condiciones.
###

import os
os.system("clear")

print("\n Setencia simple condicional")

edad = 18
if edad >= 18:
    print("Eres mayor de edad")
    print("¡Felicidades!")

edad = 15
if edad >= 18:
    print("Eres mayor de edad")
    print("¡Felicidades!")

print("\n Sentencia condicional con else")
edad = 15
if edad >= 18:
    print("Eres mayor de edad")
else:
    print("Eres menor de edad")

print("\n Setencia condicional con elif")
nota = 7
if nota >= 9:
    print("¡Sobresaliente!")
elif nota >= 7:
    print("¡Notable!")
elif nota >= 5:
    print("¡Aprobado!")
else:
    print("¡No está calificado!")

print("\n Condiciones múltiples")
edad = 69
tiene_carnet = True

# JavaScript
# && -> and
# || -> or

# (Ve) Un pueblo de Isla Margarita
if edad >= 18 and tiene_carnet:
    print("Puedes conducir")
else:
    print("POLICIA!!!!!!!")

# (Ve) Un pueblo de Isla Margarita
if edad >= 18 or tiene_carnet:
    print("Puedes conducir en la Isla Margarita")
else:
    print("Paga al policía y te deja conducir!!!")

es_fin_de_semana = False
if not es_fin_de_semana:
    print("¡Creky, venga que hay que trabajar!")

print("\n Anidar condicionales")
edad = 20
tiene_dinero = True
if edad >= 18:
    if tiene_dinero:
        print("Puedes ir a la discoteca")
    else:
        print("Quédate en casa")
else:
    print("No puedes entrar a la disco")

# Más fácil
# if edad < 18:
#     print("No puedes entrar a la disco")
# elif tiene_dinero:
#     print("Puedes ir a la discoteca")
# else:
#     print("Quédate en casa")
