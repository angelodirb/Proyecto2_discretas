
def set(set_, n):
    for i in range(n):
        conj = {i + 1}
        set_.append(conj)
    return set_

def union(conjuntos, conjunto1, conjunto2):

    if conjunto1 == conjunto2:
        print("Error: No puedes unir el mismo conjunto consigo mismo.")
                
    else:
        index1 = None
        index2 = None

        for i, conj in enumerate(conjuntos):
            if conjunto1 in conj: 
                index1 = i
            
            if conjunto2 in conj:  
                index2 = i

        new_conjunto = conjuntos[index1] | conjuntos[index2]

     
        for i in sorted([index1, index2], reverse=True):
            del conjuntos[i]

        conjuntos.append(new_conjunto)
        return conjuntos
    
def particiones(numero, maximo=None):
    if maximo is None:
        maximo = numero
    if numero == 0:
        return [[]]
    if numero < 0:
        return []
    
    resultados = []
    for i in range(1, maximo + 1):
        for subresultado in particiones(numero - i, i):
            resultados.append([i] + subresultado)
    return resultados

# Función para mostrar las combinaciones y contar cuántas hay
def mostrar_combinaciones(numero):
    combinaciones = particiones(numero)
    return len(combinaciones)

def main(setinput):
    contador = 0
    print("Ingrese primero el numero de elementos y luego el numero de operaciones")
    imput = str(input(": "))


    lista = imput.split()

    N = int(lista[0])

    M = int(lista[1])
    
    set(setinput, N)
    permutaciones = []
    while contador < M:
        
        op = str(input("Ingrese operacion: "))
        string = op.split()
        
        if string[0] == "union":
            union(setinput, int(string[1]), int(string[2]))   
            contador += 1

        elif string[0] == "interseccion":
            element = int(string[1])
            for i, conj in enumerate(setinput):
                if element in conj:  # Si el valor está en el conjunto
                    size_set = len(conj)
                    permutaciones.append(mostrar_combinaciones(size_set))
                    contador += 1
    for i in permutaciones:
        print(i)   



T = int(input("Ingrese el número de casos de prueba: "))

contador = 0

while contador < T:
    conjunto = []
    main(conjunto)
    contador += 1


