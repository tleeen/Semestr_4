#include "Inf.h"
#include "ManagerDLL.h"
using namespace std;


int main()
{
    HINSTANCE h;
    H_RESULT_ res;
    ClassFactory* factory;
    FunctionArg GetClassObject, CreateInstance;
    FunctionNotArg FreeUnusedLibraries;
    h = LoadLibrary("managerDll.dll");

    GetClassObject = (FunctionArg) GetProcAddress(h, "GetClassObject");
    FreeUnusedLibraries = (FunctionNotArg) GetProcAddress(h, "FreeUnusedLibraries");
    CreateInstance = (FunctionArg) GetProcAddress(h, "CreateInstance");
    
    res = GetClassObject(CLSIDServer_, IID_ServerFactory_, (void**)&factory);

    if (res == S_OK_)
    {
        Info* fIX = NULL;
        res = factory->CreateInstance(IID_IServer_, (void**)&fIX);
        if (res == S_OK_)
        {
            fIX->Enter();
            fIX->Print();
        }
        fIX->Release();
        factory->Release();
    }
    FreeUnusedLibraries();
    FreeLibrary(h);
}