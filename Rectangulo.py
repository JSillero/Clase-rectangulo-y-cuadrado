'''
Created on 5 abr. 2019

@author: d18sisaj
'''





class Rectangulo(Exception):
    '''
    Constructor de la clase rectangulo ,
    primer parametro, altura
    segundo parametro anchura
    '''
    def __init__(self,altura,anchura):
        Exception.__init__(self)
        if (altura>10|altura<1|anchura>10|altura<1):
            print("Error")
            raise ValueError("Dato no valido")
            print("Error")
        
        self._alto=anchura
        self._ancho=altura
    
    @property
    def alto (self):
        return self._alto
    
    @alto.setter
    def alto(self,alto):
        if(alto>10|alto<1):
            print("Error")
            raise ValueError("Dato no valido")
        self._alto=alto
    
    @property
    def ancho(self):
        return self._ancho
    
    @ancho.setter
    def ancho(self,ancho):
        if(ancho>10|ancho<1):
            raise ValueError("Dato no valido")
        
        self._ancho=ancho
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
                
    
        
Rectangulo    
        