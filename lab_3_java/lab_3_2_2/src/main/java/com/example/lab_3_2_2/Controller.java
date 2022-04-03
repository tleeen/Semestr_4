package com.example.lab_3_2_2;

import javafx.application.Platform;
import javafx.event.ActionEvent;
import javafx.fxml.FXML;
import javafx.scene.control.Button;

public class Controller {
    @FXML
    Button btn;

    @FXML
    private void click() {
        new NewThread("", btn);
    }

    static class NewThread implements Runnable {
        Button btn;

        NewThread(String name, Button btn) {
            this.btn = btn;
            Thread t = new Thread(this, name);
            System.out.println("Запуск потока" + t.getName());
            t.start();
        }

        public void run() {
            Thread t = Thread.currentThread();
            System.out.println(t.getName() + "Запуск");
            int i = 1;
            Platform.runLater(() -> btn.setText("Поток запущен"));
            while (true) {
                System.out.println(t.getName() + " Счётчик " + i);
                try {
                    Thread.sleep(1000);
                } catch (Exception ignored) {
                }
                i++;
            }
        }
    }
}