@REM pause
@REM exit

g++ -c cpp/MDLL.cpp -o o/MDLL.o
g++ -c cpp/Server.cpp -o o/Server.o
g++ -c cpp/ClassFactory.cpp -o o/ClassFactory.o
g++ -c cpp/NewServer.cpp -o o/NewServer.o
g++ -c cpp/NewClassFactory.cpp -o o/NewClassFactory.o
g++ -c managerDll.cpp -o o/managerDll.o

g++ -shared ./o/Server.o ./o/MDLL.o ./o/ClassFactory.o ./o/NewServer.o ./o/NewClassFactory.o -o Server.dll -lole32 -loleaut32 -luser32 -Wl,--kill-at
g++ -shared ./o/managerDll.o -o managerDll.dll -Wl,--kill-at

@REM pause
@REM exit

pause