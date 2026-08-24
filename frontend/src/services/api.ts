import {
    AgentStatus,
    StartupConfig,
    BrowserStatus,
    ChromeProfile,
    NetworkStatus,
    Application,
    LogEntry,
    StartupWorkflowResult,
    ApiResponse
} from '../types/api';

const API_URL = 'http://127.0.0.1:8000/api';

async function fetchApi<T>(endpoint: string, options: RequestInit = {}): Promise<T> {
    try {
        const response = await fetch(`${API_URL}${endpoint}`, {
            ...options,
            headers: {
                'Content-Type': 'application/json',
                ...options.headers,
            },
        });
        if (!response.ok) {
            throw new Error(`API error: ${response.status}`);
        }
        return await response.json();
    } catch (error) {
        console.error(`Error fetching ${endpoint}:`, error);
        throw error;
    }
}

export const APIService = {
    getHealth: () => fetchApi<{status: string, service: string}>('/health'),
    
    getAgentStatus: () => fetchApi<AgentStatus>('/agent/status'),
    startAgent: () => fetchApi<ApiResponse>('/agent/start', { method: 'POST' }),
    stopAgent: () => fetchApi<ApiResponse>('/agent/stop', { method: 'POST' }),
    restartAgent: () => fetchApi<ApiResponse>('/agent/restart', { method: 'POST' }),
    
    getStartupConfig: () => fetchApi<StartupConfig>('/startup/config'),
    updateStartupConfig: (config: StartupConfig) => fetchApi<ApiResponse>('/startup/config', {
        method: 'PUT',
        body: JSON.stringify(config)
    }),
    runStartupWorkflow: () => fetchApi<StartupWorkflowResult>('/startup/run', { method: 'POST' }),
    
    getBrowserStatus: () => fetchApi<BrowserStatus>('/browser/status'),
    getChromeProfiles: () => fetchApi<{profiles: ChromeProfile[]}>('/browser/profiles').then(d => d.profiles),
    setChromeProfile: (profile: string) => fetchApi<ApiResponse>('/browser/profile', {
        method: 'PUT',
        body: JSON.stringify({ profile })
    }),
    openYouTube: () => fetchApi<ApiResponse>('/browser/youtube', { method: 'POST' }),
    openUrl: (url: string) => fetchApi<ApiResponse>('/browser/open', {
        method: 'POST',
        body: JSON.stringify({ url })
    }),
    
    getNetworkStatus: () => fetchApi<NetworkStatus>('/network/status'),
    getApplications: () => fetchApi<Application[]>('/applications'),
    launchApplication: (id: string) => fetchApi<ApiResponse>(`/applications/${id}/launch`, { method: 'POST' }),
    getLogs: (limit = 100) => fetchApi<{logs: LogEntry[]}>(`/logs?limit=${limit}`).then(d => d.logs),
};
