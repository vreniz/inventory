# Esto usualmente va anidado dentro de un ciclo que controla si una vez cumplida la validación
# y realizada cualquier operación, el usuario quiere continuar introduciencdo datos, validandolos,
# y calculandolos hasta que diga que no y termine el programa ver iteracioncontinuidad.py
# usualmente validar nombres y/o strings es lo primero 
#
# esto en proyectos reales se puede volver una funcion def pal future 

while True: # validacion del precio en .flotante; “repite hasta que el usuario lo haga bien"
     entrada_precio = input("Enter product price: ") # pide los datos para que el usuario lo escriba
     entrada_clean = entrada_precio.replace(",", ".") #arregla el formato antes de validar permitiendo que el usuario utilice coma (,) o (.) convirtiendo las comas en puntos
     if entrada_clean.count(".") > 1: # condicion para contar cuántos puntos hay
        print("Error ❌, invalid format (too many decimals)") # imprime mensaje de error si tiene muchos decimales (más de un punto)
        continue # si está mal → vuelve a empezar el ciclo
     try: #1
         precio = float(entrada_clean) #1 Python intenta convertir a número decimal
         if precio > 0: # valida que el numero ingresado sea un entero positivo 👉 Verifica:🧠 “¿es positivo?” Sí → sale del ciclo ✅ No → error ❌
            break # sale del ciclo
         else:
             print("Error ❌, price must be a positive number") # error si no es positivo y lo pide nuevamente,🧠 El programa repite hasta que el usuario escriba: un número decimal válido y mayor que 0
     except:
         print("Error ❌, Please enter a valid number for price (e.g. 1.0 or 1,0) ") # si no puede convertir eso no es un número y vuelve a pedir 🔁
         