

/**
 * 2.- (Java) Crea la clase Rectángulo de forma que:
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

compares to, y equals para python

 * @param args
 */
  public class Rectangulo{
    protected int alto;
    protected int ancho;
    /**
     * 
     * @param alto
     * @param ancho
     */
    public Rectangulo(int alto, int ancho) {
      
      setAncho(ancho);
      setAlto(alto);
    }
    /**
     * Camia el valor del ancho de un rectangulo al parametro introducido, si es valido
     * @param ancho2
     */
    public void setAncho(int ancho2) {
     
      if(ancho2>10||ancho2<1)
        throw new ArithmeticException();
      
      this.ancho=ancho2;
    }
    /**
     * Cambio el valor del alto de un rectangulo al parametro introducido, si es valido
     * @param alto2
     * 
     */
    public void setAlto(int alto2) {
     
      if(alto2>10||alto2<1)
        throw new ArithmeticException();
      
      this.alto=alto2;
      
    }
    
    public int getAlto() {
      return this.alto;
    }
    
    public int getAncho() {
      return this.ancho;
    }
    
    /**
     * Cuando se pide que se muestre por pantalla devuelve una imagen de un rectangulo acorde a sus dimensiones
     */
    public String toString() {
      String imagen="";
      for(int i=0;i<this.ancho;i++) {
        imagen=imagen+"*";
      }
      imagen=imagen+"\n";
      for(int i=0;i<this.alto-2;i++) {
        imagen=imagen+"*";
        
        for(int e=0;e<this.ancho-2;e++) {
          imagen=imagen+" ";
        }
        
        if(this.ancho>1) {
          imagen=imagen+"*";
        }
        imagen=imagen+"\n";
      }
      if(this.alto>=2) {
        for(int i=0;i<this.ancho;i++) {
          imagen=imagen+"*";
        }
      }
      
      return imagen;
    }
    
  }

