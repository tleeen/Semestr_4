package com.example.lab_5_java;

import javafx.beans.property.SimpleIntegerProperty;
import javafx.beans.property.SimpleStringProperty;
import javafx.collections.FXCollections;
import javafx.collections.ObservableList;

import java.sql.ResultSet;
import java.sql.SQLException;

public class Product {
    public SimpleIntegerProperty id;
    public SimpleStringProperty title;
    public SimpleIntegerProperty col;

    public Product(int id, String title, int col){
        this.id = new SimpleIntegerProperty(id);
        this.title = new SimpleStringProperty(title);
        this.col = new SimpleIntegerProperty(col);
    }

    public int getId(){
        return this.id.get();
    }

    public static ObservableList<Product> getAllProducts() throws SQLException{
        ObservableList<Product> products = FXCollections.observableArrayList();
        ResultSet rs;
        String query = "select * from product";
        rs = Date_base.exeQuery(query);
        while(rs.next()){
            Product Product = new Product(rs.getInt("id"), rs.getString("title"), rs.getInt("col"));
            products.add(Product);
        }
        return products;
    }

    public static ObservableList<Product> getFilteredProducts(String queryFilter) throws SQLException{
        ObservableList<Product> products = FXCollections.observableArrayList();
        ResultSet rs;
        String query = "select * from product where " + queryFilter + ";";
        rs = Date_base.exeQuery(query);
        while(rs.next()){
            Product Product = new Product(rs.getInt("id"), rs.getString("title"), rs.getInt("col"));
            products.add(Product);
        }
        return products;
    }

    public static void addProduct(String title, String col){
        String query = "insert into product(title, col)\nvalues (\'" + title + "\', " + col + ");";
        Date_base.exeUpdate(query);
    }

    public static void updateProduct(String id, String title, String col){
        String query = "update product\nset title=\'" + title + "\', col=" + col + " \nwhere id=" + id + ";";
        Date_base.exeUpdate(query);
    }

    public static void deleteProduct(String id){
        String query = "delete from product\nwhere id=" + id + ";";
        Date_base.exeUpdate(query);
    }
}

