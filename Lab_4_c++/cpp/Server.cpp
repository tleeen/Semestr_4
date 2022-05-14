#include <iostream>
#include "../h/Server.h"
#include "../h/IClassFactory.h"
#include <cmath>
using namespace std;

Vector::~Vector(){}

void Vector::Enter()
{
    cout << "Enter X" << endl;
    cin >> X;
    cout << "Enter Y" << endl;
    cin >> Y;
    cout << "Enter Z" << endl;
    cin >> Z;
}

void Vector::Print()
{
    cout << "Vector ("<< X << ","<<Y<<","<<Z<<")" << endl;
}

void Vector::GetLength()
{

    cout << "The length of the vector is " << sqrt(X * X + Y * Y + Z * Z) << endl;
}

void Vector::Add(double X1, double Y1, double Z1)
{
    cout << "The sum of the vectors is Vector ("<< X + X1 << ","<< Y + Y1 <<","<< Z + Z1 <<")" << endl;
}

void Vector::Diff(double X1, double Y1, double Z1)
{
    cout << "The vector difference is Vector ("<< X - X1 << ","<< Y - Y1 <<","<< Z - Z1 <<")" << endl;
}

void Vector::Mult(double X1, double Y1, double Z1)
{
     cout << "The product of vectors is " << X * X1 + Y * Y1 + Z * Z1 << endl;
}

U_LONG_ Vector::AddRef() 
{
    countReference++;

    global::global_countReference++;

    return countReference;
}

U_LONG_ Vector::Release() 
{
    countReference--;

    global::global_countReference--;

    if(countReference == 0)
    {
        delete this;
    }
    return countReference;
}

H_RESULT_ Vector::QueryInterface(I_ID_ iid, void** ppv)
{
    switch (iid)
    {
        case IID_IUnknown_:
        {
            *ppv = (I_Unknown_*) (Info*) this;
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
        default:
        {
            *ppv = NULL;
            return -1;
        }
    }
    AddRef();
    return S_OK_;
}