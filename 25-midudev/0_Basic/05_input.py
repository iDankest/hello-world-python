###
#05 - Entrada de usuario (input())
#La función input() nos permite pedir datos al usuario.
###
nombre = input("¿Cómo te llamas? ")
print(f"Hola {nombre}!") # f-string

age = input("¿Cuántos años tienes? \n")
print(f"Dentro de 20 años tendras {int(age) + 20} años")

print("obtener multiples valores a la vez")
country, city = input("¿De dónde eres? ").split(", ")
print(country, city)