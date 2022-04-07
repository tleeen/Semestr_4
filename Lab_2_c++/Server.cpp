#include <iostream>
#include "IServer.h"
#include "Server.h"
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

U_LONG Vector::AddRef() 
{
    countReference++;
    return countReference;
}

U_LONG Vector::Release() 
{
    countReference--;
    if(countReference == 0)
    {
        delete this;
    }
    return countReference;
}

H_RESULT Vector::QueryInterface(I_ID iid, void** ppv)
{
    switch (iid)
    {
        case IID_IUnknown:
        {
            *ppv = (I_Unknown*) (Info*) this;
            break;
        }
        case IID_IServer:
        {
            *ppv = (Info*) this;
            break;
        }
        case IID_IServer2:
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
    return S_OK;
}

H_RESULT IServerFactory::CreateInstance(I_ID iid, void** ppv)
{
    Vector* vector = new Vector();
    if (vector == 0)
    {
        return E_OUTOFMEMORY;
    }
    H_RESULT res = vector->QueryInterface(iid, ppv);
    return res;
}

H_RESULT IServerFactory::QueryInterface(I_ID iid, void** ppv)
{
    if (iid == IID_IUnknown || iid == IID_IClassFactory)
    {
        *ppv = (I_ClassFactory*) this;
    }
    else
    {
        *ppv = 0;
        return E_NOINTERFACE;
    }
    AddRef();
    return S_OK;
}

H_RESULT GetClassObject(CLS_ID clsid, I_ID iid, void** ppv)
{
    if(clsid != CLSIDServer)
    {
        return E_CLASSNOTAVAILABLE;
    }
    IServerFactory* factory = new IServerFactory();
    if(factory == 0) 
    {
        return E_OUTOFMEMORY;
    }
    H_RESULT res = factory->QueryInterface(iid, ppv);
    return res;
}