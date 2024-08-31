def calculoFactorial (num:int)->str|int :
    resultado : int
    if num < 0 :
        return "No se puede valores negativos" 
    elif num == 0:
          return 1
    for n in range(1,num+1):
        resultado = resultado * n
    return resultado



    
    