def magia_numerica(lista):
    '''Crea una nueva lista con la suma de los números pares de la lista original
    y los números pares ordenados de mayor a menor.'''
    lista_sin_duplicados = list(set(lista))
    lista_ordenada = sorted(lista_sin_duplicados, reverse=True)
    lista_pares = [num for num in lista_ordenada if num % 2 == 0]
    suma = sum(lista_pares)
    nueva_lista = [suma] + lista_pares
    
    if suma != sum(nueva_lista[1:]):
        raise ValueError("La suma no coincide con el primer elemento")
    
    return nueva_lista


if __name__ == "__main__":
    lista = [1, 1, 3, 4, 5, 6, 6, 7, 8, 8]
    print(f"Lista original: {lista}")
    resultado = magia_numerica(lista)
    print(f"Lista procesada: {resultado}")