#include "Inf.h"
#include "ManagerDLL.h"
using namespace std;


int main()
{
    HINSTANCE h;
    HRESULT res;
    NewClassFactory* factory;
    FunctionArg GetClassObject, CreateInstance;
    FunctionNotArg FreeUnusedLibraries;
    h = LoadLibrary("managerDll.dll");

    GetClassObject = (FunctionArg) GetProcAddress(h, "GetClassObject");
    FreeUnusedLibraries = (FunctionNotArg) GetProcAddress(h, "FreeUnusedLibraries");
    CreateInstance = (FunctionArg) GetProcAddress(h, "CreateInstance");
    
    res = GetClassObject(CLSID_NewServer, IID_NewClassFactory, (void**)&factory);

    if (res == S_OK)
    {
        Info* fIX = NULL;
        res = factory->CreateInstance(NULL, IID_IServer, (void**)&fIX);
        {
            fIX->Enter();
            fIX->Print();
        }
        NewFunction* fIZ = NULL;
        res = fIX->QueryInterface(IID_IServer3, (void**)&fIZ);
        if (res == S_OK)
        {
            fIZ->Sin(3, 3, 3);
            fIZ->Cos(4, 4, 4);
            fIZ->Colinarity(5, 5, 5);
            fIZ->Angle(6, 6, 6);
        }
        fIX->Release();
        fIZ->Release();
        factory->Release();
    }
    FreeUnusedLibraries();
    FreeLibrary(h);
}