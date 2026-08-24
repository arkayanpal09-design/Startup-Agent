# NOVA - Personal PC Startup Agent

This is a local Windows desktop automation agent that automatically prepares your PC. It bridges a Google Stitch generated frontend to a production-quality local FastAPI backend.

## Architecture

- **Frontend:** Google Stitch design, exported and adapted into a Vite + TypeScript application running on port 3000.
- **Backend:** Python + FastAPI running on port 8000, bound exclusively to `127.0.0.1`.
- **Communication:** REST API calls with strict CORS rules locking to local environment.

## Backend Setup

1. Open a terminal in `backend/`
2. Create virtual environment:
   ```powershell
   python -m venv .venv
   .\.venv\Scripts\Activate.ps1
   ```
3. Install dependencies:
   ```powershell
   pip install -r requirements.txt
   ```
4. Start the server:
   ```powershell
   python run.py
   # Or using uvicorn directly:
   uvicorn app.main:app --host 127.0.0.1 --port 8000 --reload
   ```

## Frontend Setup

1. Open a terminal in `frontend/`
2. Install dependencies:
   ```powershell
   npm install
   ```
3. Start the dev server:
   ```powershell
   npm run dev
   ```

## Available API Endpoints
- `GET /api/health` - Checks backend heartbeat
- `GET /api/agent/status` - Gets core memory status
- `POST /api/agent/start` - Starts automation loops
- `POST /api/agent/stop` - Stops automation loops
- `GET /api/startup/config` - Fetches the saved automation settings
- `POST /api/startup/run` - Fires the setup routine
- `GET /api/browser/status` - Checks if Google Chrome is installed
- `GET /api/browser/profiles` - Lists detected Chrome profiles
- `POST /api/browser/youtube` - Opens YouTube securely
- `GET /api/network/status` - Returns offline/online and ping latency
- `GET /api/applications` - Lists permitted apps
- `GET /api/logs` - Retrieves in-memory trace history

## Security
- API does NOT expose automation endpoints to `0.0.0.0`. Validated strict to `127.0.0.1`.
- `subprocess` modules in Python use hard-coded explicit variables without `shell=True` to prevent injection.
- Chrome controls do not touch passwords or Selenium sessions, strictly executing static URLs.

## Automated Windows Startup
You can configure NOVA to automatically boot your Chrome profile when you log into Windows!

### Manual Startup Test
To test the workflow without installing it:
```powershell
powershell -ExecutionPolicy Bypass -File .\scripts\test_startup.ps1
```

### Install Automatic Startup
To create a Windows Task Scheduler trigger for your current user:
```powershell
powershell -ExecutionPolicy Bypass -File .\scripts\install_startup.ps1
```

### Check Startup Status
To view whether the task is ready or running:
```powershell
powershell -ExecutionPolicy Bypass -File .\scripts\status_startup.ps1
```

### Remove Automatic Startup
To cleanly delete the Task Scheduler event:
```powershell
powershell -ExecutionPolicy Bypass -File .\scripts\uninstall_startup.ps1
```

## Testing
To run the included unit tests:
```powershell
pytest tests/
```
Tests safely mock all system APIs and do not trigger actual browsers.
