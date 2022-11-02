from typing import List, Optional
from xml.dom import INVALID_CHARACTER_ERR

from fastapi import FastAPI
from fastapi import HTTPException
from fastapi import status

from fastapi.responses import JSONResponse
from fastapi.responses import Response

from fastapi import Path
from fastapi import Query
from fastapi import Header

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
# gt=0 :: maior que 0
# let=3 :: menor que 3
async def get_candidato(id: int = Path(default=None, title="ID do curso", description="Deve ser 1 ou 2", gt=0, lt=3)):
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
        return Response(status_code=status.HTTP_204_NO_CONTENT)
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail={"msg": f"Candidato não encontrado. {id}"})


@app.get("/calcularVotos")
async def calcular(id_1: int = Query(default=1, gt=0),
                   id_2: int = Query(default=2, gt=0),
                   id_3: Optional[int] = Query(default=None, gt=0),
                   classe: str = Header(default=None)):

    total_votos: int = candidatos[id_1]["votos"] + candidatos[id_2]["votos"]
    if id_3:
        total_votos += id_3

    print(f"classe: {classe}")

    return {"total_votos": total_votos}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("main:app", host="127.0.0.1", port=8000,
                log_level="info", reload=True)
