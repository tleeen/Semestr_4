#include "../h/Server.h"
#include "../h/ClassFactory.h"
#include <iostream>
#define NULL __null

namespace global{
    int global_countReferencen = 0;
}

ClassFactory::ClassFactory()
{
    countReferencen = 0;
}

ClassFactory::~ClassFactory(){}

HRESULT ClassFactory::QueryInterface(const IID& iid, void** ppv)
{
    if (iid == guid::IID_IUnknown || iid == guid::IID_IClassFactory)
    {
        *ppv = (IClassFactory*)this;
    } 
    else if (iid == IID_ServerFactory)
    {
        *ppv = (ClassFactory*)this;
    } else 
    {
        return E_NOINTERFACE;
    }
    AddRef();
    return S_OK;
}


HRESULT ClassFactory::CreateInstance(IUnknown* pUnknownOuter, const IID& iid, void** ppv)
{
    HRESULT res;
    Vector *VECTOR;
    *ppv = NULL;
    VECTOR = new Vector();
    if (VECTOR == 0)
    {
        return E_OUTOFMEMORY;
    }
    res = VECTOR->QueryInterface(iid, ppv);  
    if (FAILED(res))
    { 
        delete VECTOR;
    } 
    return res;
}

ULONG ClassFactory::AddRef() 
{
    countReferencen++;

     global::global_countReferencen++;
    
    return countReferencen;
}

ULONG ClassFactory::Release() 
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

HRESULT ClassFactory::LockServer(BOOL block){return S_OK;}