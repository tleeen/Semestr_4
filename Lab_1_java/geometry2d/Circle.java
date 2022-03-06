package geometry2d;

import exception.Exc;
import exception.Exc_h;

public class Circle implements Figure{

    public double x1, x2, y1, y2;
    
    public String Show(){
            String a;
            a = "Circle:   x1 = " + (x1) + "  y1 = " + (y1) + "  " + "x2 = " + (x2) + "  " + "y2 = " + (y2);
            return a;
        }
    
    public double Area(){
            double r, s;
            r = Math.sqrt((x2 - x1) * (x2 - x1) + (y2 - y1) * (y2 - y1));
            s = M_PI * r * r;
            return s;
        }
    
        public Circle(double side_x1, double side_x2, double side_y1, double side_y2) throws exception.Exc{
            this.x1 = (side_x1); 
            this.x2 = (side_x2); 
            this.y1 = (side_y1);
            this.y2 = (side_y2);
            if ((this.x1 == 0) && (this.x2 == 0) && (this.y1 == 0) && (this.y2 == 0))
                throw new exception.Exc("Error: Wrong circle coordinate value");
        }
    
    };