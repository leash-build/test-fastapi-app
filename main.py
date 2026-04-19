from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

from leash import LeashAuthError, get_leash_user, is_authenticated

app = FastAPI()


@app.get("/")
def root():
    return {"app": "test-fastapi-app", "status": "running"}


@app.get("/health")
def health():
    return {"healthy": True}


@app.get("/me")
def me(request: Request):
    try:
        user = get_leash_user(request)
        return {
            "id": user.id,
            "email": user.email,
            "name": user.name,
            "picture": user.picture,
        }
    except LeashAuthError as exc:
        return JSONResponse(status_code=401, content={"error": str(exc)})


@app.get("/auth-status")
def auth_status(request: Request):
    return {"authenticated": is_authenticated(request)}
