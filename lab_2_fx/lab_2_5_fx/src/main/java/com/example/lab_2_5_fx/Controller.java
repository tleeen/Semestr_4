package com.example.lab_2_5_fx;

import javafx.scene.control.Button;
import javafx.scene.control.RadioButton;
import javafx.scene.text.Text;



public class Controller {


    public RadioButton red;

    public RadioButton whi;

    public Button btncl;

    public RadioButton blu;

    public Text txt;

    public RadioButton yel;

    public RadioButton gre;

    public void click_on_clear() {
        txt.setText(" ");
    }

    public void click_on_red() {
        if (red.isSelected()) {
            txt.setText(txt.getText() + "Красный ");
        }
        else{
            String a = txt.getText();
            for (int i = 0; i < 8; i++) {
                a = removeLastChar(a);
            }
            txt.setText(a);
        }
    }

    public void click_on_blue() {
        if (blu.isSelected()) {
            txt.setText(txt.getText() + "Синий ");
        }
        else{
            String a = txt.getText();
            for (int i = 0; i < 6; i++) {
                a = removeLastChar(a);
            }
            txt.setText(a);
        }
    }

    public void click_on_white() {
        if (whi.isSelected()) {
            txt.setText(txt.getText() + "Белый ");
        }
        else{
            String a = txt.getText();
            for (int i = 0; i < 6; i++) {
                a = removeLastChar(a);
            }
            txt.setText(a);
        }
    }

    public void click_on_yellow() {
        if (yel.isSelected()) {
            txt.setText(txt.getText() + "Жёлтый ");
        }
        else{
            String a = txt.getText();
            for (int i = 0; i < 7; i++) {
                a = removeLastChar(a);
            }
            txt.setText(a);
        }
    }

    public void click_on_green() {
        if (gre.isSelected()) {
            txt.setText(txt.getText() + "Зелёный ");
        }
        else{
            String a = txt.getText();
            for (int i = 0; i < 8; i++) {
                a = removeLastChar(a);
            }
            txt.setText(a);
        }
    }

    public static String removeLastChar(String s) {
        return (s == null || s.length() == 0) ? null : (s.substring(0, s.length() - 1));
    }
}
