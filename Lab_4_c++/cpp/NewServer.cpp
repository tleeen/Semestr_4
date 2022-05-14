#include "../h/NewServer.h"
#include "../h/IClassFactory.h"
#include <iostream>
#include <fstream>
#include <cmath>
using namespace std;

NewVector::~NewVector(){}

void NewVector::Sin(double X1, double Y1, double Z1)
{
    cout << "The sin of the angle between the vectors is " << (sqrt((Y * Z1 - Z * Y1) * (Y * Z1 - Z * Y1) + (X * Z1 - Z * X1) * (X * Z1 - Z * X1) + (X * Y1 - Y * X1) * (X * Y1 - Y * X1))) / (sqrt(X * X + Y * Y + Z * Z) * sqrt(X1 * X1 + Y1 * Y1 + Z1 * Z1)) << endl;
}

void NewVector::Cos(double X1, double Y1, double Z1)
{
    cout << "The sin of the angle between the vectors is " << (X * X1 + Y * Y1 + Z * Z1) / (sqrt(X * X + Y * Y + Z * Z) * sqrt(X1 * X1 + Y1 * Y1 + Z1 * Z1)) << endl;
}

void NewVector::Colinarity(double X1, double Y1, double Z1)
{
    if (Y * Z1 - Z * Y1 == 0 && X * Z1 - Z * X1 == 0 && X * Y1 - Y * X1 == 0)
    {
        cout << "Vectors are collinear" <<endl;
    }
    else
    {
        cout << "Vectors are not callinear" <<endl;
    }
}

void NewVector::Angle(double X1, double Y1, double Z1)
{
    cout << "The angle between the vectors is " <<  acos((X * X1 + Y * Y1 + Z * Z1) / (sqrt(X * X + Y * Y + Z * Z) * sqrt(X1 * X1 + Y1 * Y1 + Z1 * Z1))) << endl;
}

void NewVector::Enter()
{
    Vector_old->Enter();
}

void NewVector::Print()
{
    Vector_old->Print();
}

void NewVector::GetLength()
{
    Vector_old->GetLength();
}

void NewVector::Add(double X1, double Y1, double Z1)
{
    Vector_old->Add(X1, Y1, Z1);
}

void NewVector::Diff(double X1, double Y1, double Z1)
{
    Vector_old->Diff(X1, Y1, Z1);
}

void NewVector::Mult(double X1, double Y1, double Z1)
{
    Vector_old->Diff(X1, Y1, Z1);
}

H_RESULT_ NewVector::QueryInterface(I_ID_ iid, void** ppv)
{
    switch (iid)
    {
        case IID_IUnknown_:
        {
            *ppv = (I_Unknown_*) (NewFunction*) this;
            break;
        }
        case IID_IServer_:
        {
            *ppv = (Info*) this;
            break;
        }
        case IID_IServer2_:
        {
            *ppv = (Operations*) this;
            break;
        }
        case IID_IServer3_:
        {
            *ppv = (NewFunction*) this;
            break;
        }
        default:
        {
            *ppv = NULL;
            return -1;
        }
    }
    AddRef();
    return S_OK_;
}

U_LONG_ NewVector::AddRef()
{
    countReference++;
    Vector_old->AddRef();
    global::global_countReference++;
    return countReference;
}

U_LONG_ NewVector::Release()
{
    countReference--;
    Vector_old->Release();
    global::global_countReference--;
    if (countReference == 0)
    {
        delete this;
        return 0;
    }
    return countReference;
}