#include "IClassFactory.h"
#pragma once

class ClassFactory:public IClassFactory_
{
    private:
        int countReference;
    public:
        ClassFactory();
        ~ClassFactory();
        H_RESULT_ QueryInterface(I_ID_ iid, void** ppv);
        U_LONG_ virtual AddRef();
        U_LONG_ virtual Release();
        virtual H_RESULT_ CreateInstance(I_ID_ iid, void** ppv);
};

class NewClassFactory: public IClassFactory_{
    private:
        int countReference;
    public:
        NewClassFactory();
        ~NewClassFactory();
        H_RESULT_ QueryInterface(I_ID_ iid, void** ppv);
        U_LONG_ virtual AddRef();
        U_LONG_ virtual Release();
        virtual H_RESULT_ CreateInstance(I_ID_ iid, void** ppv);
};