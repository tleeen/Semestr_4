#include "../h/IUnknown.h"
#include "../h/Server.h"
#include "../h/ClassFactory.h"
#include <windows.h>
#include <fstream>
#include <iostream>
#include <vector>
#define NULL __null

using namespace std;

char module_name[MAX_PATH];

H_RESULT_ CreateInstance(CLS_ID_ clsid, I_ID_ iid, void** ppv)
{
    H_RESULT_ res = 1;
     IClassFactory_ *ICF = NULL;
    if(clsid == 1)
    {
        ClassFactory *CF = new ClassFactory();
        CF->QueryInterface(IID_ServerFactory_, (void**)&ICF);
        res = ICF->CreateInstance(iid, ppv);
    }
     else if (clsid == 2){
        NewClassFactory *CF = new NewClassFactory();
        CF->QueryInterface(IID_ServerFactory_, (void**)&ICF);
        res = ICF->CreateInstance(iid, ppv);
    }
    return res;
}

H_RESULT_ DLLGetClassObject(CLS_ID_ clsid, I_ID_ iid, void** ppv)
{
    H_RESULT_ res = 1;
    switch(clsid)
    {
        case 101:
        {
            ClassFactory *CF = new ClassFactory();
            res = CF->QueryInterface(iid, ppv);
        }
        case 102:
        {
            NewClassFactory* CF = new NewClassFactory();
            res = CF->QueryInterface(iid, ppv);
            break;
        }
    }
    return res;
}

H_RESULT_ DllRegisterServer()
{
    H_RESULT_ res = 0;
    fstream file;
    int pos;
    string line, num;
    vector<string> lines;
    file.open("C:\\Users\\79236\\Desktop\\Lab_4_c++\\reg.txt", ios::in);
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
    file.open("C:\\Users\\79236\\Desktop\\Lab_4_c++\\reg.txt", ios::in);
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
    return res;
}

H_RESULT_ DllUnregisterServer()
{
    H_RESULT_ res = 0;
    fstream file;
    int pos;
    string line, num;
    vector<string> lines;
    file.open("reg.txt", ios::in);
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

    file.open("reg.txt", ios::out);
    for(int i = 0; i<lines.size(); i++)
    {
        file << lines[i];
    }
    
    file.close();
    return res;
    }


H_RESULT_ DLLCanUnloadNow()
{
    H_RESULT_ res = 1;
    if (global::global_countReference == 0) res = 0;
    return res;
}

BOOL APIENTRY DllMain(HINSTANCE hinstDLL, DWORD fdwReason, LPVOID lpvReserved)
{
    GetModuleFileName(hinstDLL, module_name, sizeof module_name);
    return TRUE;
}

