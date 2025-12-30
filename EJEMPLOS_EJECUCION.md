# Ejemplos de Ejecución del Menú de Programas

## Menú Principal

```
==================================================
     MENÚ PRINCIPAL - FUNDAMENTOS DE PROGRAMACIÓN
==================================================
1. Par o Impar
2. Promedio de 3 Números
3. Área de un Triángulo
4. Descuento por Compra
5. Validación Aprobado/Reprobado
0. Salir
==================================================

Seleccione una opción:
```

---

## Opción 1: Par o Impar

**Ejemplo 1 - Número Par:**
```
Seleccione una opción: 1

==================================================
PROGRAMA 1: PAR O IMPAR
==================================================
Ingrese un número entero: 24

✓ El número 24 es PAR

Presione ENTER para volver al menú...
```

**Ejemplo 2 - Número Impar:**
```
Seleccione una opción: 1

==================================================
PROGRAMA 1: PAR O IMPAR
==================================================
Ingrese un número entero: 17

✓ El número 17 es IMPAR

Presione ENTER para volver al menú...
```

---

## Opción 2: Promedio de 3 Números

**Ejemplo:**
```
Seleccione una opción: 2

==================================================
PROGRAMA 2: PROMEDIO DE 3 NÚMEROS
==================================================
Ingrese el primer número: 8.5
Ingrese el segundo número: 9.0
Ingrese el tercer número: 7.5

✓ Los números ingresados son: 8.5, 9.0, 7.5
✓ El promedio es: 8.33

Presione ENTER para volver al menú...
```

---

## Opción 3: Área de un Triángulo

**Ejemplo:**
```
Seleccione una opción: 3

==================================================
PROGRAMA 3: ÁREA DE UN TRIÁNGULO
==================================================
Ingrese la base del triángulo: 10
Ingrese la altura del triángulo: 5

✓ Base: 10.0
✓ Altura: 5.0
✓ Área del triángulo: 25.00

Presione ENTER para volver al menú...
```

---

## Opción 4: Descuento por Compra

**Ejemplo 1 - Compra con 10% descuento:**
```
Seleccione una opción: 4

==================================================
PROGRAMA 4: DESCUENTO POR COMPRA
==================================================

Escala de descuentos:
• Compra menor a $100: Sin descuento
• Compra de $100 a $500: 10% de descuento
• Compra de $501 a $1000: 15% de descuento
• Compra mayor a $1000: 20% de descuento
--------------------------------------------------

Ingrese el monto de la compra: $250

✓ Monto original: $250.00
✓ Descuento aplicado: 10%
✓ Ahorro: $25.00
✓ Total a pagar: $225.00

Presione ENTER para volver al menú...
```

**Ejemplo 2 - Compra con 20% descuento:**
```
Seleccione una opción: 4

==================================================
PROGRAMA 4: DESCUENTO POR COMPRA
==================================================

Escala de descuentos:
• Compra menor a $100: Sin descuento
• Compra de $100 a $500: 10% de descuento
• Compra de $501 a $1000: 15% de descuento
• Compra mayor a $1000: 20% de descuento
--------------------------------------------------

Ingrese el monto de la compra: $1500

✓ Monto original: $1500.00
✓ Descuento aplicado: 20%
✓ Ahorro: $300.00
✓ Total a pagar: $1200.00

Presione ENTER para volver al menú...
```

---

## Opción 5: Validación Aprobado/Reprobado

**Ejemplo 1 - Estudiante Aprobado:**
```
Seleccione una opción: 5

==================================================
PROGRAMA 5: VALIDACIÓN APROBADO/REPROBADO
==================================================

Nota mínima para aprobar: 3.0
Escala de calificación: 0.0 a 5.0
--------------------------------------------------

Ingrese el nombre del estudiante: Juan Pérez
Ingrese la nota final (0.0 - 5.0): 4.5

✓ Estudiante: Juan Pérez
✓ Nota final: 4.50
✓ Estado: APROBADO
✓ ¡Excelente desempeño!

Presione ENTER para volver al menú...
```

**Ejemplo 2 - Estudiante Reprobado:**
```
Seleccione una opción: 5

==================================================
PROGRAMA 5: VALIDACIÓN APROBADO/REPROBADO
==================================================

Nota mínima para aprobar: 3.0
Escala de calificación: 0.0 a 5.0
--------------------------------------------------

Ingrese el nombre del estudiante: María García
Ingrese la nota final (0.0 - 5.0): 2.5

✓ Estudiante: María García
✓ Nota final: 2.50
✗ Estado: REPROBADO
✗ Debe cursar nuevamente la asignatura

Presione ENTER para volver al menú...
```

---

## Validación de Opción Inválida

**Ejemplo 1 - Opción fuera de rango:**
```
Seleccione una opción: 9

✗ Opción no válida. Intente de nuevo.
   Por favor, seleccione una opción entre 0 y 5

Presione ENTER para volver al menú...
```

**Ejemplo 2 - Entrada no numérica:**
```
Seleccione una opción: abc

✗ Error: Debe ingresar un número válido
   Por favor, seleccione una opción entre 0 y 5

Presione ENTER para volver al menú...
```

---

## Opción 0: Salir

```
Seleccione una opción: 0

==================================================
     ¡GRACIAS POR USAR EL PROGRAMA!
     Saliendo del sistema...
==================================================
```

---

## Notas Técnicas

### Características Implementadas:

1. **Ciclo While**: Mantiene el menú activo hasta que el usuario seleccione salir
2. **Estructura Switch**: Implementada con if/elif/else en Python
3. **Modularidad**: Cada programa está en una función independiente
4. **Validación de Entradas**: Manejo de errores con try/except
5. **Retorno al Menú**: Función pausar() permite volver al menú después de cada operación
6. **Salida Controlada**: Opción 0 termina el programa de forma ordenada

### Validaciones Implementadas:

- Números enteros válidos (Par/Impar)
- Números flotantes válidos (Promedio, Área, Descuento, Nota)
- Valores positivos para base y altura del triángulo
- Montos no negativos para compras
- Notas en rango 0.0 - 5.0
- Opciones de menú válidas (0-5)
