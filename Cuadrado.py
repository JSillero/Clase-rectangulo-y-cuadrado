'''
Created on 5 abr. 2019

@author: d18sisaj
'''
from Rectangulo import Rectangulo

class Cuadrado(Rectangulo):
    
    
    def __init__(self,lado):
        Rectangulo.__init__(self,lado,lado)
        
    @property   
    def lado(self):
        return self._alto
   
    '''NO RECONOCE LA PROPIEDAD EL SETER'''
    @lado.setter   
    def lado(self, lado):
        Rectangulo.alto(lado)
        Rectangulo.ancho(lado)
    
    def __eq__(self, cuadrado):
        if(self._alto==cuadrado._alto):
            return True
        else:
            return False

    def __gt__(self,cuadrado):
        if(self._alto>cuadrado._alto):
            return True
        else:
            return False
    
    def __lt__(self,cuadrado):
        if(self._alto<cuadrado._alto):
            return True
        else:
            return False
    
    def __ge__(self,cuadrado):
        if(self._alto>=cuadrado._alto):
            return True
        else:
            return False
        
    def __le__(self,cuadrado):
        if(self._alto<=cuadrado._alto):
            return True
        else:
            return False    