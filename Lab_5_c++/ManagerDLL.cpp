#include "Inf.h"
#include "ManagerDLL.h"
#include <vector>
#include <windows.h>
#include <fstream>
using namespace std;

vector<HINSTANCE> libs(1);

HRESULT GetClassObject(const CLSID& clsid, const IID& iid, void** ppv)
{
    HRESULT res;
    HINSTANCE h;
    FunctionArg DLLGetClassObject;
    bool Find = false;
    fstream file;
    string line, num;
    const char *path;
    int pos;

    file.open("C:\\Users\\79236\\Desktop\\Lab_5_c++\\a.txt", ios::in);
    while(getline(file, line))
    {
        pos = line.find(":");
        num = line.substr(0, pos);
        if (stoi(num) == 2)
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
            DLLGetClassObject = (FunctionArg) GetProcAddress(h, "DllGetClassObject");
            libs.push_back(h);
            if (DLLGetClassObject)
            {
                res = DLLGetClassObject(clsid, iid, ppv);
            }
        }
    }
    return res;
}

HRESULT CreateInstance(const CLSID& clsid, const IID& iid, void** ppv){
    HRESULT res;
    IClassFactory* factory;
    res = GetClassObject(clsid, guid::IID_IClassFactory, (void**)&factory);
    factory->CreateInstance(NULL, iid, ppv);
    return res;
}



HRESULT FreeUnusedLibraries()
{
    HRESULT res;
    FunctionNotArg DllCanUnloadNow;
    for (int i = 0; i < libs.size(); i++)
    {
        DllCanUnloadNow = (FunctionNotArg) GetProcAddress(libs[i], "DLLCanUnloadNow");
        if (DllCanUnloadNow)
        {
            res = DllCanUnloadNow();
            if (res == SUCCEEDED(res))
            {
                FreeLibrary(libs[i]);
                libs.erase(libs.begin() + i);
                libs.resize(libs.size() - 1);
            }
        }
    }
    return res;
}