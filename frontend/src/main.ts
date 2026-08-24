import { APIService } from './services/api';

document.addEventListener('DOMContentLoaded', async () => {
    // DOM Elements
    const elAgentStatusDesc = document.getElementById('agent-status-desc')!;
    const elAgentOnlineBadge = document.getElementById('agent-online-badge')!;
    const elStartupStatus = document.getElementById('startup-status')!;
    const elInternetStatus = document.getElementById('internet-status')!;
    const elChromeStatus = document.getElementById('chrome-status')!;
    const elProfileName = document.getElementById('profile-name')!;

    // Buttons
    const btnStopAgent = document.getElementById('btn-stop-agent') as HTMLButtonElement;
    const btnRestartAgent = document.getElementById('btn-restart-agent') as HTMLButtonElement;
    const btnYoutube = document.getElementById('btn-youtube') as HTMLButtonElement;
    const btnChrome = document.getElementById('btn-chrome') as HTMLButtonElement;
    const btnStartup = document.getElementById('btn-startup') as HTMLButtonElement;

    const elConfigEnabled = document.getElementById('config-enabled') as HTMLInputElement;
    const elConfigWaitNetwork = document.getElementById('config-wait-network') as HTMLInputElement;
    const elConfigDelay = document.getElementById('config-delay') as HTMLInputElement;
    const elConfigNetTimeout = document.getElementById('config-net-timeout') as HTMLInputElement;
    const elConfigNetRetry = document.getElementById('config-net-retry') as HTMLInputElement;
    const elConfigProfile = document.getElementById('config-profile') as HTMLSelectElement;
    const elConfigUrls = document.getElementById('config-urls') as HTMLInputElement;
    const btnSaveConfig = document.getElementById('btn-save-config') as HTMLButtonElement;

    const setButtonLoading = (btn: HTMLButtonElement, loading: boolean, originalText: string, icon: string) => {
        if (loading) {
            btn.innerHTML = `<span class="material-symbols-outlined text-sm animate-spin">refresh</span> Loading...`;
            btn.disabled = true;
        } else {
            btn.innerHTML = `<span class="material-symbols-outlined text-sm">${icon}</span> ${originalText}`;
            btn.disabled = false;
        }
    };

    const updateDashboard = async () => {
        try {
            const status = await APIService.getAgentStatus();
            elAgentStatusDesc.innerText = status.running ? "Running efficiently" : "Offline / Stopped";
            elAgentStatusDesc.className = status.running ? "font-caption text-caption text-secondary" : "font-caption text-caption text-error";
            
            elAgentOnlineBadge.innerText = status.running ? "ONLINE" : "OFFLINE";
            elAgentOnlineBadge.className = status.running ? "font-label-mono text-label-mono text-secondary" : "font-label-mono text-label-mono text-error";

            elStartupStatus.innerText = status.startup_automation_enabled ? "Enabled" : "Disabled";
            
            elInternetStatus.innerText = status.internet_connected ? "Connected" : "Disconnected";
            elInternetStatus.className = status.internet_connected ? "font-body-md text-body-md text-secondary font-medium" : "font-body-md text-body-md text-error font-medium";
            
            elChromeStatus.innerText = status.chrome_available ? "Available" : "Missing";
            elProfileName.innerText = status.active_chrome_profile;
        } catch (error) {
            elAgentStatusDesc.innerText = "Backend Offline";
            elAgentStatusDesc.className = "font-caption text-caption text-error";
            elAgentOnlineBadge.innerText = "OFFLINE";
            elAgentOnlineBadge.className = "font-label-mono text-label-mono text-error";
            // Show error states globally
        }
    };

    // Event Listeners
    btnStopAgent.addEventListener('click', async () => {
        setButtonLoading(btnStopAgent, true, "Stop Agent", "stop_circle");
        try {
            await APIService.stopAgent();
            await updateDashboard();
        } catch(e) {}
        setButtonLoading(btnStopAgent, false, "Stop Agent", "stop_circle");
    });

    btnRestartAgent.addEventListener('click', async () => {
        setButtonLoading(btnRestartAgent, true, "Restart", "restart_alt");
        try {
            await APIService.restartAgent();
            await updateDashboard();
        } catch(e) {}
        setButtonLoading(btnRestartAgent, false, "Restart", "restart_alt");
    });

    btnYoutube.addEventListener('click', async () => {
        console.log("Opening YouTube...")
        const origText = `<div class="font-body-md text-body-md text-on-surface font-medium">Open YouTube</div><div class="font-caption text-caption text-on-surface-variant">Media workflow</div>`;
        const iconDiv = btnYoutube.querySelector('div')!.outerHTML;
        btnYoutube.innerHTML = `<span class="material-symbols-outlined text-sm animate-spin">refresh</span> Opening YouTube...`;
        btnYoutube.disabled = true;
        try {
            await APIService.openYouTube();
            alert("Success opening YouTube!");
        } catch(e) {
            alert("Failed to open YouTube.")
        }
        btnYoutube.innerHTML = iconDiv + `<div>${origText}</div>`;
        btnYoutube.disabled = false;
    });

    btnChrome.addEventListener('click', async () => {
        const iconDiv = btnChrome.querySelector('div')!.outerHTML;
        const origText = `<div class="font-body-md text-body-md text-on-surface font-medium">Open Chrome</div><div class="font-caption text-caption text-on-surface-variant">Default browser</div>`;
        btnChrome.innerHTML = `<span class="material-symbols-outlined text-sm animate-spin">refresh</span> Opening Chrome...`;
        btnChrome.disabled = true;
        try {
            await APIService.openUrl("https://google.com");
            alert("Success opening Chrome!");
        } catch(e) {
            alert("Failed to open Chrome.");
        }
        btnChrome.innerHTML = iconDiv + `<div>${origText}</div>`;
        btnChrome.disabled = false;
    });

    btnStartup.addEventListener('click', async () => {
        const iconDiv = btnStartup.querySelector('div')!.outerHTML;
        const origText = `<div class="font-body-md text-body-md text-on-surface font-medium">Run Startup Workflow</div><div class="font-caption text-caption text-on-surface-variant">Execute routine</div>`;
        btnStartup.innerHTML = `<span class="material-symbols-outlined text-sm animate-spin">refresh</span> Running Workflow...`;
        btnStartup.disabled = true;
        try {
            await APIService.runStartupWorkflow();
            alert("Startup workflow completed successfully.");
        } catch(e) {
            alert("Failed to run workflow.");
        }
        btnStartup.innerHTML = iconDiv + `<div>${origText}</div>`;
        btnStartup.disabled = false;
    });
    
    // Save Config Action
    btnSaveConfig.addEventListener('click', async () => {
        setButtonLoading(btnSaveConfig, true, "Save Configuration", "save");
        try {
            await APIService.updateStartupConfig({
                enabled: elConfigEnabled.checked,
                startup_delay: parseInt(elConfigDelay.value, 10) || 0,
                wait_for_network: elConfigWaitNetwork.checked,
                network_timeout: parseInt(elConfigNetTimeout.value, 10) || 60,
                retry_interval: parseInt(elConfigNetRetry.value, 10) || 5,
                chrome_profile: elConfigProfile.value,
                startup_websites: elConfigUrls.value.split(",").map(s => s.trim())
            });
            alert("Configuration saved successfully.");
            await fetchConfig();
        } catch(e) {
            alert("Error saving configuration.");
        }
        setButtonLoading(btnSaveConfig, false, "Save Configuration", "save");
    });
    
    const fetchConfig = async () => {
        try {
            const config = (await fetch('/api/startup/config')).json();
            const data = await config;
            // Support both old and new schema keys gracefully bridging JSON
            elConfigEnabled.checked = data.startup_enabled ?? data.enabled;
            elConfigDelay.value = data.startup_delay_seconds ?? data.startup_delay;
            elConfigWaitNetwork.checked = data.wait_for_network;
            elConfigNetTimeout.value = data.network_timeout_seconds ?? data.network_timeout;
            elConfigNetRetry.value = data.network_retry_interval_seconds ?? data.retry_interval;
             
            // Setup Profile Select Options
            try {
                const pdata = await (await fetch('/api/browser/profiles')).json();
                elConfigProfile.innerHTML = "";
                pdata.profiles.forEach((p: any) => {
                    const opt = document.createElement("option");
                    opt.value = p.name;
                    opt.innerText = p.display_name;
                    elConfigProfile.appendChild(opt);
                });
            } catch(e) {}
            
            elConfigProfile.value = data.chrome_profile ?? "Default";
            elConfigUrls.value = (data.startup_urls ?? data.startup_websites).join(", ");
        } catch (e) {
            console.error("Failed to load config.");
        }
    };

    // Initial load
    updateDashboard();
    fetchConfig();
    
    // Polling every 10 seconds
    setInterval(updateDashboard, 10000);
});
