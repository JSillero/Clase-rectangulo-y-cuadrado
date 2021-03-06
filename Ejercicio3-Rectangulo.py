'''
Created on 5 abr. 2019
EN PYTHON 3. Crea la clase Rectángulo de forma que:
• Un objeto de esta clase se construye pasándole el ancho y el alto. Ninguno de los dos atributos
puede ser menor o igual a cero ni mayor que diez, en esos casos se debe lanzar la excepción
ArithmeticException.
• Mediante getters y setters permite que se acceda y se modifique el ancho y el alto del
rectángulo teniendo en cuenta las restricciones en cuanto a las dimensiones del apartado
anterior.
• Al imprimir en pantalla un objeto de la clase usando System.out.print se debe dibujar el
rectángulo por la pantalla (de manera similar a como se imprime un cuadrado en la página 130
del libro Aprende Java con Ejercicios).
• Crea la clase Cuadrado como subclase de Rectángulo. Le debes añadir a su comportamiento
la posibilidad de comparar objetos cuadrados entre sí.
• Crea los programas de test correspondientes a ambas clases. Debes provocar que se lance la
excepción y capturarla.

equals y compareto
@author: d18sisaj
'''
from Rectangulo import Rectangulo
from Cuadrado import Cuadrado

cuad=Cuadrado(15)
cuad2=Cuadrado(4)
cuad3=Cuadrado(3)
cuad4=Cuadrado(4)
rect=Rectangulo(3,11)
print(cuad)
print(rect)
print(rect.ancho)
if(cuad2==cuad4):
    print("Son iguales")
else:
    print("Son diferentes")
    
if(cuad3>cuad4):
    print("Primero es mayor")
else:
    print("Segundo es mayor")
    
if(cuad3<cuad4):
    print("Primero es menos")
else:
    print("Segundo es mayor")