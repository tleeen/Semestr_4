package com.example.lab_5_java.DB;

import javafx.event.ActionEvent;
import javafx.fxml.FXML;
import javafx.scene.control.Button;
import javafx.scene.control.TextField;
import javafx.stage.Stage;

import com.example.lab_5_java.Product;

public class Controller_2{
    @FXML
    private TextField col;

    @FXML
    private TextField title;

    @FXML
    private Button btn_ok;

    @FXML
    void insert(ActionEvent event) {
        String titleString = title.getText();
        String colString = col.getText();
        Product.addProduct(titleString, colString);
        Stage stage = (Stage) btn_ok.getScene().getWindow();
        Controller.refresh();
        stage.close();
    }
}

