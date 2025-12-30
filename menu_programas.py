"""
Menú Principal - Programas de Fundamentos de Programación
Docente: Jorge Andrés Araujo Bernal
Estudiante: [Nombre del estudiante]
"""

def par_impar():
    """Determina si un número es par o impar"""
    print("\n" + "="*50)
    print("PROGRAMA 1: PAR O IMPAR")
    print("="*50)

    try:
        numero = int(input("Ingrese un número entero: "))

        if numero % 2 == 0:
            print(f"\n✓ El número {numero} es PAR")
        else:
            print(f"\n✓ El número {numero} es IMPAR")
    except ValueError:
        print("\n✗ Error: Debe ingresar un número entero válido")


def promedio_tres_numeros():
    """Calcula el promedio de 3 números"""
    print("\n" + "="*50)
    print("PROGRAMA 2: PROMEDIO DE 3 NÚMEROS")
    print("="*50)

    try:
        num1 = float(input("Ingrese el primer número: "))
        num2 = float(input("Ingrese el segundo número: "))
        num3 = float(input("Ingrese el tercer número: "))

        promedio = (num1 + num2 + num3) / 3

        print(f"\n✓ Los números ingresados son: {num1}, {num2}, {num3}")
        print(f"✓ El promedio es: {promedio:.2f}")
    except ValueError:
        print("\n✗ Error: Debe ingresar números válidos")


def area_triangulo():
    """Calcula el área de un triángulo"""
    print("\n" + "="*50)
    print("PROGRAMA 3: ÁREA DE UN TRIÁNGULO")
    print("="*50)

    try:
        base = float(input("Ingrese la base del triángulo: "))
        altura = float(input("Ingrese la altura del triángulo: "))

        if base <= 0 or altura <= 0:
            print("\n✗ Error: La base y altura deben ser valores positivos")
        else:
            area = (base * altura) / 2
            print(f"\n✓ Base: {base}")
            print(f"✓ Altura: {altura}")
            print(f"✓ Área del triángulo: {area:.2f}")
    except ValueError:
        print("\n✗ Error: Debe ingresar números válidos")


def descuento_compra():
    """Calcula el descuento según el monto de compra"""
    print("\n" + "="*50)
    print("PROGRAMA 4: DESCUENTO POR COMPRA")
    print("="*50)
    print("\nEscala de descuentos:")
    print("• Compra menor a $100: Sin descuento")
    print("• Compra de $100 a $500: 10% de descuento")
    print("• Compra de $501 a $1000: 15% de descuento")
    print("• Compra mayor a $1000: 20% de descuento")
    print("-"*50)

    try:
        monto = float(input("\nIngrese el monto de la compra: $"))

        if monto < 0:
            print("\n✗ Error: El monto no puede ser negativo")
        else:
            descuento = 0

            if monto < 100:
                descuento = 0
            elif monto <= 500:
                descuento = 10
            elif monto <= 1000:
                descuento = 15
            else:
                descuento = 20

            monto_descuento = monto * (descuento / 100)
            total = monto - monto_descuento

            print(f"\n✓ Monto original: ${monto:.2f}")
            print(f"✓ Descuento aplicado: {descuento}%")
            print(f"✓ Ahorro: ${monto_descuento:.2f}")
            print(f"✓ Total a pagar: ${total:.2f}")
    except ValueError:
        print("\n✗ Error: Debe ingresar un número válido")


def validacion_aprobado():
    """Valida si un estudiante aprobó o reprobó según su nota"""
    print("\n" + "="*50)
    print("PROGRAMA 5: VALIDACIÓN APROBADO/REPROBADO")
    print("="*50)
    print("\nNota mínima para aprobar: 3.0")
    print("Escala de calificación: 0.0 a 5.0")
    print("-"*50)

    try:
        nombre = input("\nIngrese el nombre del estudiante: ")
        nota = float(input("Ingrese la nota final (0.0 - 5.0): "))

        if nota < 0 or nota > 5:
            print("\n✗ Error: La nota debe estar entre 0.0 y 5.0")
        else:
            print(f"\n✓ Estudiante: {nombre}")
            print(f"✓ Nota final: {nota:.2f}")

            if nota >= 3.0:
                print(f"✓ Estado: APROBADO")
                if nota >= 4.5:
                    print("✓ ¡Excelente desempeño!")
                elif nota >= 4.0:
                    print("✓ ¡Muy buen desempeño!")
                else:
                    print("✓ Buen desempeño")
            else:
                print(f"✗ Estado: REPROBADO")
                print("✗ Debe cursar nuevamente la asignatura")
    except ValueError:
        print("\n✗ Error: Debe ingresar una nota válida")


def mostrar_menu():
    """Muestra el menú principal"""
    print("\n" + "="*50)
    print("     MENÚ PRINCIPAL - FUNDAMENTOS DE PROGRAMACIÓN")
    print("="*50)
    print("1. Par o Impar")
    print("2. Promedio de 3 Números")
    print("3. Área de un Triángulo")
    print("4. Descuento por Compra")
    print("5. Validación Aprobado/Reprobado")
    print("0. Salir")
    print("="*50)


def pausar():
    """Pausa la ejecución hasta que el usuario presione ENTER"""
    input("\nPresione ENTER para volver al menú...")


def main():
    """Función principal que controla el menú"""
    print("\n" + "╔" + "="*48 + "╗")
    print("║  BIENVENIDO AL SISTEMA DE PROGRAMAS - FDP     ║")
    print("╚" + "="*48 + "╝")

    while True:
        mostrar_menu()

        try:
            opcion = int(input("\nSeleccione una opción: "))

            # Estructura tipo switch usando if/elif/else
            if opcion == 1:
                par_impar()
                pausar()
            elif opcion == 2:
                promedio_tres_numeros()
                pausar()
            elif opcion == 3:
                area_triangulo()
                pausar()
            elif opcion == 4:
                descuento_compra()
                pausar()
            elif opcion == 5:
                validacion_aprobado()
                pausar()
            elif opcion == 0:
                print("\n" + "="*50)
                print("     ¡GRACIAS POR USAR EL PROGRAMA!")
                print("     Saliendo del sistema...")
                print("="*50 + "\n")
                break
            else:
                print("\n✗ Opción no válida. Intente de nuevo.")
                print("   Por favor, seleccione una opción entre 0 y 5")
                pausar()
        except ValueError:
            print("\n✗ Error: Debe ingresar un número válido")
            print("   Por favor, seleccione una opción entre 0 y 5")
            pausar()


if __name__ == "__main__":
    main()
