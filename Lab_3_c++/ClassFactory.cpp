#include "Server.h"
#include "ClassFactory.h"
#include <iostream>
#define NULL __null

namespace global{
    int global_countReference = 0;
}

ClassFactory::ClassFactory()
{
    countReference = 0;
}

ClassFactory::~ClassFactory(){}

H_RESULT_ ClassFactory::QueryInterface(I_ID_ iid, void** ppv)
{
    switch (iid)
    {
        case IID_IUnknown_:
        case IID_IClassFactory_:

            *ppv = (IClassFactory_*)this;
            break;
        case IID_ServerFactory_:
            *ppv = (ClassFactory*)this;
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

H_RESULT_ ClassFactory::CreateInstance(I_ID_ iid, void** ppv)
{
    Vector* VECTOR = new Vector();
    switch(iid){
        case 1:
        case 2:
            VECTOR->QueryInterface(iid, ppv);
            break;
        default:
        {
            *ppv = NULL;
            return 1;
        }
    }
    return 0;
}

U_LONG_ ClassFactory::AddRef() 
{
    countReference++;

     global::global_countReference++;
    
    return countReference;
}

U_LONG_ ClassFactory::Release() 
{
    countReference--;

    global::global_countReference--;

    if(countReference == 0)
    {
        delete this;
    }

    return countReference;
}