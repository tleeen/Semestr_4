#include <iostream>
#include "../h/Server.h"
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

ULONG Vector::AddRef() 
{
    countReferencen++;

    global::global_countReferencen++;

    return countReferencen;
}

ULONG Vector::Release() 
{
    countReferencen--;

    global::global_countReferencen--;

    if(countReferencen == 0)
    {
        delete this;
        return 0;
    }
    return countReferencen;
}

HRESULT Vector::QueryInterface(const IID& iid, void** ppv)
{
    if (iid == guid::IID_IUnknown)
    {
        *ppv = (IUnknown*)((Info*)this);
    } 
    else if (iid == IID_IServer)
    {
        *ppv = (Info*)this;
    } 
    else if (iid == IID_IServer2)
    {
        *ppv = (Operations*)this;
    } 
    else 
    {
        return E_NOINTERFACE;
    }
    AddRef();
    return S_OK;
}