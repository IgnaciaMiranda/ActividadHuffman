# Codificación Huffman en Python

Este proyecto implementa el algoritmo de **codificación Huffman**, una técnica de compresión de datos sin pérdida que asigna códigos más cortos a los caracteres más frecuentes. El script permite analizar un texto dado, generar su versión comprimida, y visualizar estadísticas de compresión, incluyendo la representación del árbol de Huffman.

## Características

- Construcción del árbol de Huffman a partir de las frecuencias de caracteres.
- Generación de códigos binarios únicos para cada carácter.
- Codificación del texto original.
- Impresión visual del árbol de Huffman en consola.
- Cálculo de estadísticas como el tamaño original, tamaño comprimido, ratio de compresión y porcentaje de ahorro.

## Requisitos

- Python 3.x
- No se requieren librerías externas, todo se basa en módulos estándar (`heapq`, `collections`).

## Uso

Ejecuta el script directamente desde la línea de comandos:

```bash
python huffman.py
```
Ejemplo de funcionamiento:

analisis del texto 1
====================
texto original: 'La compresion de datos...'

tabla de frecuencias y codigos:
...
texto codificado (completo):
010110110101...

estadisticas de compresion:
- tamaño original: 2016 bits
- tamaño comprimido: 1120 bits
- ratio de compresion: 1.80:1
- ahorro de espacio: 44.44%

arbol de huffman (representacion en consola):
├── : Nodo interno (100)
    ├── 0: Nodo interno (45)
    ...
