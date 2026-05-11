package com.dev.aetherion;

import javafx.application.Application;
import javafx.fxml.FXMLLoader;
import javafx.scene.Scene;
import javafx.stage.Stage;

import java.io.IOException;
import java.util.Objects;

public class AetherionApplication extends Application {
    private static final int MIN_WIDTH = 1180;
    private static final int MIN_HEIGHT = 720;

    @Override
    public void start(Stage stage) throws IOException {
        FXMLLoader loader = new FXMLLoader(AetherionApplication.class.getResource("views/Aetherion.fxml"));
        Scene scene = new Scene(loader.load(), 1320, 820);
        scene.getStylesheets().add(Objects.requireNonNull(
                AetherionApplication.class.getResource("styles/Main.css")
        ).toExternalForm());

        stage.setTitle("Aetherion MasterCore");
        stage.setMinWidth(MIN_WIDTH);
        stage.setMinHeight(MIN_HEIGHT);
        stage.setScene(scene);
        stage.show();
    }

    public static void main(String[] args) {
        launch(args);
    }
}
