from ArbolBinario import ArbolBinario

def main():
    # Instancia
    arbol = ArbolBinario()


    # Agregacion
    arbol.agregarIterativo(8)
    arbol.agregarIterativo(5)
    arbol.agregarIterativo(10)
    arbol.agregarIterativo(4)
    arbol.agregarIterativo(7)
    arbol.agregarIterativo(9)
    arbol.agregarIterativo(12)
    arbol.agregarIterativo(3)
    arbol.agregarIterativo(6)
    # arbol.agregarIterativo(arbol.raiz, 6)
    
    # Recorrido
    arbol.inorden()
    arbol.inorderTraversal()

    arbol.deleteNode(arbol.raiz, 6)
    arbol.inorden()
    arbol.inorderTraversal()
    # arbol.preorden()
    # arbol.postorden()
    
    # # Búsqueda
    # busqueda = input("Busca algo en el árbol: ")
    # nodo = arbol.buscar(int(busqueda))
    # if nodo is None:
    #     print(f"{busqueda} no existe")
    # else:
    #     print(f"{busqueda} sí existe")
  
    # # Prueba metodos vacio y eshoja
    # arbol2 = ArbolBinario()
    # arbol2.agregar(1)
    # print("El arbol2 esta vacio: " + str(arbol2.vacio()))
    # print("La raiz del arbol2 es hoja: " + str(arbol2.esHoja()))
    print(arbol.fibonacci(6))
  

if __name__ == '__main__':
    main()