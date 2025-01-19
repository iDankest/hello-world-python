##
# 04 - Variables
# Las variables sirven para almacenar información y poder reutilizarla en nuestro código.
# Python es un lenguaje de tipado dinámico, por lo que no es necesario declarar el tipo de dato de la variable.
###

# asignar una variable
# solo hace falta poner esto
my_name = "Kilian"

age = 25

age = 26
print(age)

# Tipado dinamico: el tipo de dato se determina en tiempo de ejecución
# Que no tienes que declararlo explicitamente

name = "Dankest"
print(name)

name = 5
print(name)
#f-string (literal de cadena de formato )
print(f"Mi nombre es {my_name} y tengo {age - 1} años")
# covenciones de nombres
# snake_case
mi_variable = 5
MI_CONSTANTE = 5

#palabras reservadas
# False, None, True, and, as, assert, break, class, continue, def, del, elif, else, except, finally, for, from, global, if, import, in, is, lambda, nonlocal, not, or, pass, raise, return, try

is_user_logged_in: bool = False #Esto no sirve para nada, solo es para que sepas que es un booleano