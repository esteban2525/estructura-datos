

class Vehiculo:
    def __init__(self, marca:str, combustible:str):
        self.marca = marca
        self.combustible = combustible
    def encender(self ):
        pass
    def arrancar(self ):
        pass
    def __str__(self) -> str:
        return f"El vehiculo {self.marca} utiliza combustible {self.combustible}"
carro = Vehiculo("Toyota", "Corriente") 
print(carro)
print(type(carro))