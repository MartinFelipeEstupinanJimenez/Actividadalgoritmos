#Este programa va a tener como finalidad mostrar varios elementos que pueda solicitar el usuario o 

print("--------------------------------Inicio del programa--------------------------------")

edad1 = int (input("Cual es su edad "))

if edad1 >= 18:
    print("Eres mayor de edad ") 
    print("--------------------------------Modulo de seguridad--------------------------------")

    #Si el usuario es mayor de edad le vamos a solicitar una contraseña

    print("Su contraseña fue enviada exitosamente enviada al correo")

    clavemayordeedad = "Contraseña"
    password = input("Ingrese la contraseña que fue enviada a su correo ")

    if clavemayordeedad == password:
        print("Contraseña correcta")
        print("--------------------------------Modulo de interacción--------------------------------")
        print("Tiene que cambiar la contraseña actual")
        frase = str(input("Ingrese una contraseña nueva "))

        prueba = str(input("Ingrese de nuevo la contraseña "))

        clavemayordeedad = frase

        if clavemayordeedad == prueba:
            print("Su clave se ha cambiado exitasamente")
            print("Usted ha completado los tres modulos de autenticación")
        else:
        
            print("Las contraseñas no son iguales")
    else:
        print("Contraseña incorrecta")
else:
    print("Eres menor de edad")
    
