'''
Created on 5 abr. 2019

@author: d18sisaj
'''





class Rectangulo:
    '''
    Constructor de la clase rectangulo ,
    primer parametro, altura
    segundo parametro anchura
    '''
    def __init__(self,altura,anchura):
        if (altura>10|altura<1|anchura>10|altura<1):
            raise TypeError("Dato no valido")
            
            
        self._alto=altura
        self._ancho=anchura
        
    def getAlto(self):
        return self._alto
    
    def getAncho(self):
        return self._ancho
    
    def setAlto(self,altura):
        if(altura>10|altura<1):
            raise TypeError("Dato no valido")
        self._alto=altura
    
    def setAncho(self,anchura):
        if(anchura>10|anchura<1):
            raise TypeError("Dato no valido")
        
        self._ancho=anchura
    '''
    To string que muestra un dibujo de un rectangulo
    '''
    def __str__(self):
        imagen=""
        
        i=0
        while(i<self._ancho):
            imagen=imagen+"*"
            i=i+1
        imagen=imagen+"\n"
        i=0
        while(i<self._alto-2):
            i=i+1
            imagen=imagen+"*"
            e=0
            while(e<self._ancho-2):
                e=e+1
                imagen=imagen+" "
            if(self._ancho>1):
                imagen=imagen+"*"
            imagen=imagen+"\n"
        if(self._alto>=2):
            i=0
            while(i<self._ancho):
                i=i+1
                imagen=imagen+"*"
        return imagen
                
    
        
    
        