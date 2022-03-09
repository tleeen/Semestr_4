#include <iostream>
#include "IServer.h"
using namespace std;

int main()
{
    HRESULT_ res;
    CLSID_ CLSID_Server = 2;
    IID_ IID_Interface = 1;
    IUnknown_ *pIUnknown = nullptr;

    if(!CreateInstance(CLSID_Server, IID_Interface, (void**)&pIUnknown))
    {
        IY *py = NULL;
        res = pIUnknown->QueryInterface(2, (void**)&py);
        if (res == 0)
        {
            py->Fy(1, 1);
        }
        else
        {
            cout << "This interface is not available" << endl;
        }
    }
    else
    {
        cout << "Error in CreateInstance function" << endl;
    }

     CLSID_Server = 1;
     IID_Interface = 1;

    if(!CreateInstance(CLSID_Server, IID_Interface, (void**)&pIUnknown))
    {
        IX *py = NULL;
        res = pIUnknown->QueryInterface(1, (void**)&py);
        if (res == 0)
        {
            py->Fx(1, 1);
        }
        else
        {
            cout << "This interface is not available" << endl;
        }
    }
    else
    {
        cout << "Error in CreateInstance function" << endl;
    }

    return 0;
}