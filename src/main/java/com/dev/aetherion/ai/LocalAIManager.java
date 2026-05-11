package com.dev.aetherion.ai;

public class LocalAIManager {
    private ModelConfig modelConfig = ModelConfig.defaultOfflineConfig();

    public void configure(ModelConfig modelConfig) {
        this.modelConfig = modelConfig;
    }

    public String status() {
        return "Offline bridge ready. Model path: " + modelConfig.modelPath();
    }
}
