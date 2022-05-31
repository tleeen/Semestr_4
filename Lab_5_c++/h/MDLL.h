#include <vector>
#include <string>
#include <windows.h>
using namespace std;
#pragma once

namespace global
{
    extern int global_countReferencen;
}

namespace guid
{
    const IID IID_IUnknown = {0x0181045a, 0x17bf, 0x406a, {0xa4, 0x60, 0x4a, 0xa3, 0x62, 0xc9, 0x97, 0xaf}};
    const IID IID_IClassFactory = {0x7ce81ca4, 0xbb42, 0x4634, {0xa8, 0xc4, 0x81, 0xf8, 0x45, 0xb6, 0x23, 0xdf}};
}

    const CLSID CLSID_Server = {0x12AEBEBB, 0xA929, 0x4B31, {0xA4, 0xD9, 0xA3, 0x6B, 0xB7, 0x33, 0x82, 0x8F}};
    const CLSID CLSID_NewServer = {0xFCF54AD5, 0xAAB2, 0x465B, {0xB5, 0x06, 0x31, 0x82, 0x63, 0xBE, 0xF7, 0x8D}};
    const IID IID_IServer = {0x25b72fdd, 0xeb0f, 0x4c8f, {0x8c, 0x75, 0xca, 0xf7, 0x58, 0xd2, 0x81, 0xd9}};
    const IID IID_IServer2 = {0xd4bebb6c, 0x763f, 0x4331, {0x85, 0xae, 0xbb, 0x3b, 0x24, 0xf0, 0x97, 0x7c}};
    const IID IID_IServer3 = {0x106f3b84, 0x80db, 0x4973, {0x9d, 0x55, 0x2f, 0x0f, 0x43, 0x46, 0x2c, 0x3a}};
    const IID IID_ServerFactory = {0xfeff8e4e, 0x52ce, 0x4255, {0x83, 0xdd, 0x93, 0x58, 0x6d, 0x95, 0xb8, 0xe0}};
    const IID IID_NewClassFactory = {0xb1c44c4e, 0x7a19, 0x4245, {0xbb, 0xe4, 0xa4, 0xbd, 0x6c, 0xfb, 0xb5, 0x4a}};

class Info : public IUnknown
{
public:
    virtual void __stdcall Print() = 0;
    virtual void __stdcall Enter() = 0;
};

class Operations : public IUnknown
{
public:
    virtual void __stdcall GetLength() = 0;
    virtual void __stdcall Add(double X1, double Y1, double Z1) = 0;
    virtual void __stdcall Diff(double X1, double Y1, double Z1) = 0;
    virtual void __stdcall Mult(double X1, double Y1, double Z1) = 0;
};

class NewFunction: public IUnknown
{
    public:
        virtual void __stdcall Sin(double X1, double Y1, double Z1 ) = 0;
        virtual void __stdcall Cos(double X1, double Y1, double Z1) = 0;
        virtual void __stdcall Colinarity(double X1, double Y1, double Z1) = 0;
        virtual void __stdcall Angle(double X1, double Y1, double Z1) = 0; 
};

HRESULT CreateInstance(const CLSID& clsid, const IID& iid, void** ppv);
extern "C" __declspec(dllexport) HRESULT __stdcall  DllGetClassObject(const CLSID& clsid, const IID& iid, void** ppv);
extern "C" __declspec(dllexport) HRESULT __stdcall DllRegisterServer();
extern "C" __declspec(dllexport) HRESULT __stdcall DllUnregisterServer();
extern "C" __declspec(dllexport) HRESULT __stdcall DllCanUnloadNow();