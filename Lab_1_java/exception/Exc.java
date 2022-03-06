package exception;

public class Exc extends Exception{

    public String a;
    
    public void error(){
        System.out.println(a);
        }
        
        public Exc(String text){
    
            a = text;
        }
    }

