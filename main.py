from fastapi import FastAPI
from fastapi import HTTPException


app = FastAPI(title="Docker Desktop K8s Lab version-3 hello world!")

@app.get("/")
def root():
    return {"msg": " nastya"}

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/crash")
def crash():
    import os
    os._exit(1)
    
@app.get("/slow")
def slow():
    import time
    time.sleep(2)
    return {"msg": "slow response"}

@app.get("/health1")
def health():
    raise HTTPException(status_code=500, detail="принудительная ошибка health для демонстрации probes")

@app.get("/memory")
def memory():
    chunk = "x" * (300 * 1024 * 1024)
    return {"allocated_bytes": len(chunk)}