#include <iostream>
#include "Server.h"
using namespace std;

Server1::Server1() 
{
    a = 1234;
}

HRESULT_ Server1::QueryInterface(IID_ iid, void** ppv)
{
    if (iid == 0)
    {
        *ppv = (IUnknown_*)((IX*)this);
        return 0;
    }
    else if (iid == 1)
    {
        *ppv = (IX*)this;
        return 0;
    }
    else 
    {
        *ppv = NULL;
        return 1;
    }
}

void Server1::Fx(double c, int a) 
{
    cout << "Server1 Fx" << endl;
}


Server2::Server2()
{
    a = 4321;
}

HRESULT_ Server2::QueryInterface(IID_ iid, void** ppv)
{
    if (iid == 0)
    {
        *ppv = (IUnknown_*)((IY*)this);
        return 0;
    }
    else if (iid == 1)
    {
        *ppv = (IX*)this;
        return 0;
    }
    else if (iid == 2)
    {
        *ppv = (IY*)this;
        return 0;
    }
    else 
    {
        *ppv = NULL;
        return 1;
    }
}

void Server2::Fx(double c, int a)
{
    cout << "Server2 Fx" << endl;
}

void Server2::Fy(double c, int a)
{
    cout << "Server2 Fy" << endl;
}