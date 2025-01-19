# Vamos a ver ejemplos de recursividad en Python
# Recursividad es cuando una función se llama a sí misma
#Vamos a empezar con un ejemplo simple de factorial

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

print(factorial(5))

# vamos a hacer otro ejemplo de recursividad numero desendente
def numero_desendente(n):
    if n == 0:
        return 0
    else:
        return n + numero_desendente(n-1)

print(numero_desendente(5))

