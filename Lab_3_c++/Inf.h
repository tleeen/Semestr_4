#include "ClassFactory.h"
#include "IClassFactory.h"
#include "IUnknown.h"
#include "Wrapper.h"
#include <windows.h>
#include <iostream>
#pragma once

typedef H_RESULT_ (*FunctionArg) (CLS_ID_, I_ID_, void**);
typedef H_RESULT_ (*FunctionNotArg) ();