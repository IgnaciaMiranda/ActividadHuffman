# Codificación Huffman en Python

Este proyecto implementa el algoritmo de **codificación Huffman**, una técnica de compresión de datos sin pérdida que asigna códigos más cortos a los caracteres más frecuentes. El script permite analizar un texto dado, generar su versión comprimida y visualizar estadísticas de compresión, incluyendo la representación del árbol de Huffman.

## Características

- Construcción del árbol de Huffman a partir de las frecuencias de caracteres.
- Generación de códigos binarios únicos para cada carácter.
- Codificación del texto original.
- Representación visual del árbol de Huffman en consola.
- Cálculo de estadísticas: tamaño original, tamaño comprimido, ratio de compresión y porcentaje de ahorro.

## Requisitos

- Python 3.x
- No se requieren librerías externas (se utilizan únicamente módulos estándar como `heapq` y `collections`).

## Uso

Ejecuta el script directamente desde la línea de comandos:

```bash
python huffman.py
