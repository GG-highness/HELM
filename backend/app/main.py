from fastapi import FastAPI

from app.core.database import check_db_connection

app = FastAPI(
    title="HELM API",
    description="Holistic Effect & Level Meter — カードバランス予測API",
    version="0.1.0",
)


@app.get("/api/health")
async def health_check():
    db_ok = check_db_connection()
    return {"status": "ok", "db": "connected" if db_ok else "disconnected"}
