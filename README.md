# Menú de Programas - Fundamentos de Programación

## 📋 Descripción

Programa desarrollado para la asignatura de Fundamentos de Programación que implementa un menú tipo switch con 5 programas básicos. El proyecto cumple con todos los requisitos de la actividad académica.

## 📁 Archivos del Proyecto

1. **`menu_programas.py`** - Programa principal con el menú switch
2. **`INFORME_ACTIVIDAD.md`** - Documento base para el informe en PDF
3. **`EJEMPLOS_EJECUCION.md`** - Ejemplos detallados de cada opción
4. **`README.md`** - Este archivo con instrucciones

## 🚀 Cómo Ejecutar el Programa

### Requisitos
- Python 3.6 o superior instalado

### Ejecución

```bash
python menu_programas.py
```

o en algunos sistemas:

```bash
python3 menu_programas.py
```

## 📊 Programas Incluidos

| # | Programa | Descripción |
|---|----------|-------------|
| 1 | Par o Impar | Determina si un número es par o impar |
| 2 | Promedio de 3 Números | Calcula el promedio aritmético |
| 3 | Área de un Triángulo | Calcula el área (base × altura) / 2 |
| 4 | Descuento por Compra | Aplica descuentos escalonados |
| 5 | Validación Aprobado/Reprobado | Valida notas de estudiantes |
| 0 | Salir | Termina el programa |

## 📝 Cómo Generar el Entregable PDF

### Paso 1: Ejecutar y Capturar
1. Ejecuta el programa: `python menu_programas.py`
2. Captura pantalla del menú principal
3. Prueba cada opción (1-5) y captura las pantallas
4. Prueba también opciones inválidas para mostrar las validaciones

### Paso 2: Preparar el Documento
1. Abre el archivo `INFORME_ACTIVIDAD.md`
2. Inserta las capturas de pantalla en las secciones indicadas
3. Completa la reflexión personal al final
4. Revisa que todo esté completo

### Paso 3: Convertir a PDF
Puedes usar cualquiera de estos métodos:

**Opción A - Usando un editor Markdown:**
- Visual Studio Code con extensión "Markdown PDF"
- Typora
- MarkdownPad

**Opción B - Online:**
- https://www.markdowntopdf.com/
- https://cloudconvert.com/md-to-pdf

**Opción C - Copiar a Word/Google Docs:**
- Copia el contenido del informe
- Pégalo en Word o Google Docs
- Inserta las imágenes
- Exporta como PDF

### Paso 4: Verificar
- ✓ El PDF tiene máximo 10 páginas
- ✓ Incluye imágenes del menú y de cada programa
- ✓ Tiene la conclusión general al final
- ✓ No incluye archivos .py ni .pseint

## 🎯 Características Implementadas

✅ **Ciclo while** para repetir el menú
✅ **Estructura switch** usando if/elif/else
✅ **Funciones modulares** para cada programa
✅ **Validación de entradas** con try/except
✅ **Retorno al menú** después de cada ejecución
✅ **Salida controlada** con opción 0
✅ **Mensajes de error** claros y descriptivos

## 📚 Conceptos de Programación Aplicados

- Estructuras de control (if/elif/else)
- Ciclos (while, break)
- Funciones y modularidad
- Manejo de excepciones (try/except)
- Validación de datos
- Entrada/Salida (input/print)
- Formateo de strings (f-strings)
- Operadores aritméticos y lógicos

## 🧪 Casos de Prueba Recomendados

### Programa 1 - Par o Impar
- Probar con: 24 (par), 17 (impar), "abc" (error)

### Programa 2 - Promedio
- Probar con: 8.5, 9.0, 7.5

### Programa 3 - Área Triángulo
- Probar con: base=10, altura=5
- Probar con: base=-5, altura=3 (error)

### Programa 4 - Descuento
- Probar con: $50 (0%), $250 (10%), $750 (15%), $1500 (20%)

### Programa 5 - Validación
- Probar con: nota=4.5 (aprobado), nota=2.5 (reprobado)
- Probar con: nota=6.0 (error - fuera de rango)

### Validación del Menú
- Probar con: 9 (opción inválida)
- Probar con: "abc" (entrada no numérica)
- Probar con: 0 (salir)

## 👨‍🎓 Información Académica

**Asignatura:** Fundamentos de Programación
**Docente:** Jorge Andrés Araujo Bernal
**Actividad:** Menú tipo Switch con múltiples programas

## 💡 Consejos para el Informe

1. **Capturas de pantalla:** Asegúrate de que se vean claras y completas
2. **Ejemplos diversos:** Muestra diferentes casos de uso para cada programa
3. **Validaciones:** No olvides capturar los mensajes de error
4. **Conclusión:** Reflexiona sobre lo aprendido, no solo describas
5. **Formato:** Mantén un formato profesional y ordenado

## 📧 Soporte

Para dudas sobre el código, revisa los comentarios en `menu_programas.py`.
Para ejemplos de ejecución, consulta `EJEMPLOS_EJECUCION.md`.

---

**¡Éxito con tu entrega! 🎓**