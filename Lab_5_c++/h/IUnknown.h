#pragma once

using H_RESULT_ = int;
using I_ID_ = int;
using CLS_ID_ = int;
using U_LONG_ = int;

namespace global
{
    extern int global_countReference;
}

class I_Unknown_
{
    public:
        virtual H_RESULT_ QueryInterface(I_ID_, void**) = 0;
        virtual U_LONG_ AddRef() = 0;
        virtual U_LONG_ Release() = 0;
};

class Info : public I_Unknown_
{
public:
    virtual void Print() = 0;
    virtual void Enter() = 0;
};

class Operations : public I_Unknown_
{
public:
    virtual void GetLength() = 0;
    virtual void Add(double X1, double Y1, double Z1) = 0;
    virtual void Diff(double X1, double Y1, double Z1) = 0;
    virtual void Mult(double X1, double Y1, double Z1) = 0;
};

class NewFunction: public I_Unknown_
{
    public:
        virtual void Sin(double X1, double Y1, double Z1 ) = 0;
        virtual void Cos(double X1, double Y1, double Z1) = 0;
        virtual void Colinarity(double X1, double Y1, double Z1) = 0;
        virtual void Angle(double X1, double Y1, double Z1) = 0; 
};

H_RESULT_ CreateInstance(CLS_ID_ clsid, I_ID_ iid, void** ppv);
extern "C" H_RESULT_ __declspec(dllexport) DLLGetClassObject(CLS_ID_ clsid, I_ID_ iid, void** ppv);
extern "C" H_RESULT_ __declspec(dllexport) DllRegisterServer();
extern "C" H_RESULT_ __declspec(dllexport) DllUnregisterServer();
extern "C" H_RESULT_ __declspec(dllexport) DLLCanUnloadNow();
