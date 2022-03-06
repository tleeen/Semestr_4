package geometry2d;

import exception.Exc;
import exception.Exc_h;

public class Square implements Figure{

    public double x1, x2, x3, x4, y1, y2, y3, y4;
    
    public String Show(){
            String a;
            a = "Square:   x1 = " + (x1) + "  y1 = " + (y1) + "  " + "x2 = " + (x2) + "  " + "y2 = " + (y2) + "  " + "x3 = " + (x3) + "  " + "y3 = " + (y3) + "  " + "x4 = " + (x4) + "  " + "y4 = " + (y4);
            return a;
        }

    public double Area(){
            double a, s;
            a = Math.sqrt((x2 - x1) * (x2 - x1) + (y2 - y1) * (y2 - y1));
            s = a * a;
            return s;
        }
    
        public Square(double side_x1, double side_x2, double side_y1, double side_y2, double side_x3, double side_x4, double side_y3, double side_y4) throws exception.Exc{
            this.x1 = (side_x1); 
            this.x2 = (side_x2); 
            this.x3 = (side_x3);
            this.x4 = (side_x4);
            this.y1 = (side_y1);
            this.y2 = (side_y2);
            this.y3 = (side_y3);
            this.y4 = (side_y4);
            if ((this.x1 == 0) && (this.x2 == 0) && (this.y1 == 0) && (this.y2 == 0) && (this.x3 == 0) && (this.y3 == 0) && (this.x4 == 0) && (this.y4 == 0))
                throw new exception.Exc("Error: Wrong square coordinate value");
        }
    };