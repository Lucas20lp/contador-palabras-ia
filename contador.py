from collections import Counter

texto = input("Escribí un texto: ")

# Convertimos todo a minúsculas
texto = texto.lower()

# Separamos las palabras
palabras = texto.split()

# Contamos las palabras
contador = Counter(palabras)

print("\nCantidad total de palabras:", len(palabras))
print("\nFrecuencia de cada palabra:")

for palabra, cantidad in contador.items():
    print(palabra, ":", cantidad)