module com.example.lab_4_java {
    requires javafx.controls;
    requires javafx.fxml;


    opens com.example.lab_4_java to javafx.fxml;
    exports com.example.lab_4_java;
}