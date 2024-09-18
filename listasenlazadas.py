class Animal:
    def __init__(self, nombre, edad, tipo):
        self.nombre = nombre
        self.edad = edad
        self.tipo = tipo

    def __str__(self):
        return f"{self.nombre} ({self.tipo}) - {self.edad} años"


class Nodo:
    def __init__(self, animal):
        self.animal = animal
        self.siguiente = None


class ListaEnlazada:
    def __init__(self):
        self.cabeza = None

    def agregar_animal(self, animal):
        if self.cabeza is None:
            self.cabeza = Nodo(animal)
        else:
            actual = self.cabeza
            while actual.siguiente:
                actual = actual.siguiente
            actual.siguiente = Nodo(animal)

    def mostrar_animales(self):
        actual = self.cabeza
        if actual is None:
            print("La lista está vacía.")
            return
        while actual:
            print(actual.animal)
            actual = actual.siguiente


# Ejemplo de uso
zoo = ListaEnlazada()
zoo.agregar_animal(Animal("Aguilucha", 5, "Águila"))
zoo.agregar_animal(Animal("Panterita", 3, "Pantera"))
zoo.agregar_animal(Animal("Vacita", 2, "Vaca"))

print("\nAnimales en la lista:")
zoo.mostrar_animales()
