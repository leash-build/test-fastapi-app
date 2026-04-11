from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def root():
    return {"app": "test-fastapi-app", "status": "running"}


@app.get("/health")
def health():
    return {"healthy": True}
