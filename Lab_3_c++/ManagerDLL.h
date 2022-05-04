#include "Inf.h"
#pragma once

extern "C" H_RESULT_ __declspec(dllexport) GetClassObject(CLS_ID_ clsid, I_ID_ iid, void** ppv);
extern "C" H_RESULT_ __declspec(dllexport) CreateInstance();
extern "C" H_RESULT_ __declspec(dllexport) FreeUnusedLibraries();