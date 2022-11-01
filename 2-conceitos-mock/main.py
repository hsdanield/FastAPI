from typing import List, Optional

from distutils.log import debug
from fastapi import FastAPI
from fastapi import HTTPException
from fastapi import status

from fastapi.responses import JSONResponse
from fastapi.responses import Response

from models import Candidato

app = FastAPI()

candidatos = {
    1: {
        "nome": "Lula",
        "cargo": "Presidente",
        "votos": 60345999,
        "porcentagem_votos": 50.90,
    },

    2: {
        "nome": "Bolsonaro",
        "cargo": "Presidente",
        "votos": 58206354,
        "porcentagem_votos": 49.10
    },

}


@app.get("/candidatos")
async def get_candidatos():
    return candidatos


@app.get("/candidatos/{id}")
async def get_candidato(id: int):
    try:
        return candidatos[id]
    except KeyError:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail={"msg": f"Candidato não encontrado. {id}"})


@app.post("/candidatos", status_code=status.HTTP_201_CREATED)
async def post_candidato(candidato: Candidato):
    next_id: int = len(candidatos) + 1
    del candidato.id
    candidatos[next_id] = candidato
    return candidato


@app.put("/candidatos/{id}")
async def put_candidato(id: int, candidato: Candidato):
    if id in candidatos:
        del candidato.id
        candidatos[id] = candidato
        return candidato
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail={"msg": f"Candidato não encontrado. {id}"})


@app.delete("/candidatos/{id}")
async def delete_candidato(id: int):
    if id in candidatos:
        del candidatos[id]
        # return JSONResponse(status_code = status.HTTP_204_NO_CONTENT)
        return Response(status_code = status.HTTP_204_NO_CONTENT)
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail={"msg": f"Candidato não encontrado. {id}"})


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("main:app", host="127.0.0.1", port=8000,
                log_level="info", reload=True)
