'''
Title: ArbolBinario
Author: Alex Ticlla Choque
Created: 03/27/24
Version: 1.0
'''
from Nodo import Nodo

class ArbolBinario:
    """
    Clase ArbolBinario representa la estructura de un arbol binario
    """
    def __init__(self, dato=None):
        """
        Constructor de la clase ArbolBinario si se le proporciona un dato
        entonces la raiz del arbol contiene el dato, sino la raiz es nula. 
        """
        if dato is not None:
            self.raiz = Nodo(dato)
        else:
            self.raiz = None

    
    # Metodos Privados 

    def __agregar_recursivo(self, current_nodo, dato):
        # Metodo auxiliar para el metodo 'agregar'
        if dato < current_nodo.dato:
            if current_nodo.izquierda is None:
                current_nodo.izquierda = current_nodo(dato)
            else:
                self.__agregar_recursivo(current_nodo.izquierda, dato)
        elif dato > current_nodo.dato:
            if current_nodo.derecha is None:
                current_nodo.derecha = current_nodo(dato)
            else:
                self.__agregar_recursivo(current_nodo.derecha, dato)
        else:
            print("El dato a ingresar ya existe en el arbol")

    def __inorden_recursivo(self, current_nodo):
        # Metodo recursivo imprime el contenido de un arbol en inorden
    
        # Caso base
                
        if current_nodo is not None:
            self.__inorden_recursivo(current_nodo.izquierda)
            print(current_nodo.dato, end=", ")
            self.__inorden_recursivo(current_nodo.derecha)

    def __preorden_recursivo(self, current_nodo):
        # Metodo recursivo imprime el contenido de un arbol en preorden

        if current_nodo is not None:
            print(current_nodo.dato, end=", ")
            self.__preorden_recursivo(current_nodo.izquierda)
            self.__preorden_recursivo(current_nodo.derecha)

    def __postorden_recursivo(self, current_nodo):
        # Metodo recursivo imprime el contenido de un arbol en postorden

        if current_nodo is not None:
            self.__postorden_recursivo(current_nodo.izquierda)
            self.__postorden_recursivo(current_nodo.derecha)
            print(current_nodo.dato, end=", ")

    def __buscar(self, current_nodo, busqueda):
        # Metodo recursivo para buscar un valor 'busqueda'
        if current_nodo is None:
            return None
        if current_nodo.dato == busqueda:
            return current_nodo
        if busqueda < current_nodo.dato:
            return self.__buscar(current_nodo.izquierda, busqueda)
        else:
            return self.__buscar(current_nodo.derecha, busqueda)

    # Funciones públicas

    def agregar(self, dato):
        # Metodo para agregar un 'dato' de cualquier tipo al Arbol
        if self.raiz is None:
            self.raiz = Nodo(dato)
        else:
            self.__agregar_recursivo(self.raiz, dato)

    def inorden(self):
        # Metodo para imprimir el contenido de un arbol de manera inorden
        print("Imprimiendo árbol inorden recursivamente: ")
        self.__inorden_recursivo(self.raiz)
        print("")

    def preorden(self):
        # Metodo para imprimir el contenido de un arbol de manera preorden
        print("Imprimiendo árbol preorden recursivamente: ")
        self.__preorden_recursivo(self.raiz)
        print("")

    def postorden(self):

        # Metodo para imprimir el contenido de un arbol de manera postorden
        print("Imprimiendo árbol postorden recursivamente: ")
        self.__postorden_recursivo(self.raiz)
        print("")

    def buscar(self, busqueda):
        # Funcion de busqueda
        return self.__buscar(self.raiz, busqueda)
    
    def vacio(self):
        return self.raiz == None
    
    def esHoja(self, node):
        # Solo funciona para arboles con un nodo
        if node is None:
            return False
        
        if (node.derecha is None) and (node.izquierda is None):
            return True
        
        return False
        
    # Funciones iterativas
    def agregarIterativo(self, value):
        '''Metodo iterativo para agregar un valor al arbol.
        Parametros: self.raiz, dato'''
        previous_node = None
        current_node = self.raiz
        if current_node is None:
            self.raiz = Nodo(value)
        else:
            while current_node is not None:
                previous_node = current_node

                if value > current_node.dato:
                    current_node = current_node.derecha
                elif value < current_node.dato:
                    current_node = current_node.izquierda
                else:
                    return
                
            new_node = Nodo(value)
            if value > previous_node.dato:
                previous_node.setHijoDerecha(new_node)
            else:
                previous_node.setHijoIzquierda(new_node)
            return
        
    def iterativeInorder(self, current_node):
        '''
        Metodo de recorrido inorder traversal iterativo
        toma como parametro a un nodo actual, que en primera instancia
        es la raiz del arbol
        '''
        if current_node is None:
            print('El arbol se encuentra vacio')
            return
        
        print('Imprimiendo el arbol iterativamente inorder traversal: ')
        pila = []
        while current_node or pila:
            while current_node:
                pila.append(current_node)
                current_node = current_node.izquierda
            current_node = pila.pop()
            print(str(current_node.dato) + ', ', end='')
            current_node = current_node.derecha
        print()
        return
    
    def inorderTraversal(self):
        self.iterativeInorder(self.raiz)
    

    def deleteNode(self, root, key):
            # Base case
        if root is None:
            return root
        # If the key to be deleted is smaller than the root's key, then it lies in the left subtree
        if key < root.dato:
            root.izquierda = self.deleteNode(root.izquierda, key)
        # If the key to be deleted is greater than the root's key, then it lies in the right subtree
        elif key > root.dato:
            root.derecha = self.deleteNode(root.derecha, key)
        # If key is same as root's key, then this is the node to be deleted
        else:
            # Node with only one child or no child
            if root.izquierda is None:
                return root.derecha
            elif root.derecha is None:
                return root.izquierda

            # Node with two children: Get the inorder successor (smallest in the right subtree)
            root.dato = self.minValue(root.derecha)

            # Delete the inorder successor
            root.derecha = self.deleteNode(root.derecha, root.dato)
        return root

    def minValue(self, root):
        minv = root.dato
        while root.izquierda:
            minv = root.izquierda.key
            root = root.izquierda
        return minv
