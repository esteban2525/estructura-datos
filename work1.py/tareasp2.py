from datetime import datetime

class Tarea:
    def __init__(self, descripcion, prioridad, fecha_vencimiento):
        self.descripcion = descripcion
        self.prioridad = prioridad
        self.fecha_vencimiento = fecha_vencimiento

    def __str__(self):
        return f"{self.descripcion} | Prioridad: {self.prioridad} | Vence: {self.fecha_vencimiento.strftime('%d/%m/%Y')}"

class Nodo:
    def __init__(self, tarea):
        self.tarea = tarea
        self.siguiente = None

class ListaEnlazadaTareas:
    def __init__(self):
        self.cabeza = None

    def agregar_tarea(self, tarea):
        nuevo_nodo = Nodo(tarea)
        if not self.cabeza:
            self.cabeza = nuevo_nodo
        else:
            actual = self.cabeza
            while actual.siguiente:
                actual = actual.siguiente
            actual.siguiente = nuevo_nodo

    def mostrar_tareas(self):
        actual = self.cabeza
        while actual:
            print(actual.tarea)
            actual = actual.siguiente

    def eliminar_tarea(self, descripcion):
        if not self.cabeza:
            print("Lista vacía.")
            return
        if self.cabeza.tarea.descripcion == descripcion:
            self.cabeza = self.cabeza.siguiente
            print(f"Tarea '{descripcion}' eliminada.")
            return
        actual = self.cabeza
        while actual.siguiente:
            if actual.siguiente.tarea.descripcion == descripcion:
                actual.siguiente = actual.siguiente.siguiente
                print(f"Tarea '{descripcion}' eliminada.")
                return
            actual = actual.siguiente
        print(f"Tarea '{descripcion}' no encontrada.")

# Ejemplo de uso
lista = ListaEnlazadaTareas()
lista.agregar_tarea(Tarea("Comprar materiales", 1, datetime(2024, 9, 25)))
lista.agregar_tarea(Tarea("Enviar informe", 2, datetime(2024, 9, 20)))
lista.agregar_tarea(Tarea("Revisar contrato", 3, datetime(2024, 10, 5)))

print("Tareas pendientes:")
lista.mostrar_tareas()

lista.eliminar_tarea("Enviar informe")

print("\nTareas pendientes después de eliminación:")
lista.mostrar_tareas()
