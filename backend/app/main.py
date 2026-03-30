from fastapi import FastAPI

app = FastAPI(
    title="HELM API",
    description="Holistic Effect & Level Meter — カードバランス予測API",
    version="0.1.0",
)


@app.get("/api/health")
async def health_check():
    return {"status": "ok"}
