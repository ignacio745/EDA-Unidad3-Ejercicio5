from ListaSecuencial import ListaSecuencial


if __name__ == "__main__":
    unaLista = ListaSecuencial(10, int)
    unaLista.insertar(10, 1)
    unaLista.insertar(5, 2)
    unaLista.insertar(7, 3)
    unaLista.insertar(5, 4)
    unaLista.insertar(2, 5)
    unaLista.insertar(10, 6)

    print("Lista antes de eliminar repetidos")
    unaLista.recorrer(print)

    i = 1

    while i <= unaLista.cantidad()-1:

        j = i+1

        while j <= unaLista.cantidad():
            if unaLista.recuperar(i) == unaLista.recuperar(j):
                unaLista.suprimir(j)
            else:
                j += 1
        
        i += 1

    print("Lista luego de eliminar repetidos")

    unaLista.recorrer(print)