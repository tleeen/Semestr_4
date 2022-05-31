#include "MDLL.h"
#pragma once

class ClassFactory:public IClassFactory
{
    private:
        int countReferencen;
    public:
        ClassFactory();
        virtual ~ClassFactory();
        HRESULT __stdcall QueryInterface(const IID& iid, void** ppv);
        virtual ULONG __stdcall AddRef();
        virtual ULONG  __stdcall Release();
        virtual HRESULT __stdcall CreateInstance(IUnknown* pUnknownOuter, const IID& iid, void** ppv);
        virtual HRESULT __stdcall LockServer(BOOL block);
};

class NewClassFactory: public IClassFactory{
    private:
        int countReferencen;
    public:
        NewClassFactory();
        virtual ~NewClassFactory();
        HRESULT __stdcall QueryInterface(const IID& iid, void** ppv);
        virtual ULONG __stdcall AddRef();
        virtual ULONG __stdcall Release();
        virtual HRESULT __stdcall CreateInstance(IUnknown* pUnknownOuter, const IID& iid, void** ppv);
        virtual HRESULT __stdcall LockServer(BOOL block);
};