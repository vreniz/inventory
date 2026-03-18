# Esto usualmente va anidado dentro de un ciclo que controla si una vez cumplida la validación
# y realizada cualquier operación, el usuario quiere continuar introduciencdo datos, validandolos,
# y calculandolos hasta que diga que no y termine el programa ver iteracioncontinuidad.py
# usualmente validar nombres y/o strings es lo primero 
#
# esto en proyectos reales se puede volver una funcion def pal future 

while True: # VALIDACION ENTERO, REPITE hasta que el usuario escriba bien el número 
      entrada_cantidad = input("Enter Product Quantity: ") # el usuario ingresa el numero 
      try: #1
            cantidad= int(entrada_cantidad) #1 intento convertir a número entero
            if cantidad > 0: # 👉 🧠 “si es mayor que 0 → todo bien” 👉 sale del ciclo con el break ✅
             break # creo que PARA QUITAR EL BREAK le puedo asignar false AQUI, si creo una variable adicional en true al comienzo y el while lo cambio a  Nombredevariable == True
            elif cantidad == 0: #🧠 “0 no está permitido”
                 print("Error ❌, quantity cannot be zero") # mensaje de error y continua el ciclo
            else: # "si no es > 0 ni es 0 → es negativo”
                print("Error ❌, the quantity must be a positive integer") #mensaje de error y continua el ciclo     
      except ValueError: # 👉 🧠 “no es un número entero válido como caracteres o otras cosas y continua el ciclo”
          print("Error ❌, Please enter a valid integer number for Quantity ")
"""     
while True: # VALIDACION ENTERO sin tanto if elif else
      entrada_cantidad = input("Enter Product Quantity: ")
      try:
            cantidad= int(entrada_cantidad)
            if cantidad <= 0:
              print("Error ❌, the quantity must be a positive integer or different from 0")  
              continue
            break             
      except ValueError:
          print("Error ❌, Please enter a valid integer number for Quantity ")        
"""     