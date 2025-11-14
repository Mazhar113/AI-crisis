from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers import reports, resources, alerts, dashboard, auth
from websocket.realtime import router as ws_router

app = FastAPI(title="Crisis Response & Coordination AI Map - Ultimate Live")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(reports.router)
app.include_router(resources.router)
app.include_router(alerts.router)
app.include_router(dashboard.router)
app.include_router(auth.router)
app.include_router(ws_router)
