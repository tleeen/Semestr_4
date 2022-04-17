package com.example.lab_4_java;

import javafx.fxml.FXML;
import javafx.scene.control.Button;
import javafx.scene.text.Text;

public class Controller {
    private final Net net = new Net();

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

    public void sendData(String a, String b, String c) {
        String[] labelTexts = new String[3];
        labelTexts[0] = a;
        labelTexts[1] = c;
        labelTexts[2] = b;
        net.sendToServer(labelTexts);
    }

    public void click_on_enter() {
        String tmp = txt.getText();
        String[] parts = tmp.split(" ");
        String b = parts[parts.length - 1];
        int pos = txt.getText().indexOf(" ");
        String a = tmp.substring(0, pos);
        String c = tmp.substring(pos + 1, pos + 2);

        sendData(a, b, c);

        String res = "";
        try {
            res = net.receiveFromServ();
        } catch (Exception e) {
            e.printStackTrace();
        }
        txt.setText(res);
    }
    public void click_on_clear() {
        txt.setText("");
    }
}