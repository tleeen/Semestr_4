module com.example.lab_5_java {
    requires javafx.controls;
    requires javafx.fxml;
    requires java.sql;
    requires org.postgresql.jdbc;


    opens com.example.lab_5_java to javafx.fxml;
    exports com.example.lab_5_java;
}