#include "../h/NewServer.h"
#include "../h/ClassFactory.h"
#include "../h/IClassFactory.h"
#include <iostream>
#define NULL __null

NewClassFactory::NewClassFactory(){
    countReference = 0;
}

NewClassFactory::~NewClassFactory(){}

H_RESULT_ NewClassFactory::QueryInterface(I_ID_ iid, void** ppv)
{
    switch (iid)
    {
        case IID_IUnknown_:
        case IID_IClassFactory_:

            *ppv = (IClassFactory_*)this;
            break;
        case IID_NewClassFactory_:
            *ppv = (NewClassFactory*)this;
            break;
        default:
        {
            *ppv = NULL;
            return 1;
        }
    }
    AddRef();
    return S_OK_;
}

H_RESULT_ NewClassFactory::CreateInstance(I_ID_ iid, void** ppv)
{
    H_RESULT_ res = 1;
    NewVector* NEWVECTOR = new NewVector();
    res = NEWVECTOR->QueryInterface(iid, ppv);    
    return res;
}

U_LONG_ NewClassFactory::AddRef()
{
    countReference++;
    global::global_countReference++;
    return countReference;
}

U_LONG_ NewClassFactory::Release()
{
    countReference--;
    global::global_countReference--;
    if (countReference == 0)
    {
        delete this;
        return 0;
    }
    return countReference;
}