#Hacer un ejercicio en donde el usurio ingrese una variable numérica y por medio de una secuencia lógica me permita validar si un resultado es correcto

#Solicitar el número al usuario 
num = input ("por favor, ingrese un número: ")

num = float (num)

#Verificar si el número es par o impar 
if num % 2 == 0:
    print ("el número es par. ")
else: 
    print ("el número es impar. ")