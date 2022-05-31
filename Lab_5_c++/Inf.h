#include "h/ClassFactory.h"
#include "h/IClassFactory.h"
#include "h/IUnknown.h"
#include "h/Wrapper.h"
#include <windows.h>
#include <iostream>
#pragma once

typedef H_RESULT_ (*FunctionArg) (CLS_ID_, I_ID_, void**);
typedef H_RESULT_ (*FunctionNotArg) ();