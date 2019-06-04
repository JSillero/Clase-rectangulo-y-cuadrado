'''
Created on 5 abr. 2019

@author: d18sisaj
'''
from Cuadrado import Cuadrado
from Rectangulo import Rectangulo

rect=Rectangulo(4,5)
print(rect)
rect.alto(7)



cuad=Cuadrado(5)


print(cuad)
print("Lado del cuadrado",cuad.lado)
cuad.lado(6)
print("Lado del cuadrado",cuad.lado)
