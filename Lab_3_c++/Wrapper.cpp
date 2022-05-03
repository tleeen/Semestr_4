#include "Wrapper.h"
#include <iostream>

using namespace std;

Wrapper::Wrapper()
{
	H_RESULT_ res;

	this->factory = NULL;
    res = DLLGetClassObject(CLSIDServer_, IID_IClassFactory_, (void**)&this->factory);
    if (res == S_OK_)
    {
        this->fIX = NULL;
        this->factory->CreateInstance(IID_IServer_, (void**)&this->fIX);
        this->fIY = NULL;
        this->fIX->QueryInterface(IID_IServer2_, (void**)&this->fIY);
    }
}

Wrapper::Wrapper(Wrapper& sc)
{
    this->factory = sc.factory;
    this->fIX = sc.fIX;
    this->fIY = sc.fIY;
    this->factory->AddRef();
    this->fIX->AddRef();
    this->fIY->AddRef();
}

Wrapper& Wrapper::operator=(Wrapper& sc)
{
        this->factory = sc.factory;
     	this->fIX = sc.fIX;
    	this->fIY = sc.fIY;
        this->fIX->AddRef();
        this->factory->AddRef();
        this->fIY->AddRef();
        return *this;
}



Wrapper::~Wrapper()
{
   this->factory->Release();
   this->fIX->Release();
   this->fIY->Release();
}

void Wrapper::Enter()
{
	this->fIX->Enter();
}
void Wrapper::Print()
{
	this->fIX->Print();
}
void Wrapper::GetLength()
{
	this->fIY->GetLength();
}
void Wrapper::Add(double X1, double Y1, double Z1)
{
	this->fIY->Add(X1, Y1, Z1);
}
void Wrapper::Diff(double X1, double Y1, double Z1)
{
	this->fIY->Diff(X1, Y1, Z1);
}
void Wrapper::Mult(double X1, double Y1, double Z1)
{
	this->fIY->Mult(X1, Y1, Z1);
}



