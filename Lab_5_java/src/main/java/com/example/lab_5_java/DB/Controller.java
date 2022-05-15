package com.example.lab_5_java.DB;

import com.example.lab_5_java.Date_base;
import com.example.lab_5_java.Product;
import java.sql.Statement;
import java.io.IOException;
import java.net.URL;
import java.sql.Connection;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.util.Objects;
import java.util.ResourceBundle;
import javafx.collections.FXCollections;
import javafx.collections.ObservableList;
import javafx.event.ActionEvent;
import javafx.event.EventHandler;
import javafx.fxml.FXML;
import javafx.fxml.FXMLLoader;
import javafx.fxml.Initializable;
import javafx.scene.Parent;
import javafx.scene.Scene;
import javafx.scene.control.Button;
import javafx.scene.control.ContextMenu;
import javafx.scene.control.MenuItem;
import javafx.scene.control.TableColumn;
import javafx.scene.control.TableView;
import javafx.scene.control.TextField;
import javafx.scene.control.cell.PropertyValueFactory;
import javafx.scene.input.MouseButton;
import javafx.scene.input.MouseEvent;
import javafx.stage.Modality;
import javafx.stage.Stage;


public class Controller implements Initializable{

    @FXML
    TableView<Product> Date_base_table;
    static TableView<Product> DB_table_copy;
    @FXML
    TableColumn<Product, Integer> table_id;
    @FXML
    TableColumn<Product, String> table_title_p;
    @FXML
    TableColumn<Product, Integer> table_col_p;
    @FXML
    Button btn_f;
    @FXML
    TextField textQuery;
    Date_base db;
    Connection con = null;
    ObservableList<Product> products;

    @Override
    public void initialize(URL arg0, ResourceBundle arg1) {
        products = FXCollections.observableArrayList();
        table_id.setCellValueFactory(new PropertyValueFactory<>("id"));
        table_title_p.setCellValueFactory(new PropertyValueFactory<>("title"));
        table_col_p.setCellValueFactory(new PropertyValueFactory<>("col"));
        db = new Date_base("postgres", "1234");
        con = db.getConnection();

        ContextMenu cm = new ContextMenu();
        MenuItem act1 = new MenuItem("Insert");
        cm.getItems().add(act1);
        MenuItem act2 = new MenuItem("Update");
        cm.getItems().add(act2);
        MenuItem act3 = new MenuItem("Delete");
        cm.getItems().add(act3);

        Date_base_table.addEventHandler(MouseEvent.MOUSE_CLICKED, click -> {
            if(click.getButton() == MouseButton.SECONDARY) {
                cm.show(DB_table_copy, click.getScreenX(), click.getScreenY());
            }
        });

        act1.setOnAction(event -> insert());

        act2.setOnAction(event -> update());

        act3.setOnAction(event -> delete());
        DB_table_copy = Date_base_table;
        refresh();
    }

    public void insert(){
        Stage stage = new Stage();
        Parent root;
        try {
            root = FXMLLoader.load(Objects.requireNonNull(getClass().getResource("FX_2.fxml")));
            Scene scene = new Scene(root);
            stage.setScene(scene);
            stage.setTitle("INSERT");
            stage.setResizable(false);
            stage.initModality(Modality.WINDOW_MODAL);
            stage.initOwner(Date_base_table.getScene().getWindow());
            stage.show();
        } catch (IOException e) {
            e.printStackTrace();
        }
        refresh();
    }

    public void update(){
        Stage stage = new Stage();
        Parent root;
        try {
            root = FXMLLoader.load(Objects.requireNonNull(getClass().getResource("FX_3.fxml")));
            Scene scene = new Scene(root);
            stage.setScene(scene);
            stage.setTitle("UPDATE");
            stage.setResizable(false);
            stage.initModality(Modality.WINDOW_MODAL);
            stage.initOwner(Date_base_table.getScene().getWindow());
            stage.show();
        } catch (IOException e) {
            e.printStackTrace();
        }
        refresh();
    }

    public void delete(){
        String id = String.valueOf(DB_table_copy.getSelectionModel().getSelectedItem().getId());
        Product.deleteProduct(id);
        refresh();
    }

    static public void refresh(){
        ObservableList<Product> products = FXCollections.observableArrayList();
        try {
            products = Product.getAllProducts();
        } catch (SQLException e) {
            e.printStackTrace();
        }
        DB_table_copy.setItems(products);
    }

    @FXML
    public void filt(){
        String query;
        ObservableList<Product> products;
        query = textQuery.getText();
        if (query.equals("")){
            refresh();
            return;
        }
        try {
            products = Product.getFilteredProducts(query);
            DB_table_copy.setItems(products);
        } catch (Exception e) {
            textQuery.setText("Invalid query");
        }
    }
}