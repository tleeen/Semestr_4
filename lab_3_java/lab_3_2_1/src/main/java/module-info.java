module com.example.lab_3_2_1 {
    requires javafx.controls;
    requires javafx.fxml;


    opens com.example.lab_3_2_1 to javafx.fxml;
    exports com.example.lab_3_2_1;
}