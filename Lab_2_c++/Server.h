#include <iostream>
#include "IServer.h"
#include <cmath>

class Vector : public Info, public Operations
{
    private:
        int countReference = 0;
        double X, Y, Z;
    public:
        void Enter();
        void Print();
        void GetLength();
        void Add(double X1, double Y1, double Z1);
        void Diff(double X1, double Y1, double Z1);
        void Mult(double X1, double Y1, double Z1);

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

        H_RESULT QueryInterface(I_ID iid, void** ppv);
        U_LONG AddRef();
        U_LONG Release();

        ~Vector();
};