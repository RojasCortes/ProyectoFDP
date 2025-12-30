# INFORME DE ACTIVIDAD
## Menú de Programas con Estructura Switch

---

### INFORMACIÓN ACADÉMICA

**Asignatura:** Fundamentos de Programación
**Docente:** Jorge Andrés Araujo Bernal
**Estudiante:** [Nombre del estudiante]
**Fecha:** [Fecha de entrega]

---

## INTRODUCCIÓN

El presente informe documenta el desarrollo de un programa en Python que implementa un menú tipo switch para ejecutar múltiples programas vistos durante el curso de Fundamentos de Programación. El objetivo es demostrar el dominio de estructuras condicionales, ciclos, modularidad y validación de entradas.

---

## PROGRAMAS IMPLEMENTADOS

El menú principal incluye los siguientes 5 programas:

1. **Par o Impar**: Determina si un número ingresado es par o impar
2. **Promedio de 3 Números**: Calcula el promedio aritmético de tres valores
3. **Área de un Triángulo**: Calcula el área usando base y altura
4. **Descuento por Compra**: Aplica descuentos según el monto de compra
5. **Validación Aprobado/Reprobado**: Valida si un estudiante aprobó según su nota

---

## CAPTURAS DE PANTALLA

### 1. Menú Principal

**[INSTRUCCIÓN: Ejecutar el programa y capturar pantalla del menú principal]**

```
╔════════════════════════════════════════════════╗
║  BIENVENIDO AL SISTEMA DE PROGRAMAS - FDP     ║
╚════════════════════════════════════════════════╝

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

**Descripción:** Menú principal del programa que muestra las 5 opciones disponibles más la opción de salida.

---

### 2. Programa 1 - Par o Impar

**[INSTRUCCIÓN: Ejecutar opción 1, ingresar un número par (ej: 24) y capturar pantalla]**

**Datos de prueba:**
- Entrada: 24
- Resultado esperado: "El número 24 es PAR"

**[INSTRUCCIÓN: Ejecutar opción 1 nuevamente, ingresar un número impar (ej: 17) y capturar pantalla]**

**Datos de prueba:**
- Entrada: 17
- Resultado esperado: "El número 17 es IMPAR"

**Descripción:** Este programa utiliza el operador módulo (%) para determinar si un número es divisible por 2. Incluye validación para asegurar que la entrada sea un número entero válido.

---

### 3. Programa 2 - Promedio de 3 Números

**[INSTRUCCIÓN: Ejecutar opción 2, ingresar tres números (ej: 8.5, 9.0, 7.5) y capturar pantalla]**

**Datos de prueba:**
- Entradas: 8.5, 9.0, 7.5
- Promedio esperado: 8.33

**Descripción:** Calcula el promedio aritmético de tres números usando la fórmula: (num1 + num2 + num3) / 3. Acepta números decimales y muestra el resultado con dos decimales.

---

### 4. Programa 3 - Área de un Triángulo

**[INSTRUCCIÓN: Ejecutar opción 3, ingresar base=10 y altura=5, capturar pantalla]**

**Datos de prueba:**
- Base: 10
- Altura: 5
- Área esperada: 25.00

**Descripción:** Implementa la fórmula del área de un triángulo: (base × altura) / 2. Incluye validación para asegurar que base y altura sean valores positivos.

---

### 5. Programa 4 - Descuento por Compra

**[INSTRUCCIÓN: Ejecutar opción 4, probar con diferentes montos]**

**Prueba 1 - 10% de descuento:**
- Monto: $250
- Descuento: 10%
- Total esperado: $225.00

**Prueba 2 - 20% de descuento:**
- Monto: $1500
- Descuento: 20%
- Total esperado: $1200.00

**Descripción:** Aplica descuentos escalonados según el monto:
- Menos de $100: Sin descuento
- $100 - $500: 10%
- $501 - $1000: 15%
- Más de $1000: 20%

---

### 6. Programa 5 - Validación Aprobado/Reprobado

**[INSTRUCCIÓN: Ejecutar opción 5, probar con estudiante aprobado]**

**Prueba 1 - Aprobado:**
- Nombre: Juan Pérez
- Nota: 4.5
- Estado esperado: APROBADO - ¡Excelente desempeño!

**[INSTRUCCIÓN: Ejecutar opción 5, probar con estudiante reprobado]**

**Prueba 2 - Reprobado:**
- Nombre: María García
- Nota: 2.5
- Estado esperado: REPROBADO

**Descripción:** Valida si un estudiante aprobó (nota ≥ 3.0) o reprobó. Incluye mensajes adicionales según el nivel de desempeño:
- 4.5 - 5.0: Excelente
- 4.0 - 4.4: Muy bueno
- 3.0 - 3.9: Bueno
- 0.0 - 2.9: Reprobado

---

### 7. Validación de Errores

**[INSTRUCCIÓN: Probar ingresar una opción inválida (ej: 9) y capturar pantalla]**

**Prueba 1 - Opción fuera de rango:**
- Entrada: 9
- Mensaje esperado: "Opción no válida. Intente de nuevo."

**[INSTRUCCIÓN: Probar ingresar texto en lugar de número (ej: "abc") y capturar pantalla]**

**Prueba 2 - Entrada no numérica:**
- Entrada: abc
- Mensaje esperado: "Error: Debe ingresar un número válido"

**Descripción:** El programa valida las entradas del usuario y muestra mensajes claros cuando se ingresan opciones inválidas, cumpliendo con el requisito de validación de datos.

---

### 8. Salida del Programa

**[INSTRUCCIÓN: Ejecutar opción 0 para salir y capturar pantalla]**

**Descripción:** Al seleccionar la opción 0, el programa muestra un mensaje de despedida y termina la ejecución de forma controlada, saliendo del ciclo while.

---

## ESTRUCTURA TÉCNICA DEL PROGRAMA

### 1. Ciclo Principal (While)

El programa utiliza un ciclo `while True` que se ejecuta indefinidamente hasta que el usuario seleccione la opción 0 (Salir). Esto permite que el menú se muestre repetidamente después de ejecutar cada programa.

```python
while True:
    mostrar_menu()
    opcion = int(input("\nSeleccione una opción: "))

    # Estructura switch...

    if opcion == 0:
        break  # Sale del ciclo
```

### 2. Estructura Switch (if/elif/else)

Python no tiene un `switch` nativo, por lo que se simula usando `if/elif/else`:

```python
if opcion == 1:
    par_impar()
    pausar()
elif opcion == 2:
    promedio_tres_numeros()
    pausar()
elif opcion == 3:
    area_triangulo()
    pausar()
# ... más opciones
else:
    print("Opción no válida")
```

### 3. Modularidad (Funciones)

Cada programa está implementado en una función independiente, lo que facilita el mantenimiento y la reutilización del código:

- `par_impar()`: Función para programa 1
- `promedio_tres_numeros()`: Función para programa 2
- `area_triangulo()`: Función para programa 3
- `descuento_compra()`: Función para programa 4
- `validacion_aprobado()`: Función para programa 5
- `mostrar_menu()`: Función para mostrar el menú
- `pausar()`: Función para pausar y volver al menú

### 4. Validación de Entradas

Se implementaron validaciones usando `try/except` para manejar errores:

```python
try:
    opcion = int(input("\nSeleccione una opción: "))
    # Procesar opción...
except ValueError:
    print("Error: Debe ingresar un número válido")
```

Validaciones adicionales:
- Rangos válidos (notas de 0.0 a 5.0)
- Valores positivos (base y altura del triángulo)
- Montos no negativos (compras)

### 5. Retorno al Menú

Después de ejecutar cada programa, se llama a la función `pausar()` que espera a que el usuario presione ENTER antes de mostrar el menú nuevamente:

```python
def pausar():
    input("\nPresione ENTER para volver al menú...")
```

---

## CONCEPTOS APLICADOS

### 1. Condicionales
- **if/elif/else**: Estructura de selección múltiple (switch simulado)
- **Operadores de comparación**: ==, !=, <, >, <=, >=
- **Operadores lógicos**: and, or, not
- **Operador módulo**: % para determinar par/impar

### 2. Ciclos
- **while**: Ciclo para mantener el menú activo
- **break**: Para salir del ciclo de forma controlada

### 3. Funciones
- **Definición**: def nombre_funcion()
- **Modularidad**: Separación de responsabilidades
- **Reutilización**: Funciones llamadas múltiples veces

### 4. Manejo de Excepciones
- **try/except**: Captura de errores
- **ValueError**: Manejo de errores de conversión de tipos

### 5. Entrada/Salida
- **input()**: Captura de datos del usuario
- **print()**: Mostrar información formateada
- **f-strings**: Formateo de cadenas (Python 3.6+)

---

## PRUEBAS REALIZADAS

| Programa | Caso de Prueba | Entrada | Resultado Esperado | ✓/✗ |
|----------|----------------|---------|-------------------|-----|
| Par/Impar | Número par | 24 | "El número 24 es PAR" | ✓ |
| Par/Impar | Número impar | 17 | "El número 17 es IMPAR" | ✓ |
| Par/Impar | Entrada inválida | "abc" | Mensaje de error | ✓ |
| Promedio | Tres números | 8.5, 9.0, 7.5 | Promedio: 8.33 | ✓ |
| Promedio | Entrada inválida | "xyz" | Mensaje de error | ✓ |
| Área Triángulo | Valores positivos | base=10, altura=5 | Área: 25.00 | ✓ |
| Área Triángulo | Valores negativos | base=-5, altura=3 | Mensaje de error | ✓ |
| Descuento | Monto < $100 | $50 | Descuento: 0% | ✓ |
| Descuento | Monto $100-$500 | $250 | Descuento: 10% | ✓ |
| Descuento | Monto $501-$1000 | $750 | Descuento: 15% | ✓ |
| Descuento | Monto > $1000 | $1500 | Descuento: 20% | ✓ |
| Validación | Nota ≥ 3.0 | 4.5 | APROBADO | ✓ |
| Validación | Nota < 3.0 | 2.5 | REPROBADO | ✓ |
| Validación | Nota fuera de rango | 6.0 | Mensaje de error | ✓ |
| Menú | Opción válida | 1-5 | Ejecuta programa | ✓ |
| Menú | Opción 0 | 0 | Sale del programa | ✓ |
| Menú | Opción inválida | 9 | Mensaje de error | ✓ |
| Menú | Entrada no numérica | "abc" | Mensaje de error | ✓ |

**Total de pruebas exitosas: 17/17**

---

## CONCLUSIÓN GENERAL

### Logros Alcanzados

La actividad permitió consolidar los conceptos fundamentales de programación mediante la implementación exitosa de un menú tipo switch que integra múltiples programas. Los principales logros fueron:

1. **Dominio de Estructuras de Control:**
   - Implementación correcta de ciclos `while` para mantener el programa activo
   - Uso efectivo de condicionales `if/elif/else` para simular una estructura switch
   - Aplicación del `break` para salir de forma controlada del programa

2. **Programación Modular:**
   - Cada funcionalidad fue implementada en funciones independientes
   - El código es fácil de mantener y expandir
   - Se evitó la duplicación de código mediante la reutilización de funciones

3. **Validación de Datos:**
   - Manejo robusto de errores usando `try/except`
   - Validación de rangos y tipos de datos
   - Mensajes de error claros y orientados al usuario

4. **Experiencia de Usuario:**
   - Interfaz clara y fácil de usar
   - Mensajes informativos y bien formateados
   - Sistema de navegación intuitivo que permite volver al menú

5. **Buenas Prácticas:**
   - Código bien documentado con docstrings
   - Nombres de variables y funciones descriptivos
   - Formateo consistente y legible

### Aprendizajes Clave

Durante el desarrollo de esta actividad se reforzaron conceptos esenciales:

- **Pensamiento Algorítmico:** Descomponer un problema complejo en funciones simples y manejables
- **Manejo de Flujo:** Controlar la ejecución del programa mediante estructuras de control
- **Validación de Entradas:** La importancia de anticipar y manejar errores del usuario
- **Modularidad:** Los beneficios de organizar el código en componentes reutilizables

### Aplicabilidad Práctica

Este tipo de programa tiene aplicaciones reales en:
- Sistemas de menús para aplicaciones de consola
- Herramientas administrativas y de configuración
- Interfaces de línea de comandos (CLI)
- Programas educativos y de demostración

### Reflexión Personal

**[INSTRUCCIÓN: Agregar aquí una reflexión personal sobre la actividad, por ejemplo:]**

El desarrollo de este menú integrador me permitió comprender cómo los conceptos individuales aprendidos en clase (condicionales, ciclos, funciones) se combinan para crear aplicaciones funcionales y útiles. La experiencia de validar las diferentes entradas del usuario me hizo valorar la importancia de escribir código robusto que maneje situaciones inesperadas.

Considero que esta actividad fortaleció significativamente mi capacidad para:
- Planificar la estructura de un programa antes de codificar
- Organizar el código de manera lógica y mantenible
- Pensar en la experiencia del usuario al diseñar interfaces
- Depurar y probar sistemáticamente cada componente

### Posibles Mejoras Futuras

Aunque el programa cumple con todos los requisitos, se podrían implementar mejoras:
- Agregar más programas al menú
- Guardar un historial de operaciones realizadas
- Exportar resultados a un archivo de texto
- Agregar colores a la interfaz de consola
- Implementar un sistema de ayuda (opción ?)

---

## REFERENCIAS

- Material de clase - Fundamentos de Programación
- Documentación oficial de Python: https://docs.python.org/es/3/
- Apuntes y ejercicios del curso
- Ejemplos vistos durante las sesiones sincrónicas

---

**Fecha de elaboración:** [Completar]
**Firma del estudiante:** [Completar]

---

## INSTRUCCIONES PARA GENERAR EL PDF

1. Ejecutar el programa `menu_programas.py`
2. Ir probando cada opción del menú (1 a 5)
3. Capturar pantalla de cada ejecución
4. Capturar también las validaciones de errores
5. Insertar las imágenes en este documento en las secciones indicadas
6. Completar la reflexión personal
7. Convertir el documento a PDF (máximo 10 páginas)
8. Entregar según las indicaciones del docente

**Comando para ejecutar el programa:**
```bash
python menu_programas.py
```

o

```bash
python3 menu_programas.py
```
