#include "h/ClassFactory.h"
#include "h/MDLL.h"
#include <windows.h>
#include <iostream>
#pragma once

typedef HRESULT (*FunctionArg) (CLSID, IID, void**);
typedef HRESULT (*FunctionNotArg) ();