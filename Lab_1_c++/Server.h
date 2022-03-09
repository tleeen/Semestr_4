#include "IServer.h"
#pragma once

class Server1: public IX
{
protected:
    int a;

public:
    Server1();
    HRESULT_ virtual QueryInterface(IID_, void**);
    virtual void Fx(double, int);
};

class Server2: public IX, IY
{
    protected:
        int a;
    public:
        Server2();
        HRESULT_ virtual QueryInterface(IID_, void**);
        virtual void Fx(double, int);
        virtual void Fy(double, int);
};