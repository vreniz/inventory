print("Welcome to the Inventary data entry") #mensaje de bienvenida
               # este es el ciclo que me permite preguntar si la persona quiere seguir realizando la operación de entrada de datos y calculo
iteracion=True # es necesario definirla porque sino Python no sabe qué es iteracion y da error
while iteracion: # es lo mismo que escribir esto: while iteracion == True:
    
    #aquí van las validaciones como leer numeros int, float (pidiendoselos al ) y recibir solo string
    
    
    
    
#costo_total=(precio * cantidad) - la operación a realizar 
 print("Product Name: ",nombre,"Price: ",precio, "Quantity: ",cantidad, "Total: ", costo_total)  #lo que se imprime cuando pasa las validaciónes y permite realizar la operación
 # CONTINUAR si la persona desea seguir y validar su respuesta si o no para cualquier caso, cualquier validacion y cualquier operacion
 continuar = input("Do you wish to enter a new product? yes/no: ").strip().lower()
 while continuar !="yes" and continuar !="no":
     print("Option NOT valid ❌")
     continuar = input("Do you wish to enter a new product? yes/no: ").strip().lower()
 if continuar == "yes":
  iteracion = True
 else:
  iteracion = False
  print("Thanks for entering new data!!!")