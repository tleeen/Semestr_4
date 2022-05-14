#include "IUnknown.h"
#pragma once

using H_RESULT_ = int;
using I_ID_ = int;
using CLS_ID_ = int;
using U_LONG_ = int;

const I_ID_ IID_IUnknown_ = 0;
const I_ID_ IID_ServerFactory_ = 2;
const I_ID_ IID_IServer_ = 1;
const I_ID_ IID_IServer2_ = 2;
const I_ID_ IID_IServer3_ = 3;
const I_ID_ IID_IClassFactory_ = 1;
const I_ID_ IID_NewClassFactory_ = 3;
const H_RESULT_ S_OK_ = 0;
const H_RESULT_ E_NOINTERFACE_ = -1;
const H_RESULT_ E_OUTOFMEMORY_ = -2;
const H_RESULT_ E_CLASSNOTAVAILABLE_ = -3;
const CLS_ID_ CLSIDServer_ = 101;
const CLS_ID_ CLSIDNewServer_ = 102;

class IClassFactory_: public I_Unknown_
{
    public:
        virtual H_RESULT_ CreateInstance(I_ID_, void**) = 0; 
};
