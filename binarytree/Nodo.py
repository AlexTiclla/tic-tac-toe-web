'''
Title: Nodo
Author: Alex Ticlla Choque
Created: 03/27/24
Version: 1.0
'''
class Nodo:
    '''
    This class represents a node data structure for a tree
    data structure. It has three attributes a value, a
    left child and a right child
    '''
    def __init__(self, valor):
        '''
        Constructor method. The constructor takes as input
        an object value and sets it
        '''
        self.dato = valor
        self.izquierda = None
        self.derecha = None    

    @property
    def getDato(self):
        return self.dato
    
  
    def getHijoIzquierda(self):
        return self.izquierda
    

    def getHijoDerecha(self):
        return self.derecha
    
    def setDato(self, valor):
        self.dato = valor


    def setHijoIzquierda(self, hijoIzquierdo):
        self.izquierda = hijoIzquierdo

  
    def setHijoDerecha(self, hijoDerecho):
        self.derecha = hijoDerecho




