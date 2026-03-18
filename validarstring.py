# Esto usualmente va anidado dentro de un ciclo que controla si una vez cumplida la validación
# y realizada cualquier operación, el usuario quiere continuar introduciencdo datos, validandolos,
# y calculandolos hasta que diga que no y termine el programa ver iteracioncontinuidad.py
# usualmente validar nombres y/o strings es lo primero 
#
nombreval = False  #👉 Crea una variable que significa: 🧠 “el nombre aún NO es válido”

# Necesita ser un ciclo para no permitirle al usuario continuar hasta que el usario de 
# el nombre en el formato correcto
while not nombreval:# PUEDE SER TAMBIÉN UN WHILE NOMBREVAL==FALSE:(si se) y signif mientras el nombre NO sea válido, repite
        nombre = input("Enter Product Name: ") # pide el input del nombre
        if nombre.strip() == "": # quita espacios y valida que no este vacio 
            print("Error name can not be empty") # mensaje de error
        elif nombre.replace(" ", "").isalpha(): # verifica que quite todos los espacios replace(" ", "")👉 quita TODOS los espacios; .isalpha() se asegura de preguntar si todos son letras
            nombreval = True #el nombre es válido y el while se detiene
        else: # si no cumple muestra el error y vuelve a pedir el nombre porque sigue en falso
            print("Error: name must contain only letters and spaces")