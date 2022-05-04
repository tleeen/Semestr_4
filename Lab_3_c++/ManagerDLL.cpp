#include "Inf.h"
#include "ManagerDLL.h"
#include <vector>
#include <windows.h>
#include <fstream>
using namespace std;

vector<HINSTANCE> libs(1);

H_RESULT_  GetClassObject(CLS_ID_ clsid, I_ID_ iid, void** ppv)
{
    H_RESULT_ res = 1;
    HINSTANCE h;
    FunctionArg DLLGetClassObject;
    bool Find = false;
    fstream file;
    string line, num;
    const char *path;
    int pos;

    file.open("a.txt", ios::in);
    while(getline(file, line))
    {
        pos = line.find(":");
        num = line.substr(0, pos);
        if (stoi(num) == clsid)
        {
            line = line.substr(pos + 1, line.length());
            path = line.c_str();
            Find = true;
            break;
        } 
    }
    file.close();
    if (Find)
    {
        h = LoadLibrary(path);
        if (h)
        {
            DLLGetClassObject = (FunctionArg) GetProcAddress(h, "DLLGetClassObject");
            libs.push_back(h);
            if (DLLGetClassObject)
            {
                res = DLLGetClassObject(clsid, iid, ppv);
            }
        }
    }
    return res;
}

H_RESULT_ CreateInstance(CLS_ID_ clsid, I_ID_ iid, void** ppv)
{
    H_RESULT_ res = 0;
    IClassFactory_* factory;
    res = GetClassObject(clsid, IID_IClassFactory_, (void**)&factory);
    factory->CreateInstance(iid, ppv);
    return res;
}

H_RESULT_ FreeUnusedLibraries()
{
    H_RESULT_ res = 1;
    FunctionNotArg DllCanUnloadNow;
    for (int i = 0; i < libs.size(); i++)
    {
        DllCanUnloadNow = (FunctionNotArg) GetProcAddress(libs[i], "DLLCanUnloadNow");
        if (DllCanUnloadNow)
        {
            res = DllCanUnloadNow();
            if (res == S_OK_)
            {
                FreeLibrary(libs[i]);
                libs.erase(libs.begin() + i);
                libs.resize(libs.size() - 1);
            }
        }
    }
    return res;
}