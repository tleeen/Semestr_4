package com.example.lab_3_2_1;

import javafx.application.Platform;
import javafx.fxml.FXML;
import javafx.scene.control.Button;

public class Controller{
    @FXML
    Button btn;

    @FXML
    private void click(){
        Thread t = new NewThread2("", btn);
        t.start();
    }
}

class NewThread2 extends Thread{
    Button btn;

    NewThread2(String name, Button btn){
        super(name);
        this.btn = btn;
    }

    public void run(){
        Thread t =  Thread.currentThread();
        System.out.println(t.getName() + "Запуск");
        int i = 1;
        Platform.runLater(() -> btn.setText("Поток запущен"));
        while(true){
            System.out.println(t.getName() + " Счётчик " + i);
            try {
                sleep(1000);} catch (Exception ignored) {}
            i++;
        }
    }
}