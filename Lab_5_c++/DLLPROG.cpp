#include "Inf.h"
#include "ManagerDLL.h"
using namespace std;


int main()
{
    CoInitialize(NULL);
    Info* inf = NULL;
    IClassFactory* factory = NULL;
    HRESULT resFactory;
    resFactory = CoGetClassObject(CLSID_Server, CLSCTX_INPROC_SERVER, NULL, guid::IID_IClassFactory, (void**)&factory);
    if (SUCCEEDED(resFactory))
    {
        HRESULT res;
        Info* inf = NULL;
        res = factory->CreateInstance(NULL, IID_IServer, (void**)&inf);
        if (SUCCEEDED(res)){
            inf->Enter();
            inf->Print();
        }
        Operations* op = NULL;
        res = inf->QueryInterface(IID_IServer2, (void**)&op);
        if (SUCCEEDED(res))
        {
            op->GetLength();
            op->Diff(5, 5, 5);
            op->Mult(5, 5, 5);
            op->Add(5, 5, 5);
        }
        NewFunction* nf = NULL;
        res = op->QueryInterface(IID_IServer3, (void**)&nf);
        if (SUCCEEDED(res))
        {
            nf->Angle(5, 5, 5);
            nf->Colinarity(5, 5, 5);
            nf->Cos(5, 5, 5);
            nf->Sin(5, 5, 5);
        }
        inf->Release();
        op->Release();
        nf->Release();

        factory->Release();
    }
    else
    {
        cout << "1111";
    }

    CoUninitialize();
}