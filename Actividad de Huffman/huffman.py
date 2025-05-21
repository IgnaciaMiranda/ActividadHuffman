import heapq
from collections import Counter

class nodo:
    def __init__(self, caracter, frecuencia):
        self.caracter = caracter
        self.frecuencia = frecuencia
        self.izquierda = None
        self.derecha = None
    
    def __lt__(self, otro):
        # si las frecuencias son iguales, compara caracteres para mantener consistencia
        if self.frecuencia == otro.frecuencia:
            # usa una comparacion que funcione para None (caracteres internos)
            caracter_self = self.caracter if self.caracter is not None else ''
            caracter_otro = otro.caracter if otro.caracter is not None else ''
            return caracter_self < caracter_otro
        return self.frecuencia < otro.frecuencia

def calcular_frecuencias(texto):
    """calcula la frecuencia de cada caracter en el texto."""
    return Counter(texto)

def construir_arbol_huffman(frecuencias):
    """construye el arbol de huffman a partir de las frecuencias."""
    monticulo = [nodo(caracter, frec) for caracter, frec in frecuencias.items()]
    heapq.heapify(monticulo)
    
    # si solo hay un caracter unico
    if len(monticulo) == 1:
        nodo_temp = heapq.heappop(monticulo)
        nuevo_nodo = nodo(None, nodo_temp.frecuencia)
        nuevo_nodo.izquierda = nodo_temp
        heapq.heappush(monticulo, nuevo_nodo)
    
    # construir el arbol de huffman
    while len(monticulo) > 1:
        izquierda = heapq.heappop(monticulo)
        derecha = heapq.heappop(monticulo)
        fusionado = nodo(None, izquierda.frecuencia + derecha.frecuencia)
        fusionado.izquierda = izquierda
        fusionado.derecha = derecha
        heapq.heappush(monticulo, fusionado)
    
    return monticulo[0]  # devuelve la raiz del arbol

def generar_codigos(nodo_actual, prefijo="", codigos_huffman=None):
    """genera los codigos de huffman recorriendo el arbol."""
    if codigos_huffman is None:
        codigos_huffman = {}
    
    if nodo_actual:
        if nodo_actual.caracter is not None:  # si es un nodo hoja
            codigos_huffman[nodo_actual.caracter] = prefijo
        
        # recorrer los subarboles izquierdo y derecho
        generar_codigos(nodo_actual.izquierda, prefijo + "0", codigos_huffman)
        generar_codigos(nodo_actual.derecha, prefijo + "1", codigos_huffman)
    
    return codigos_huffman

def codificacion_huffman(texto):
    """codifica el texto usando codificacion huffman."""
    # si el texto esta vacio, devolver valores predeterminados
    if not texto:
        return "", {}, None
    
    # calcular frecuencias
    frecuencias = calcular_frecuencias(texto)
    
    # construir el arbol de huffman
    raiz = construir_arbol_huffman(frecuencias)
    
    # generar los codigos de huffman
    codigos_huffman = generar_codigos(raiz)
    
    # codificar el texto
    texto_codificado = ''.join(codigos_huffman[caracter] for caracter in texto)
    
    return texto_codificado, codigos_huffman, raiz

def imprimir_arbol(nodo_actual, nivel=0, prefijo=''):
    """imprime el arbol de huffman en la consola (version simplificada sin networkx)."""
    if nodo_actual:
        espacio = '    ' * nivel
        if nodo_actual.caracter is not None:
            print(f"{espacio}├── {prefijo}: '{nodo_actual.caracter}' ({nodo_actual.frecuencia})")
        else:
            print(f"{espacio}├── {prefijo}: Nodo interno ({nodo_actual.frecuencia})")
        
        imprimir_arbol(nodo_actual.izquierda, nivel + 1, '0')
        imprimir_arbol(nodo_actual.derecha, nivel + 1, '1')

def calcular_ratio_compresion(texto_original, texto_codificado):
    """calcula la eficiencia de la compresion."""
    # tamaño original (asumiendo 8 bits por caracter en ASCII/UTF-8)
    tamanio_original = len(texto_original) * 8
    
    # tamaño comprimido (bits)
    tamanio_comprimido = len(texto_codificado)
    
    # ratio de compresion
    ratio_compresion = tamanio_original / tamanio_comprimido if tamanio_comprimido > 0 else float('inf')
    
    # porcentaje de ahorro
    porcentaje_ahorro = (1 - tamanio_comprimido / tamanio_original) * 100 if tamanio_original > 0 else 0
    
    return tamanio_original, tamanio_comprimido, ratio_compresion, porcentaje_ahorro

def analizar_codificacion_huffman(texto, titulo="analisis de codificacion huffman"):
    """realiza un analisis simplificado de la codificacion huffman."""
    # realizar la codificacion
    texto_codificado, codigos_huffman, arbol_huffman = codificacion_huffman(texto)
    
    # calcular estadisticas de compresion
    tamanio_original, tamanio_comprimido, ratio_compresion, porcentaje_ahorro = calcular_ratio_compresion(
        texto, texto_codificado
    )
    
    # imprimir resultados
    print(f"\n{titulo}\n{'='*len(titulo)}")
    print(f"\ntexto original: '{texto}'")
    
    print("\ntabla de frecuencias y codigos:")
    for caracter, codigo in sorted(codigos_huffman.items(), key=lambda x: len(x[1])):
        # Muestra 'ESPACIO' en lugar de un espacio para mejor visibilidad
        char_display = 'ESPACIO' if caracter == ' ' else caracter
        print(f"'{char_display}': frecuencia={calcular_frecuencias(texto)[caracter]}, codigo={codigo}, longitud={len(codigo)}")
        
    print("\ntexto codificado (completo):")
    print(texto_codificado)
    
    print("\nestadisticas de compresion:")
    print(f"- tamaño original: {tamanio_original} bits ({len(texto)} caracteres × 8 bits)")
    print(f"- tamaño comprimido: {tamanio_comprimido} bits")
    print(f"- ratio de compresion: {ratio_compresion:.2f}:1")
    print(f"- ahorro de espacio: {porcentaje_ahorro:.2f}%")
    
    print("\narbol de huffman (representacion en consola):")
    imprimir_arbol(arbol_huffman)
    
    return {
        'texto': texto,
        'texto_codificado': texto_codificado,
        'codigos_huffman': codigos_huffman,
        'arbol_huffman': arbol_huffman,
        'tamanio_original': tamanio_original,
        'tamanio_comprimido': tamanio_comprimido,
        'ratio_compresion': ratio_compresion,
        'porcentaje_ahorro': porcentaje_ahorro
    }

def main():
    # texto sugerido en la actividad
    texto1 = "La compresion de datos es fundamental en el mundo digital. Reducir el tamaño de la informacion permite optimizar el almacenamiento, acelerar la transmision y mejorar la eficiencia de los sistemas. Uno de los algoritmos mas conocidos para esta tarea es el algoritmo de Huffman, que asigna codigos mas cortos a los simbolos mas frecuentes."
    
    # analizar el texto 1
    resultados1 = analizar_codificacion_huffman(texto1, "analisis del texto 1")
    
    # opcional: texto 2 (Alicia en el pais de las maravillas)
    texto2 = "Aquí todos estamos locos. Yo estoy loco. Tú estás loca. ¿Cómo sabes que yo estoy loca? Tienes que estarlo, o no habrías venido aquí."
    
    # analizar el texto 2
    resultados2 = analizar_codificacion_huffman(texto2, "analisis del texto 2")

if __name__ == "__main__":
    main()