@REM pause
@REM exit

g++ -c cpp/Server.cpp -o o/Server.o
g++ -c cpp/IServer.cpp -o o/IServer.o
g++ -c cpp/ClassFactory.cpp -o o/ClassFactory.o
g++ -c managerDll.cpp -o o/managerDll.o

g++ -shared ./o/Server.o ./o/IServer.o ./o/ClassFactory.o -o Server.dll -Wl,--kill-at
g++ -shared ./o/managerDll.o -o managerDll.dll -Wl,--kill-at

@REM pause
@REM exit

pause