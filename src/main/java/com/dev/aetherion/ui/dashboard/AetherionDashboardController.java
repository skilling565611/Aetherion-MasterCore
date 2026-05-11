package com.dev.aetherion.ui.dashboard;

import com.dev.aetherion.ai.CharacterGenerator;
import com.dev.aetherion.ai.LocalAIManager;
import com.dev.aetherion.ai.ModelConfig;
import com.dev.aetherion.ai.PromptRouter;
import com.dev.aetherion.ai.SafetyRules;
import javafx.fxml.FXML;
import javafx.scene.control.Label;
import javafx.scene.control.TextArea;
import javafx.scene.layout.ColumnConstraints;
import javafx.scene.layout.GridPane;
import javafx.scene.layout.HBox;
import javafx.scene.layout.Priority;
import javafx.scene.layout.VBox;

import java.time.LocalTime;
import java.time.format.DateTimeFormatter;

public class AetherionDashboardController {
    private final LocalAIManager localAIManager = new LocalAIManager();
    private final PromptRouter promptRouter = new PromptRouter();
    private final SafetyRules safetyRules = new SafetyRules();
    private final CharacterGenerator characterGenerator = new CharacterGenerator();
    private final DateTimeFormatter timeFormatter = DateTimeFormatter.ofPattern("HH:mm:ss");

    @FXML
    private VBox centerWorkspace;

    @FXML
    private TextArea aiCommandInput;

    @FXML
    private Label footerStatus;

    @FXML
    private Label activeViewLabel;

    @FXML
    private Label localAiStatus;

    @FXML
    public void initialize() {
        localAIManager.configure(ModelConfig.defaultOfflineConfig());
        showDashboard();
        setFooter("Aetherion MasterCore initialized in offline-first mode.");
    }

    @FXML
    private void showDashboard() {
        activeViewLabel.setText("Dashboard");
        centerWorkspace.getChildren().setAll(
                sectionHeader("Dashboard Overview", "Offline systems, modules, and runtime activity"),
                metricGrid(),
                moduleLifecycle(),
                activityFeed(),
                aiInteractionPanel()
        );
    }

    @FXML
    private void showAiCore() {
        activeViewLabel.setText("AI Core");
        centerWorkspace.getChildren().setAll(
                sectionHeader("AI Core", "Local AI bridge placeholders and character tools"),
                statusCard("Local Model Runner", localAIManager.status(), "cyan"),
                statusCard("Model Slot", "No model bundled. GGUF/ONNX path support planned.", "amber"),
                statusCard("Image Recognition", "Offline image recognition placeholder ready.", "green"),
                statusCard("File Analysis", "Local-only file analysis placeholder ready.", "cyan"),
                statusCard("Character/Profile Tools", characterGenerator.previewProfile(), "amber"),
                statusCard("Command Queue", promptRouter.route("diagnostics"), "green")
        );
        setFooter("AI Core view loaded without cloud dependency.");
    }

    @FXML
    private void showSystems() {
        activeViewLabel.setText("Systems");
        centerWorkspace.getChildren().setAll(
                sectionHeader("Systems", "Device modes, performance controls, and sync status"),
                statusCard("Control Prime Mode", "Full/dev mode. Heavy local tools allowed on main PC.", "cyan"),
                statusCard("Arctic Prime Mode", "Portable runtime. Lightweight startup and low resource use.", "green"),
                statusCard("Storage Mode", "Local storage first. No cloud requirement.", "amber"),
                statusCard("Device Sync", "Manual/offline sync placeholder. User-enabled networking later.", "cyan"),
                statusCard("Performance Controls", "Profiles planned for low RAM/CPU operation.", "green"),
                statusCard("Module Controls", "Lifecycle hooks prepared for V2.0 modules.", "amber")
        );
        setFooter("Systems view loaded.");
    }

    @FXML
    private void showDeveloper() {
        activeViewLabel.setText("Developer");
        centerWorkspace.getChildren().setAll(
                sectionHeader("Developer", "Debugging, packaging, GitHub, and diagnostics utilities"),
                statusCard("Debug Console", "Runtime console placeholder ready.", "cyan"),
                statusCard("Runtime Logs", "Local log viewer placeholder ready.", "green"),
                statusCard("Build / Export", "Windows EXE packaging plan reserved under res/Exe/.", "amber"),
                statusCard("GitHub Status", "Repository-safe Gradle structure active.", "cyan"),
                statusCard("Diagnostics", safetyRules.describe(), "green"),
                statusCard("Developer Utilities", "Hooks available for future build tooling.", "amber")
        );
        setFooter("Developer view loaded.");
    }

    @FXML
    private void runDiagnostics() {
        localAiStatus.setText("AI Status: offline ready");
        setFooter("Diagnostics completed at " + LocalTime.now().format(timeFormatter) + ".");
    }

    @FXML
    private void exitApplication() {
        centerWorkspace.getScene().getWindow().hide();
    }

    @FXML
    private void sendAiCommand() {
        String prompt = aiCommandInput == null ? "" : aiCommandInput.getText().trim();
        if (prompt.isEmpty()) {
            setFooter("AI command ignored: no local prompt entered.");
            return;
        }

        setFooter(promptRouter.route(prompt));
        aiCommandInput.clear();
    }

    @FXML
    private void showPlaceholder() {
        activeViewLabel.setText("Module Placeholder");
        centerWorkspace.getChildren().setAll(
                sectionHeader("Module Placeholder", "This center workspace area is reserved for V2.0 section views."),
                statusCard("Locked Shell", "Top bar, sidebar, right rail, and footer remain stable.", "cyan"),
                statusCard("Expansion Path", "New modules should replace only center workspace content.", "green")
        );
        setFooter("Placeholder module selected.");
    }

    private VBox sectionHeader(String title, String subtitle) {
        Label titleLabel = new Label(title);
        titleLabel.getStyleClass().add("section-title");
        Label subtitleLabel = new Label(subtitle);
        subtitleLabel.getStyleClass().add("section-subtitle");

        VBox box = new VBox(4, titleLabel, subtitleLabel);
        box.getStyleClass().add("section-header");
        return box;
    }

    private GridPane metricGrid() {
        GridPane grid = new GridPane();
        grid.getStyleClass().add("dashboard-grid");
        grid.setHgap(14);
        grid.setVgap(14);
        grid.setMaxWidth(Double.MAX_VALUE);

        ColumnConstraints leftColumn = new ColumnConstraints();
        leftColumn.setPercentWidth(50);
        leftColumn.setHgrow(Priority.ALWAYS);
        ColumnConstraints rightColumn = new ColumnConstraints();
        rightColumn.setPercentWidth(50);
        rightColumn.setHgrow(Priority.ALWAYS);
        grid.getColumnConstraints().addAll(leftColumn, rightColumn);

        grid.add(statusCard("Core Runtime", "Online locally. Cloud services disabled.", "cyan"), 0, 0);
        grid.add(statusCard("Safe Mode", "Enabled. Protected offline-first operation.", "green"), 1, 0);
        grid.add(statusCard("Device Profile", "Control Prime development profile active.", "amber"), 0, 1);
        grid.add(statusCard("Module Slots", "12 registered placeholders for V2.0.", "cyan"), 1, 1);
        return grid;
    }

    private VBox moduleLifecycle() {
        VBox box = statusCard("Module Lifecycle", "Load -> validate -> activate -> monitor -> suspend.", "green");
        Label detail = new Label("Dashboard shell ready for AI Core, Systems, and Developer center views.");
        detail.getStyleClass().add("card-body");
        detail.setWrapText(true);
        box.getChildren().add(detail);
        return box;
    }

    private VBox activityFeed() {
        VBox box = statusCard("System Activity Feed", "20:00 local runtime initialized\n20:01 dashboard shell locked\n20:02 offline AI placeholders ready", "cyan");
        return box;
    }

    private VBox aiInteractionPanel() {
        VBox box = statusCard("AI Interaction Area", "Local command routing placeholder. No paid API or internet required.", "amber");
        return box;
    }

    private VBox statusCard(String title, String body, String accent) {
        Label titleLabel = new Label(title);
        titleLabel.getStyleClass().add("card-title");
        titleLabel.setWrapText(true);
        titleLabel.setMaxWidth(Double.MAX_VALUE);
        Label bodyLabel = new Label(body);
        bodyLabel.getStyleClass().add("card-body");
        bodyLabel.setWrapText(true);
        bodyLabel.setMaxWidth(Double.MAX_VALUE);

        VBox card = new VBox(8, titleLabel, bodyLabel);
        card.getStyleClass().addAll("control-card", "accent-" + accent);
        card.setMaxWidth(Double.MAX_VALUE);
        card.setMinHeight(96);
        GridPane.setHgrow(card, Priority.ALWAYS);
        HBox.setHgrow(card, Priority.ALWAYS);
        VBox.setVgrow(card, Priority.NEVER);
        return card;
    }

    private void setFooter(String message) {
        if (footerStatus != null) {
            footerStatus.setText(message);
        }
    }
}
