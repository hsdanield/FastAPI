from fastapi import FastAPI
from fastapi import FastAPI

from routes import candidato, usuario

app = FastAPI()
app.include_router(candidato.router, tags=['candidatos'])
app.include_router(usuario.router, tags=['usuarios'])


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("main:app", host="127.0.0.1", port=8000,
                log_level="info", reload=True)
