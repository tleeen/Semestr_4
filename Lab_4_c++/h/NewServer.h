#include "IUnknown.h"
#include "Server.h"
#pragma once

class NewVector: public Info, Operations, NewFunction{
    private:
        int countReference = 0;
        double X, Y, Z;
        Vector* Vector_old;
    public:
        virtual void Enter();
        virtual void Print();
        virtual void GetLength();
        virtual void Add(double X1, double Y1, double Z1);
        virtual void Diff(double X1, double Y1, double Z1);
        virtual void Mult(double X1, double Y1, double Z1);
        virtual void Sin(double X1, double Y1, double Z1);
        virtual void Cos(double X1, double Y1, double Z1);
        virtual void Colinarity(double X1, double Y1, double Z1);
        virtual void Angle(double X1, double Y1, double Z1);

        NewVector()
        {
            this->X = 0;
            this->Y = 0;
            this->Z = 0;
            CreateInstance(101, 2, (void**)&this->Vector_old);
        }
 
        NewVector(double x, double y, double z)
        {
            this->X = x;
            this->Y = y;
            this->Z = z;
            CreateInstance(101, 2, (void**)&this->Vector_old);
        }

        H_RESULT_ virtual QueryInterface(I_ID_, void**);
        U_LONG_ AddRef();
        U_LONG_ Release();
        

    ~NewVector();
};