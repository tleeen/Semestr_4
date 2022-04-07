#include "IServer.h"

class Wrapper
{
	private:
      Info* fIX;
	  Operations* fIY;
	  I_ClassFactory* factory;
	  Wrapper(Wrapper& sc);
	  Wrapper& operator=(Wrapper& sc);
	public:
	 Wrapper();
	 ~Wrapper();
	 void Enter();
	 void Print();
     void GetLength();
     void Add(double X1, double Y1, double Z1);
     void Diff(double X1, double Y1, double Z1);
     void Mult(double X1, double Y1, double Z1);
};
