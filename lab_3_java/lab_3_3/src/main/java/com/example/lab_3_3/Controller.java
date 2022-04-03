package com.example.lab_3_3;

import javafx.application.Platform;
import javafx.fxml.FXML;
import javafx.scene.control.Button;
import javafx.scene.control.ProgressBar;

public class Controller{
    public static boolean isSuspend = false;
    @FXML
    Button start, pause, stop;
    @FXML
    ProgressBar prog;

    @FXML
    private void startProgress(){
        if (!isSuspend){
            new NewThread("", prog, start, stop);
        }
    }

    @FXML
    private void pauseProgress(){
        if (!isSuspend){
            pause.setText("Продолжить");
            System.out.println("Пауза");
        }
        else{
            pause.setText("Пауза");
            System.out.println("Продолжение");
        }
        isSuspend = !isSuspend;
    }


}

class NewThread implements Runnable{
    ProgressBar prog;
    Button start;
    Button stop;

    NewThread(String name, ProgressBar prog, Button start, Button stop){
        this.start = start;
        this.stop = stop;
        this.prog = prog;
        Thread t = new Thread(this, name);
        System.out.println("Поток запущен" + t.getName());
        t.start();
    }

    public void run(){
        Thread t =  Thread.currentThread();
        System.out.println(t.getName() + "Cтарт");

        for(int i = 1; i<=1000; i++){

            if (start.isPressed() || stop.isPressed()){
                prog.setProgress(0);
                t.interrupt();
                System.out.println("Стоп");
                break;
            }

            while(Controller.isSuspend){
                try {
                    wait(0);
                } catch (Exception ignored) {}
            }

            final double j = i;
            Platform.runLater(() -> prog.setProgress(j/1000));
            try {
                Thread.sleep(20);} catch (Exception ignored) {}
        }
        t.interrupt();
    }
}