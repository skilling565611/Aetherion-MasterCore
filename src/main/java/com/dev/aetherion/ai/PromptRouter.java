package com.dev.aetherion.ai;

public class PromptRouter {
    public String route(String prompt) {
        return "Local prompt queued for future offline processing: " + prompt;
    }
}
