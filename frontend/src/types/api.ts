export interface AgentStatus {
    running: boolean;
    status: string;
    startup_automation_enabled: boolean;
    internet_connected: boolean;
    chrome_available: boolean;
    active_chrome_profile: string;
    last_startup: string;
}

export interface StartupConfig {
    enabled?: boolean; // legacy
    startup_enabled?: boolean;
    startup_delay?: number; // legacy
    startup_delay_seconds?: number;
    wait_for_network: boolean;
    network_timeout?: number; // legacy
    network_timeout_seconds?: number;
    retry_interval?: number; // legacy
    network_retry_interval_seconds?: number;
    startup_websites?: string[]; // legacy
    startup_urls?: string[];
    chrome_profile?: string;
}

export interface BrowserStatus {
    available: boolean;
    browser: string;
    active_profile: string;
}

export interface ChromeProfile {
    name: string;
    display_name: string;
}

export interface NetworkStatus {
    connected: boolean;
    latency_ms: number;
}

export interface Application {
    id: string;
    name: string;
    path: string;
    allowed: boolean;
}

export interface LogEntry {
    timestamp: string;
    level: string;
    message: string;
}

export interface WorkflowStepResult {
    name: string;
    status: string;
}

export interface StartupWorkflowResult {
    success: boolean;
    steps: WorkflowStepResult[];
}

export interface ApiResponse {
    success: boolean;
    message: string;
}
