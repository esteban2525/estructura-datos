#CREAR UNA FUNCIÓN QUE REALICE OPERACIONES BASICAS (SUMA,RESTA...) ENTRE DOS NUMEROS

def factorial(n):
    resultado = 1
    for i in range(1, n + 1):
        resultado *= i
    return resultado

def operacion_basica(num1, num2, operacion):
    if operacion == 'suma':
        return num1 + num2
    elif operacion == 'resta':
        return num1 - num2
    elif operacion == 'multiplicacion':
        return num1 * num2
    elif operacion == 'division':
        if num2 != 0:
            return num1 / num2
        else:
            raise ZeroDivisionError("No se puede dividir por cero")
    else:
        raise ValueError("Operación no válida")

#uso
print(factorial(5))
print(operacion_basica(10, 3, 'suma'))  
print(operacion_basica(5, 3, 'resta'))  
print(operacion_basica(5, 3, 'multiplicacion'))  
print(operacion_basica(30, 2, 'division'))  
    

