module com.example.lab_2_5_fx {
    requires javafx.controls;
    requires javafx.fxml;


    opens com.example.lab_2_5_fx to javafx.fxml;
    exports com.example.lab_2_5_fx;
}