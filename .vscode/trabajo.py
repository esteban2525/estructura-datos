import math

def calcular_inercia_cuarto_circulo():
    p = float(input("Digite el valor de P: "))
    r = float(input("Digite el valor de R: "))
    ix = iy = p * r**4 / 16
    return ix, iy

def calcular_inercia_enjuta_parabolica():
    a = float(input("Digite el valor de a: "))
    h = float(input("Digite el valor de h: "))
    ix = a * h**3 / 21
    iy = a**3 * h / 5
    return ix, iy

def calcular_inercia_sector_circular():
    r1 = float(input("Digite el valor de R1: "))
    ang = float(input("Digite el valor de Ang (en radianes): "))
    ix = r1**4 / 4 * (ang - math.sin(ang) * math.cos(ang))
    iy = r1**4 / 4 * (ang + math.sin(ang) * math.cos(ang))
    return ix, iy

def calcular_inercia_semicirculo():
    p2 = float(input("Digite el valor de P2: "))
    r2 = float(input("Digite el valor de R2: "))
    ix = p2 * r2**4 / 8
    iy = 5 * p2 * r2**4 / 8
    return ix, iy

def calcular_inercia_semielipse():
    p3 = float(input("Digite el valor de P3: "))
    a2 = float(input("Digite el valor de a2: "))
    b = float(input("Digite el valor de b: "))
    ix = p3 * a2 * b**3 / 8
    iy = 5 * p3 * a2**3 * b / 8
    return ix, iy

def calcular_inercia_semiparabola():
    a3 = float(input("Digite el valor de a3: "))
    b2 = float(input("Digite el valor de b2: "))
    ix = 2 * a3 * b2**3 / 15
    iy = 2 * a3**3 * b2 / 7
    return ix, iy

def main():
    opciones = {
        1: ("Calcular la inercia del cuarto de círculo", calcular_inercia_cuarto_circulo),
        2: ("Calcular la inercia de la enjuta parabólica", calcular_inercia_enjuta_parabolica),
        3: ("Calcular la inercia del sector circular", calcular_inercia_sector_circular),
        4: ("Calcular la inercia del semicírculo", calcular_inercia_semicirculo),
        5: ("Calcular la inercia de la semielipse", calcular_inercia_semielipse),
        6: ("Calcular la inercia de la semiparábola", calcular_inercia_semiparabola),
    }

    while True:
        print("\nMENÚ DE OPERACIONES")
        for key, (descripcion, _) in opciones.items():
            print(f"{key}. {descripcion}")
        print("7. Salir del programa")
        
        try:
            opc = int(input("\nSeleccione una opción: "))
            
            if opc == 7:
                print("Saliendo del programa...")
                break
            elif opc in opciones:
                ix, iy = opciones[opc][1]()
                print(f"\nMomento de inercia en Ix: {ix:.4f}")
                print(f"Momento de inercia en Iy: {iy:.4f}")
            else:
                print("Opción no válida. Intente de nuevo.")
        except ValueError:
            print("Por favor, ingrese un número válido.")
        except Exception as e:
            print(f"Ocurrió un error: {e}")

if __name__ == "__main__":
    main()