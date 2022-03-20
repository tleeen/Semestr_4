package com.example.lab_2_javafx;

import javafx.event.ActionEvent;
import javafx.fxml.FXML;
import javafx.scene.control.Button;
import javafx.scene.control.TextField;
import javafx.scene.input.MouseEvent;


public class Controller {

    @FXML
    private Button btn;
    @FXML
    private TextField tx1;
    @FXML
    private TextField tx2;

    @FXML
    private void setArrow(MouseEvent event){
        if (tx2.getText() == "" & tx1.isFocused() & tx1.getText() == ""){
            btn.setText("->");
        }
        else if (tx2.getText() == "" & tx2.isFocused() & tx1.getText() == "" ){
            btn.setText("<-");
        }
    }

    @FXML
    private void click(ActionEvent event) {
        if (tx1.getText() != ""){
            tx2.setText(tx1.getText());
            tx1.clear();
            btn.setText("<-");
        }
        else if (tx2.getText() != ""){
            tx1.setText(tx2.getText());
            tx2.clear();
            btn.setText("->");
        }
    }
}
