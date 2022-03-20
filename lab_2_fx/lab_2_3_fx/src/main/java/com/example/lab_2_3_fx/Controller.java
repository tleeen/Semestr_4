package com.example.lab_2_3_fx;

import javafx.fxml.FXML;
import javafx.scene.control.Button;
import javafx.scene.text.Text;


public class Controller {
    @FXML

    public Button btn1;

    public Text col3;

    public Button btn2;

    public Button btn3;

    public Button btn4;

    public Button btn5;

    public Text pr1;

    public Text col2;

    public Text fpr;

    public Text pr3;

    public Text col4;

    public Text pr2;

    public Text pr4;

    public Text col1;

    public Text pr5;

    public Text col5;


    public void click_on_one() {
        int a = Integer.parseInt(pr1.getText());
        a += 590;
        pr1.setText(String.valueOf(a));
        int b = Integer.parseInt(col1.getText());
        b += 1;
        col1.setText(String.valueOf(b));
        int c = Integer.parseInt(fpr.getText());
        c += 590;
        fpr.setText(String.valueOf(c));
    }

    public void click_on_two() {
        int a = Integer.parseInt(pr2.getText());
        a += 620;
        pr2.setText(String.valueOf(a));
        int b = Integer.parseInt(col2.getText());
        b += 1;
        col2.setText(String.valueOf(b));
        int c = Integer.parseInt(fpr.getText());
        c += 620;
        fpr.setText(String.valueOf(c));
    }

    public void click_on_three() {
        int a = Integer.parseInt(pr3.getText());
        a += 450;
        pr3.setText(String.valueOf(a));
        int b = Integer.parseInt(col3.getText());
        b += 1;
        col3.setText(String.valueOf(b));
        int c = Integer.parseInt(fpr.getText());
        c += 450;
        fpr.setText(String.valueOf(c));
    }

    public void click_on_four() {
        int a = Integer.parseInt(pr4.getText());
        a += 380;
        pr4.setText(String.valueOf(a));
        int b = Integer.parseInt(col4.getText());
        b += 1;
        col4.setText(String.valueOf(b));
        int c = Integer.parseInt(fpr.getText());
        c += 380;
        fpr.setText(String.valueOf(c));
    }

    public void click_on_five() {
        int a = Integer.parseInt(pr5.getText());
        a += 430;
        pr5.setText(String.valueOf(a));
        int b = Integer.parseInt(col5.getText());
        b += 1;
        col5.setText(String.valueOf(b));
        int c = Integer.parseInt(fpr.getText());
        c += 430;
        fpr.setText(String.valueOf(c));
    }

}

