g++ -c IClassFactory.cpp
g++ -c Server.cpp
g++ -c Client.cpp
g++ -c Wrapper.cpp
g++ Client.o Server.o IClassFactory.o Wrapper.o -o run.exe

pause