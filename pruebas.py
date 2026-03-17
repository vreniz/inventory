boleana= True
while boleana: # VALIDACION ENTEROS LO DE BOLEANA ES UNA VAFRIABLE X PARA QUITAR LO DEL BREAK
      entrada_cantidad = input("Enter Product Quantity: ")
      try:
         cantidad= int(entrada_cantidad)
         boleana=False # creo que PARA QUITAR EL BREAK le puedo asignar false AQUI, si creo una variable adicional en true al comienzo y el while lo cambio a  Nombredevariable == True o Nombredevariable:
      except:
          print("Error ❌, Please enter a valid number for Quantity ")
print("cantidad",cantidad)         