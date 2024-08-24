#CREAR UN SISTEMA DE CONTROL DE INGRESO PARA EVITAR EL SOBRE CUPO#
#DEFINIMOS CAPACIDAD

ingreso = 0 
cupo = int(input("ingresar cupo"))
while ingreso < cupo:
    valido=input("voleto válido")
if valido == '1':
    print("ingresar personas")
    ingreso = ingreso+1
else: 
    print("persona no ingresada")
    print("cupo lleno")   
     
    
 