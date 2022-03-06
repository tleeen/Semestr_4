package geometry3d;

import geometry2d.*;
import exception.Exc_h;

public class Cylinder{

    public geometry2d.Figure figure;
    public double h;
    
    public double Volume(){
            return h * (figure.Area());
        }
    
        public Cylinder(double h, geometry2d.Figure figure) throws exception.Exc_h{
            if (h < 0)
                throw new exception.Exc_h(h);
            this.h = h;
            this.figure = figure;
        }
    };