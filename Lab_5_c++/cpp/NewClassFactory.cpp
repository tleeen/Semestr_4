#include "../h/NewServer.h"
#include "../h/ClassFactory.h"
#include <iostream>
#define NULL __null

NewClassFactory::NewClassFactory(){
    countReferencen = 0;
}

NewClassFactory::~NewClassFactory(){}

HRESULT NewClassFactory::QueryInterface(const IID& iid, void** ppv)
{
    if (iid == guid::IID_IUnknown || iid == guid::IID_IClassFactory)
    {
        *ppv = (IClassFactory*)this;
    } 
    else if (iid == IID_NewClassFactory)
    {
        *ppv = (NewClassFactory*)this;
    } 
    else {
        return E_NOINTERFACE;
    }
    AddRef();
    return S_OK;
}

HRESULT NewClassFactory::CreateInstance(IUnknown* pUnknownOuter, const IID& iid, void** ppv)
{
    HRESULT res;

    NewVector* NEWVECTOR;

    *ppv = NULL;
    NEWVECTOR = new NewVector();

    if (NEWVECTOR == 0)
    {
        return (E_OUTOFMEMORY);
    }

    res = NEWVECTOR->QueryInterface(iid, ppv);   
    
    if (FAILED(res))
    {
        delete NEWVECTOR;
    }
    return res;
}

ULONG NewClassFactory::AddRef()
{
    countReferencen++;
    global::global_countReferencen++;
    return countReferencen;
}

ULONG NewClassFactory::Release()
{
    countReferencen--;
    global::global_countReferencen--;
    if (countReferencen == 0)
    {
        delete this;
        return 0;
    }
    return countReferencen;
}

HRESULT NewClassFactory::LockServer(BOOL block){return S_OK;}