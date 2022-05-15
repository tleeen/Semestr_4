package com.example.lab_5_java;

import javafx.application.Application;
import javafx.stage.Stage;
import javafx.scene.Scene;
import javafx.fxml.FXMLLoader;
import javafx.scene.Parent;

import java.util.Objects;

public class Main extends Application{
    public static void main(String[] args) {
        Application.launch(args);
    }

    @Override
    public void start(Stage stage) throws Exception {

        Parent root = FXMLLoader.load(Objects.requireNonNull(getClass().getResource("FX.fxml")));
        Scene scene = new Scene(root);

        stage.setScene(scene);

        stage.setTitle("Date_base");
        stage.show();
    }
}