###
# 05 - Entrada de usuario (input()) - Versión simplificada
# La función input() permite obtener datos del usuario a través de la consola.
###

nombre = input("Hola, ¿cómo te llamas?\n>")
print(f"Hola {nombre}, encantado de conocerte!")

age = input("¿Cuántos años tienes?\n>")
age = int(age)  # Convertimos la edad a un número entero (no recomendable)
print(f"Tienes {age} años")

print("Obtener múltiples valores a la vez")
country, city = input("¿En qué país y ciudad vives?\n>").split(", ")
# El "split" dicta como se separan los valores, en este caso por una coma
print(f"Vives en {country}, {city}")
