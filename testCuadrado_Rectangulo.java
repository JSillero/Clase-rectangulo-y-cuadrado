package ExamenSegundoTrimestre;

public class testCuadrado_Rectangulo {

  public static void main(String[] args) {
    // TODO Auto-generated method stub
    
    
    Rectangulo rec2= new Rectangulo(2,5);
    Rectangulo rec3= new Rectangulo(4,7);
   
    System.out.println(rec3);
    System.out.println("El alto es:"+rec3.getAlto());
    System.out.println("El ancho es:"+rec3.getAncho());
    rec3.setAlto(3);
    System.out.println("El nuevo alto es:"+rec3.getAlto());
    Cuadrado cuad1= new Cuadrado(5);
    Cuadrado cuad2= new Cuadrado(6);
    Cuadrado cuad3= new Cuadrado(4);
    System.out.println(cuad1);
    cuad1.setAlto(7);
    System.out.println(cuad1);
    if(cuad1.equals(cuad2)) {
      System.out.println("Son iguales");
    }else {
      System.out.println("No son iguales");
    }
    try {
      Rectangulo rec1= new Rectangulo(11,5);
      
      }catch (ArithmeticException e){
        System.err.println("Error al crear un rectangulo, valores invalidos");
      }
  }

}
