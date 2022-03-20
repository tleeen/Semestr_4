package com.example.lab_2_javafx;

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
        Scene scene = new Scene(fxmlLoader.load(), 777, 245);

        stage.setTitle("Number 1");
        stage.setScene(scene);
        stage.show();
    }
}