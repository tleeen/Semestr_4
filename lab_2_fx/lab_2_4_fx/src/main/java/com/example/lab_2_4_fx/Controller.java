package com.example.lab_2_4_fx;

import javafx.fxml.FXML;
import javafx.scene.control.Button;
import javafx.scene.text.Text;



public class Controller {

    @FXML

    public Button btn3;

    public Button btnpl;

    public Text txt;

    public Button btn1;

    public Button btn5;

    public Button btnum;

    public Button btn8;

    public Button btnmi;

    public Button btn9;

    public Button btn2;

    public Button btntoch;

    public Button btn7;

    public Button btn0;

    public Button btn6;

    public Button btnent;

    public Button btn4;

    public Button btnde;

    public Button btncl;

    @FXML

    public void click_on_one() {
        txt.setText(txt.getText() + 1);
    }

    public void click_on_two() {
        txt.setText(txt.getText() + 2);
    }

    public void click_on_three() {
        txt.setText(txt.getText() + 3);
    }

    public void click_on_four() {
        txt.setText(txt.getText() + 4);
    }

    public void click_on_five() {
        txt.setText(txt.getText() + 5);
    }

    public void click_on_six() {
        txt.setText(txt.getText() + 6);
    }

    public void click_on_seven() {
        txt.setText(txt.getText() + 7);
    }

    public void click_on_eight() {
        txt.setText(txt.getText() + 8);
    }

    public void click_on_nine() {
        txt.setText(txt.getText() + 9);
    }

    public void click_on_zero() {
        txt.setText(txt.getText() + 0);
    }

    public void click_on_toch() {
        txt.setText(txt.getText() + '.');
    }

    public void click_on_plus() {
        txt.setText(txt.getText() + ' ' + '+' + ' ');
    }

    public void click_on_minus() {
        txt.setText(txt.getText() + ' ' + '-' + ' ');
    }

    public void click_on_umn() {
        txt.setText(txt.getText() + ' ' + '*' + ' ');
    }

    public void click_on_del() {
        txt.setText(txt.getText() + ' ' + '/' + ' ');
    }

    public void click_on_enter() {
        String tmp = txt.getText();
        String[] parts = tmp.split(" ");
        String lastOne = parts[parts .length-1];
        float b = Float.parseFloat(lastOne);
        int pos = txt.getText().indexOf(" ");
        float a = Float.parseFloat(tmp.substring(0, pos));
        String c = tmp.substring(pos + 1, pos + 2);
        if (c.equals("+")) {
            txt.setText(String.valueOf(a + b));
        }
        if (c.equals("-")) {
            txt.setText(String.valueOf(a - b));
        }
        if (c.equals("*")) {
            txt.setText(String.valueOf(a * b));
        }
        if (c.equals("/")) {
            if (b != 0) {
                txt.setText(String.valueOf(a / b));
            }
            else{
                    txt.setText("Ошибка: нельзя делить на ноль");

                }
        }
    }

    public void click_on_clear() {
        txt.setText("");
    }
}
