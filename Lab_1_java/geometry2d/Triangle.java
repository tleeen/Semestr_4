package geometry2d;

import exception.Exc;
import exception.Exc_h;

public class Triangle implements Figure{

    public double x1, x2, x3, y1, y2, y3;
    
    public String Show(){
            String a;
            a = "Triangle:   x1 = " + x1 + "  y1 = " + y1 + "  " + "x2 = " + x2 + "  " + "y2 = " + y2 + "  " + "x3 = " + x3 + "  " + "y3 = " + y3;
            return a;
        }
    
    public double Area(){
            double a, b, c, s;
            a = Math.sqrt((x2 - x1) * (x2 - x1) + (y2 - y1) * (y2 - y1));
            b = Math.sqrt((x3 - x1) * (x3 - x1) + (y3 - y1) * (y3 - y1));
            c = Math.sqrt((x3 - x2) * (x3 - x2) + (y3 - y2) * (y3 - y2));
            double p = (a + b + c) / 2;
            s = Math.sqrt(p * (p - a) * (p - b) * (p - c));
            return s;
        }
    
    
        public Triangle(double side_x1, double side_x2, double side_x3, double side_y1, double side_y2, double side_y3) throws exception.Exc{
            this.x1 = (side_x1); 
            this.x2 = (side_x2); 
            this.x3 = (side_x3);
            this.y1 = (side_y1);
            this.y2 = (side_y2);
            this.y3 = (side_y3);
            if ((this.x1 == 0) && (this.x2 == 0) && (this.y1 == 0) && (this.y2 == 0) && (this.x3 == 0) && (this.y3 == 0))
                throw new exception.Exc("Error: Wrong triangle coordinate value");
        }
    };