# main.py
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routers import health, agent, startup, browser, network, applications, logs

app = FastAPI(title="NOVA Backend", description="Local API for NOVA startup agent")

# Local CORS configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "http://127.0.0.1:3000", "http://localhost:5173", "http://127.0.0.1:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(health.router, prefix="/api")
app.include_router(agent.router, prefix="/api")
app.include_router(startup.router, prefix="/api")
app.include_router(browser.router, prefix="/api")
app.include_router(network.router, prefix="/api")
app.include_router(applications.router, prefix="/api")
app.include_router(logs.router, prefix="/api")

@app.on_event("startup")
async def startup_event():
    # Placeholder for initializing services
    pass
