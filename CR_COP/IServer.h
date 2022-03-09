#pragma once

using HRESULT_ = int;
using IID_ = int;
using CLSID_ = int;

class IUnknown_
{
    public:
        virtual HRESULT_ QueryInterface(IID_, void**) = 0;
};

class IX: public IUnknown_
{
    public:
        virtual void Fx(double, int) = 0;
};

class IY: public IUnknown_
{
    public:
        virtual void Fy(double, int) = 0;
};

HRESULT_ CreateInstance(CLSID_ clsid, IID_ iid, void** ppv);