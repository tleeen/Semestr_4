package com.example.demo;

import javafx.event.ActionEvent;
import javafx.fxml.FXML;
import javafx.scene.control.*;


public class Controller {

    @FXML
    public CheckBox ch1;
    @FXML
    public Label tx;
    @FXML
    public CheckBox ch2;
    @FXML
    public Slider sld;
    @FXML
    public CheckBox ch3;
    @FXML
    private Button btn;

    @FXML
    private void click_on(ActionEvent event) {

        if (ch1.isSelected()) {
            btn.setVisible(false);
        } else {
            btn.setVisible(true);
        }
        if (ch2.isSelected()) {
            tx.setVisible(false);
        } else {
            tx.setVisible(true);
        }
        if (ch3.isSelected()) {
            sld.setVisible(false);
        } else {
            sld.setVisible(true);
        }
    }
}

