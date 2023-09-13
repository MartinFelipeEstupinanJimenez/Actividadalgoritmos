"vamos a realizar un codigo que realice por pantalla un calculo de variables, que nos permita sumar restar y hacer operaciones para mostrar al final un resultado de cada operacion"
"y a su vez crear una tabla de verdad y cada una de las operaciones usando bool o usando and y or"

print ("Este programa no se debe hacer por chat gpt el que lo haga le bajo la nota")

a = input("inserte un numero ")
b = input("inserte un numero mayor que el anterior ")


a = str(a)
b = str(b)

#print (a+b)
#print (a-b)
#print (a*b)
#print (a/b)
#print (a%b)

print("Tabla de la verdad todo lo relacionado con and o Y")
#print(str(a == a) + " and " + str(a == a) + " ---> " + str(a == a))
#print(str(a == a) + " and " + str(a == b) + " ---> " + str(a == b))
#print(str(a == b) + " and " + str(a == a) + " ---> " + str(a == b))
#print(str(a == b) + " and " + str(a == b) + " ---> " + str(a == b))

#print("Tabla de la verdad todo lo relacionado con or o O")
#print(str(a == a) + " and " + str(a == a) + " ---> " + str(a == a))
#print(str(a == a) + " and " + str(a == b) + " ---> " + str(a == a))
#print(str(a == b) + " and " + str(a == a) + " ---> " + str(a == a))
#print(str(a == b) + " and " + str(a == b) + " ---> " + str(a == b))

print(bool(a and a)) 
print(bool(a and b)) 
print(bool(b and a)) 
print(bool(a and b)) 

print("Tabla de la verdad todo lo relacionado con or o O")

print(bool(a or a)) 
print(bool(b or b)) 
print(bool(a or a)) 
print(bool(a or b)) 

#vamos a realizar secuencias con condiciones basadas en ciclos, realizar una lista de algunos articulos donde determinar cuales son los elementos de esa lista