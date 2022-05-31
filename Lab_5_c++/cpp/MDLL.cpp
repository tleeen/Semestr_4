#include "../h/MDLL.h"
#include "../h/Server.h"
#include "../h/ClassFactory.h"
#include <windows.h>
#include <fstream>
#include <iostream>
#include <vector>
#define NULL __null

using namespace std;

char module_name[MAX_PATH];

HRESULT CreateInstance(const CLSID& clsid, const IID& iid, void** ppv)
{
    HRESULT res;

    IClassFactory *ICF = NULL;

    if(clsid == CLSID_Server)
    {
        ClassFactory *CF = new ClassFactory();
        CF->QueryInterface(IID_ServerFactory, (void**)&ICF);
        res = ICF->CreateInstance(NULL, iid, ppv);
    }
    else if (clsid == CLSID_NewServer)
    {
        NewClassFactory *CF = new NewClassFactory();
        CF->QueryInterface(IID_NewClassFactory, (void**)&ICF);
        res = ICF->CreateInstance(NULL, iid, ppv);
    }
    return res;
}

HRESULT DllGetClassObject(const CLSID& clsid, const IID& iid, void** ppv)
{
    HRESULT res;
    if (clsid == CLSID_Server)
    {
        ClassFactory *CF = new ClassFactory();
        res = CF->QueryInterface(iid, ppv);
    } 
    else if (clsid == CLSID_NewServer) 
    {
        NewClassFactory* CF = new NewClassFactory();
            res = CF->QueryInterface(iid, ppv);
    }
    return res;
}

HRESULT DllRegisterServer()
{
    fstream file;
    int pos;
    string line, num;
    vector<string> lines;
    file.open("C:\\Users\\79236\\Desktop\\Lab_5_c++\\reg.txt", ios::in);
    while(!file.eof())
    {
        if (getline(file, line))
        {
            lines.push_back(line);
        }
    }
    file.close();
    for(int i = 0; i<lines.size(); i++)
    {
        pos = lines[i].find(":");
        num = line.substr(0, pos);
        if (stoi(num) == 1 || stoi(num) == 2)
        {
            lines[i] = num + ":" + (string)module_name + "\n";
        } 
    }
    file.open("C:\\Users\\79236\\Desktop\\Lab_5_c++\\reg.txt", ios::in);
    if (lines.empty())
    {
        file << "1:" + (string)module_name + "\n";
        file << "2:" + (string)module_name;
    } 
    else
    {
        for(int i = 0; i<lines.size(); i++)
        {
            file << lines[i];
        }
    }
    file.close();
    return S_OK;
}

HRESULT DllUnregisterServer()
{
    fstream file;
    int pos;
    string line, num;
    vector<string> lines;
    file.open("C:\\Users\\79236\\Desktop\\Lab_5_c++\\reg.txt", ios::in);
    while(!file.eof())
    {
        getline(file, line);
        lines.push_back(line);
    }
    file.close();
    for(int i = 0; i<lines.size(); i++)
    {
        pos = lines[i].find(":");
        if (pos > -1)
        {
            num = line.substr(0, pos);
            if (stoi(num) == 1 or stoi(num) == 2)
            {
                lines[i].erase();
                lines.resize(lines.size() - 1);
                break;
            } 
        }
    }

    file.open("C:\\Users\\79236\\Desktop\\Lab_5_c++\\reg.txt", ios::out);
    for(int i = 0; i<lines.size(); i++)
    {
        file << lines[i];
    }
    
    file.close();
    return S_OK;
    }


HRESULT DllCanUnloadNow(){
    return (global::global_countReferencen == 0) ?  S_OK : S_FALSE;
}

BOOL APIENTRY DllMain(HINSTANCE hinstDLL, DWORD fdwReason, LPVOID lpvReserved)
{
    GetModuleFileName(hinstDLL, module_name, sizeof module_name);
    return TRUE;
}

