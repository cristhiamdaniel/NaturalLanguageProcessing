# Dividir el texto en oraciones

import nltk

"""
# Cargar el texto
nombre_archivo = "nlp.txt"
archivo = open(nombre_archivo, "r", encoding="utf-8")
texto = archivo.read()

# print(texto)
"""

# Crear un texto en espaniol
texto = "Hola. Soy un texto en español. ¿Cómo estás? Espero que bien. ¿Qué tal? ¿Qué tal te va? ¿Qué tal te va con el curso de Procesamiento de Lenguaje Natural?"

# Tokenizar el texto en oraciones

tokenizador = nltk.data.load('tokenizers/punkt/english.pickle')
oraciones = tokenizador.tokenize(texto)

"""
# Imprimir las oraciones
for oracion in oraciones:
    print(oracion)
    print("")
"""

# Dividir el texto en palabras
palabras = nltk.word_tokenize(texto)

# Imprimir las palabras
for palabra in palabras:
    print(palabra)
    print("")

