#include <iostream>
#include "IUnknown.h"
#include <cmath>

class Vector : public Info, public Operations
{
    private:
        int countReference = 0;
        double X, Y, Z;
    public:
        virtual void Enter();
        virtual void Print();
        virtual void GetLength();
        virtual void Add(double X1, double Y1, double Z1);
        virtual void Diff(double X1, double Y1, double Z1);
        virtual void Mult(double X1, double Y1, double Z1);

        Vector()
        {
            this->X = 0;
            this->Y = 0;
            this->Z = 0;
        }
 
        Vector(double x, double y, double z)
        {
            this->X = x;
            this->Y = y;
            this->Z = z;
        }

        H_RESULT_ QueryInterface(I_ID_, void**);
        U_LONG_ AddRef();
        U_LONG_ Release();

        ~Vector();
};