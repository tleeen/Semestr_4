package com.example.lab_5_java.DB;

import javafx.event.ActionEvent;
import javafx.fxml.FXML;
import javafx.scene.control.Button;
import javafx.scene.control.TextField;
import javafx.stage.Stage;

import com.example.lab_5_java.Product;

public class Controller_3 {

    @FXML
    private TextField col;

    @FXML
    private TextField id;

    @FXML
    private TextField title;

    @FXML
    private Button btn_ok;

    @FXML
    void update(ActionEvent event) {
        String idString =id.getText();
        String titleString = title.getText();
        String colString = col.getText();
        Product.updateProduct(idString, titleString, colString);
        Stage stage = (Stage) btn_ok.getScene().getWindow();
        Controller.refresh();
        stage.close();
    }

}

