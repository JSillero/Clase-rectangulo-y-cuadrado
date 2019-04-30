'''
Created on 5 abr. 2019

@author: d18sisaj
'''
from Rectangulo import Rectangulo

class Cuadrado(Rectangulo):
    
    
    def __init__(self,lado):
        self.setAlto(lado)
        
        
    
    def setAlto(self, altura):
        Rectangulo.setAlto(self, altura)
        self._ancho=altura
    
    def setAncho(self, anchura):
        Rectangulo.setAncho(self, anchura)
        self._alto=self._ancho
        



    def __eq__(self, cuadrado):
        if(self.getAlto()==cuadrado.getAlto()):
            return True
        else:
            return False

    def __gt__(self,cuadrado):
        if(self.getAlto()>cuadrado.getAlto()):
            return True
        else:
            return False
    
    def __lt__(self,cuadrado):
        if(self.getAlto()<cuadrado.getAlto()):
            return True
        else:
            return False
    
    def __ge__(self,cuadrado):
        if(self.getAlto()>=cuadrado.getAlto()):
            return True
        else:
            return False
    def __le__(self,cuadrado):
        if(self.getAlto()<=cuadrado.getAlto()):
            return True
        else:
            return False    