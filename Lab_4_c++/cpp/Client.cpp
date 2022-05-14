#include <iostream>
#include "../h/Wrapper.h"

using namespace std;

int main()
{
    Wrapper* v = new Wrapper();
    v->Enter();
    v->Print();
    v->GetLength();
    v->Add(4, 4, 4);
    v->Diff(5, 5, 5);
    v->Mult(6, 6, 6);
    delete v;
    return 0;
}