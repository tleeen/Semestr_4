
g++ -c DLLPROG.cpp -o o/DLLPROG.o
g++ ./o/DLLPROG.o -o main.exe -lole32 -loleaut32 -luser32

pause