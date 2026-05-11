package com.dev.aetherion.ai;

public record ModelConfig(String modelPath, boolean cloudDisabled) {
    public static ModelConfig defaultOfflineConfig() {
        return new ModelConfig("res/Config/models/local-model-path.txt", true);
    }
}
