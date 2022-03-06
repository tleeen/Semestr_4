package exception;

public class Exc_h extends Exception{

    public double a;
    
    public void error(){
        System.out.println("Error: cylinder height entered incorrectly: " + a);
        }
        
        public Exc_h(double h){
    
            a = h;
        }
    }