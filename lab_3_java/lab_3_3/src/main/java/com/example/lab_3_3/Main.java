package com.example.lab_3_3;

import javafx.application.Application;
import javafx.stage.Stage;
import javafx.scene.Scene;
import javafx.fxml.FXMLLoader;

public class Main extends Application{
    public static void main(String[] args) {
        Application.launch(args);
    }

    @Override
    public void start(Stage stage) throws Exception {

        FXMLLoader fxmlLoader = new FXMLLoader(Main.class.getResource("FX.fxml"));
        Scene scene = new Scene(fxmlLoader.load(), 436, 150);
        stage.setTitle("Number 3");
        stage.setScene(scene);
        stage.show();
    }
}