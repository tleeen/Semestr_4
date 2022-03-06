package test;

import java.util.Scanner;
import geometry2d.Figure;
import geometry2d.Triangle;
import geometry2d.Rectangle;
import geometry2d.Square;
import geometry2d.Ellipse;
import geometry2d.Circle;
import exception.Exc;
import exception.Exc_h;
import geometry3d.Cylinder;

public class Main{
    public static void main(String[] args){
    int a;
    Scanner num = new Scanner(System.in);
    do{
        System.out.println("Enter job number 1-2 (enter '0' to exit)" );
        a = num.nextInt();
        try 
        {
            if (((a > 3) || (a < 1)) && (a != 0)) throw new exception.Exc("Invalid job number entered");
        }
        catch (Throwable exception)
        {
            System.out.println("Error: " + exception);
            a = num.nextInt();
        }
        switch (a)
        {
        case 1:{
            try{
            Figure figure [] = new geometry2d.Figure[5];
            System.out.println("\nFigure #1 (triangle):");
            figure[0] = new Triangle(0, 0, 30, 0, 40, 0);
            System.out.println( figure[0].Show()) ;
            System.out.println( "\nSquare: ");
            System.out.println(figure[0].Area());

            System.out.println("\n\nFigure #2 (circle):");
            figure[1] = new geometry2d.Circle(0, 0, 0, 20);
            System.out.println(figure[1].Show()) ;
            System.out.println("\nSquare: ");
            System.out.println(figure[1].Area());

            System.out.println("\n\nFigure #3 (ellipse):");
            figure[2] = new geometry2d.Ellipse(0, 0, 50, -30, 30, -20, 0, 0);
            System.out.println(figure[2].Show()) ;
            System.out.println("\nSquare: ");
            System.out.println(figure[2].Area());

            System.out.println("\n\nFigure #4 (rectangle):");
            figure[3] = new geometry2d.Rectangle(0, 0, 0, 50, 40, 40, 50, 0);
            System.out.println(figure[3].Show())  ;
            System.out.println( "\nSquare: ");
            System.out.println(figure[3].Area());

            System.out.println("\n\nFigure #5 (square):");
            figure[4] = new geometry2d.Square(0, 0, 0, 50, 50, 50, 50, 0);
            System.out.println(figure[4].Show()) ;;
            System.out.println("\nSquare: ");
            System.out.println(figure[4].Area());
            System.out.println( ) ;
            }
            catch (Exc Exc) 
            {
                Exc.error();
                System.exit(1);
            }
        }
        break;
        case 2:{
            try{
            try{
            Cylinder prism [] = new geometry3d.Cylinder [5];
            Figure figure [] = new geometry2d.Figure [5];
            System.out.println("\nFigure #1 (triangle):");
            figure[0] = new geometry2d.Triangle(0, 0, 30, 0, 40, 0);
            prism[0] = new geometry3d.Cylinder(5, figure[0]);
            System.out.println( figure[0].Show());
            System.out.println( "\nVolume: ");
            System.out.println(prism[0].Volume());


            System.out.println("\n\nFigure #2 (circle):");
            figure[1] = new geometry2d.Circle(0, 0, 0, 20);
            prism[1] = new geometry3d.Cylinder(5, figure[1]);
            System.out.println(figure[1].Show());
            System.out.println("\nVolume: ");
            System.out.println(prism[1].Volume());

            System.out.println("\n\nFigure #3 (ellipse):");
            figure[2] = new geometry2d.Ellipse(0, 0, 50, -30, 30, -20, 0, 0);
            prism[2] = new geometry3d.Cylinder(5, figure[2]);
            System.out.println(figure[2].Show());
            System.out.println("\nVolume: ");
            System.out.println(prism[2].Volume());

            System.out.println("\n\nFigure #4 (rectangle):");
            figure[3] = new geometry2d.Rectangle(0, 0, 0, 50, 40, 40, 50, 0);
            prism[3] = new geometry3d.Cylinder(5, figure[3]);
            System.out.println(figure[3].Show());
            System.out.println("\nVolume: ");
            System.out.println(prism[3].Volume());

            System.out.println("\n\nFigure #5 (square):");
            figure[4] = new geometry2d.Square(0, 0, 0, 50, 50, 50, 50, 0);
            prism[4] = new geometry3d.Cylinder(5, figure[4]);
            System.out.println( figure[4].Show());
            System.out.println("\nVolume: ");
            System.out.println(prism[4].Volume());
            System.out.println( ) ;
            }
            catch (Exc_h Exc_h)
            {
                Exc_h.error();
                System.exit(1);
            }
            }
            catch (Exc Exc)
            {
                Exc.error();
                System.exit(1);
            }
        }
        break;
        }
    } while (a != 0);
}
}