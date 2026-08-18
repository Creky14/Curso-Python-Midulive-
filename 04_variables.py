##
# 04 - Variables
# Las variables sirven para guardar datos en memoria.
# Python es un lenguaje de tipado dinámico y de tipado fuerte.
###

# Asignar una variable
# Solo hace falta poner esto
# my_name = "Creky14"
# # print(my_name)

# age = 32
# # print(age)

# # age = 39
# # print(age)

# # Tipado dinámico: el tipo de dato se determina en tiempo de ejecución
# # que no tienes que declararlo explicitamente
# name = "Creky14"
# print(type(name))

# name = 32
# print(type(name))

# # Tipado fuerte: Python no realiza conversiones de tipo automáticas
# # print(10 + "2")

# # f-string (literal de cadena de formato)
# # desde la version Python 3.6
# print(f"Hola soy {my_name}, tengo {age + 5} años")

# # No recomendada forma de asignar variables
# name, age, city = "Creky14", 32, "Madrid"

# Convenciones de nombres de variables

# mi_nombre_de_variable = "Creky14"  # snake_case
# nombre = "ok"
# MiNombreDeVariable = "ko"     # PascalCase
# minombredevariable = "ko"     # todojunto

# mi_nombre_de_variable_123 = "ok"

# MI_CONSTANTE = 3.14  # UPPER_CASE -> Constantes

# MI_CONSTANTE = 2
# print(MI_CONSTANTE)  # Python no tiene constantes, pero se pueden simular con una clase
# Se escriben en UPPER_CASE para indicar que no deben cambiarse

# 123123_variable = "ok"  # No se puede empezar con un número
# mi-variable = "ok"  # No se puede usar guiones
# mi variable = "ok"  # No se puede usar espacios

# True = False  # No se puede reasignar valores a palabras reservadas

# ['False', 'None', 'True', 'and', 'as', 'assert',
# 'async', 'await', 'break', 'class', 'continue',
# 'def', 'del', 'elif', 'else', 'except', 'finally',
# 'for', 'from', 'global', 'if', 'import', 'in', 'is',
# 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise',
# 'return', 'try', 'while', 'with', 'yield'] -> 01_hello_world.py

is_user_logged_in: bool = True
print(is_user_logged_in)

is_user_logged_in = 42
print(is_user_logged_in)
