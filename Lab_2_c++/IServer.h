#include "IClassFactory.h"
#pragma once

class Info : public I_Unknown
{
public:
    virtual void Print() = 0;
    virtual void Enter() = 0;
};

class Operations : public I_Unknown
{
public:
    virtual void GetLength() = 0;
    virtual void Add(double X1, double Y1, double Z1) = 0;
    virtual void Diff(double X1, double Y1, double Z1) = 0;
    virtual void Mult(double X1, double Y1, double Z1) = 0;
};

class IServerFactory : public I_ClassFactory 
{
    public:
        IServerFactory() {};
        H_RESULT QueryInterface(I_ID iid, void** ppv);
        H_RESULT CreateInstance(I_ID iid, void** ppv);
};

H_RESULT GetClassObject(CLS_ID clsid, I_ID iid, void** ppv);
