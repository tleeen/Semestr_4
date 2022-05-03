#include "IUnknown.h"
#include "IClassFactory.h"
#include "Server.h"
#include <iostream>
#pragma once

class Wrapper
{
	private:
      Info* fIX;
	  Operations* fIY;
	  IClassFactory_* factory;
	public:
	 Wrapper();
	 ~Wrapper();
	 Wrapper(Wrapper& sc);
	 Wrapper& operator=(Wrapper& sc);
	 void Enter();
	 void Print();
     void GetLength();
     void Add(double X1, double Y1, double Z1);
     void Diff(double X1, double Y1, double Z1);
     void Mult(double X1, double Y1, double Z1);
};
