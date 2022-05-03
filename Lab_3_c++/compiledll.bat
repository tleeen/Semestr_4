@REM pause
@REM exit

g++ -c Server.cpp -o Server.o
g++ -c IServer.cpp -o IServer.o
g++ -c ClassFactory.cpp -o ClassFactory.o
g++ -c managerDll.cpp -o managerDll.o

g++ -shared Server.o IServer.o ClassFactory.o -o Server.dll -Wl,--kill-at
g++ -shared managerDll.o -o managerDll.dll -Wl,--kill-at

@REM pause
@REM exit

pause