#pragma once

using H_RESULT = int;
using I_ID = int;
using CLS_ID = int;
using U_LONG = int;

const I_ID IID_IUnknown = 0;
const I_ID IID_IServer = 1;
const I_ID IID_IServer2 = 2;
const I_ID IID_IClassFactory = 2;
const H_RESULT S_OK = 0;
const H_RESULT E_NOINTERFACE = -1;
const H_RESULT E_OUTOFMEMORY = -2;
const H_RESULT E_CLASSNOTAVAILABLE = -3;
const CLS_ID CLSIDServer = 101;

class I_Unknown 
{
    public:
        virtual H_RESULT QueryInterface(I_ID iid, void** ppv) = 0;
        virtual U_LONG AddRef() = 0;
        virtual U_LONG Release() = 0;
};

class I_ClassFactory : public I_Unknown
{
    private:
        int countReference = 0;
    public:
        virtual H_RESULT CreateInstance(I_ID iid, void** ppv) = 0;
        U_LONG AddRef();
        U_LONG Release();
};
