from googlesearch import search

goglle_query = str(input("Ingresa tu búsqueda: "))

print("Resultados de la búsqueda:")

for result in search(goglle_query, start=0, pause=2):
    print(result)
