package com.example.lab_2_4_fx;

import javafx.application.Application;
import javafx.fxml.FXMLLoader;
import javafx.scene.Scene;
import javafx.stage.Stage;

public class Main extends Application {
    public Main() {
    }

    public static void main(String[] args) {
        Application.launch(args);
    }

    public void start(Stage stage) throws Exception {
        FXMLLoader fxmlLoader = new FXMLLoader(Main.class.getResource("FX.fxml"));
        Scene scene = new Scene(fxmlLoader.load(), 485, 630);
        stage.setTitle("Number 4");
        stage.setScene(scene);
        stage.show();
    }
}
