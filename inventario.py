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
 while True: # 
     entrada_precio = input("Enter product price: ") # 
     entrada_clean = entrada_precio.replace(",", ".") 
     if entrada_clean.count(".") > 1: 
        print("Error ❌, invalid format (too many decimals)") 
        continue 
     try: #1
         precio = float(entrada_clean) 
         if precio > 0: 
            break 
         else:
             print("Error ❌, price must be a positive number") 
     except:
         print("Error ❌, Please enter a valid number for price (e.g. 1.0 or 1,0) ") # si no puede convertir eso no es un número y vuelve a pedir 🔁
         
 while True: # 
      entrada_cantidad = input("Enter Product Quantity: ") 
      try: #1
            cantidad= int(entrada_cantidad) 
            if cantidad > 0: 
             break 
            elif cantidad == 0: 
                 print("Error ❌, quantity cannot be zero")
            else: 
                print("Error ❌, the quantity must be a positive integer") 
      except ValueError: 
          print("Error ❌, Please enter a valid integer number for Quantity ")   
      
 costo_total=(precio * cantidad) 
 print("Product Name: ",nombre,"Price: ",precio, "Quantity: ",cantidad, "Total: ", costo_total)
 # CONTINUAR
 continuar = input("Do you wish to enter a new product? yes/no: ").strip().lower()
 while continuar !="yes" and continuar !="no":
     print("Option NOT valid ❌")
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