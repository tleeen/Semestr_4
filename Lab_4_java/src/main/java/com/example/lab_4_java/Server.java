package com.example.lab_4_java;

import java.io.DataInputStream;
import java.io.DataOutputStream;
import java.io.IOException;
import java.net.ServerSocket;
import java.net.Socket;

public class Server {
    public static void main(String[] args) {
        try {
            ss = new ServerSocket(1111);
            while (true) {
                System.out.println("Ожидание подключения...");
                Socket clientSocket = ss.accept();
                new MyThread(clientSocket).start();
            }
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
    static ServerSocket ss = null;
}

class MyThread extends Thread {
    private final Socket clientSocket;
    public MyThread(Socket clientSocket) {
        this.clientSocket = clientSocket;
    }

    @Override
    public void run() {
        try {
            Socket localSocket = clientSocket;
            System.out.println("Local port: " + localSocket.getLocalPort());
            System.out.println("Remote port: " + localSocket.getPort());
            DataInputStream in = new DataInputStream(localSocket.getInputStream());
            DataOutputStream out = new DataOutputStream(localSocket.getOutputStream());
            while (true) {
                String a = in.readUTF();
                String c = in.readUTF();
                String b = in.readUTF();
                System.out.println("Первое число : " + a);
                System.out.println("Арифмитическое действие : " + c);
                System.out.println("Второе число : " + b);

                Double first = Double.valueOf(a);
                Double second = Double.valueOf(b);
                double res = switch (c) {
                    case "+" -> first + second;
                    case "-" -> first - second;
                    case "*" -> first * second;
                    case "/" -> first / second;
                    default -> 1;
                };

                out.writeUTF("" + res);
                out.flush();
            }
        } catch (Exception e) {
            System.out.println("Подключение прервано");
        }
    }
}

