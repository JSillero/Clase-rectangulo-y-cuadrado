

  package ExamenSegundoTrimestre;

  public class Cuadrado extends Rectangulo {
    
    public Cuadrado(int alto) {
      super(alto,1);
      this.ancho=this.alto;
    }
    
    @Override
    public void setAlto(int alto2) {
      super.setAlto(alto2);
      this.ancho=this.alto;
    }
    
    @Override
    public void setAncho(int ancho2) {
      super.setAncho(ancho2);
      this.alto=this.ancho;
      
    }
    /**
     * Devuelve un boolean verdadero si los cuadrados son iguales y falso en caso contrario
     * @param cuad
     * @return
     */
    public boolean equals(Cuadrado cuad) {
      if(this.alto==cuad.alto)
        return true;
      else
        return false;
      
    }
    /**
     * Compara dos cuadrados y devuelve 0 si son iguales, -1 si el argumento es mayor y 1 si el
     * principal es mayor
     * @param cuad
     * @return
     */
    public int compareTo(Cuadrado cuad) {
      if(this.alto==cuad.alto)
        return 0;
      else if (this.alto>cuad.alto) {
        return 1;
        }
      else
        return -1;
      
    }
    
  }
