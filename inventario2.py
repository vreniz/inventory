print("Welcome to the Inventary data entry")

iteracion= True
while iteracion:
 nombreval = False
 while not nombreval:# PUEDE SER TAMBIÉN UN WHILE NOMBREVAL==FALSE:
        nombre = input("Enter Product Name: ")
        if nombre.strip() == "":
            print("Error name can not be empty")
        elif nombre.replace(" ", "").isalpha():
            nombreval = True
        else:
            print("Error: name must contain only letters and spaces")
 while True: # validacion del precio en .flotante 
     entrada_precio = input("Enter product price: ")
     try:
         precio = float(entrada_precio)
         break
     except:
         print("Error ❌, Please enter a valid number for price ")
 while True: # VALIDACION ENTERO 
      entrada_cantidad = input("Enter Product Quantity: ")
      try:
         cantidad= int(entrada_cantidad)
         break # creo que PARA QUITAR EL BREAK le puedo asignar false AQUI, si creo una variable adicional en true al comienzo y el while lo cambio a  Nombredevariable == True
      except:
          print("Error ❌, Please enter a valid number for Quantity ")
    #Resultado      
      
 costo_total=(precio * cantidad) 
 print("Product Name: ",nombre,"Price: ",precio, "Quantity: ",cantidad, "Total: ", costo_total)
 # CONTINUAR
 continuar = input("Do you wish to enter a new product? yes/no: ").strip().lower()
 if continuar == "yes":
  iteracion = True
 else:
  iteracion = False
 print("Thanks for entering new data!!!")



      
#print("Product Name: ",nombre,"Price: ",precio, "Quantity: ",cantidad, "Total: ", costo_total)

"""
precioval = False
while not precioval:
    entradaprecio=input("Enter Product Price: ")
    try:
        precio = float(entradaprecio)
        precioval= True
    except ValueError:
        print("Error: Please enter a valid number for price.")    
        """