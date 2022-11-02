from typing import Any, Dict, List, Optional, final

from fastapi import Depends, FastAPI
from fastapi import HTTPException
from fastapi import status

from fastapi.responses import JSONResponse
from fastapi.responses import Response

from fastapi import Path
from fastapi import Query
from fastapi import Header

from time import sleep

from models import Candidato


def simulacao_db():
    try:
        print("Abrindo conexão com banco de dados")
        sleep(1)
    finally:
        print("Fechando conexão com banco de dados")
        sleep(1)


candidatos = [
    Candidato(id=1, nome="Lula Silva", cargo="Presidente",
              votos=60345999, porcentagem_votos=50.90),
    Candidato(id=2, nome="Jair Bolsonaro", cargo="Presidente",
              votos=60345999, porcentagem_votos=50.90)
]


app = FastAPI(title="Conceitos FastAPI com dados Mocados",
              version="0.0.1",
              description="Estudo de conceitos FastAPI com padrão REST com dados mocados utilizando metodos HTTP's (GET, POST, PUT, DELETE)")


@app.get("/candidatos",
         summary="Retorna os Candidatos",
         description="Retorna Todos os Candidatos Registrados",
         response_model=List[Candidato],
         response_description="Candidatos Encontrados com Sucesso")
async def get_candidatos(db: Any = Depends(simulacao_db)):
    return candidatos


@ app.get("/candidatos/{id}")
# gt=0 :: maior que 0
# let=3 :: menor que 3
async def get_candidato(id: int = Path(default=None, title="ID do curso",
                                       description="Deve ser 1 ou 2", gt=0, lt=4),
                        db: Any = Depends(simulacao_db)):
    try:
        candidato = [
            candidato for candidato in candidatos if candidato.id == id]
        return candidato
    except KeyError:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail={"msg": f"Candidato não encontrado. {id}"})


@ app.post("/candidatos", status_code=status.HTTP_201_CREATED, response_model=Candidato)
async def post_candidato(candidato: Candidato, db: Any = Depends(simulacao_db)):
    next_id: int = len(candidatos) + 1
    candidato.id = next_id
    candidatos.append(candidato)
    return candidato


@ app.put("/candidatos/{id}")
async def put_candidato(id: int, candidato: Candidato, db: Any = Depends(simulacao_db)):
    if id in candidatos:
        del candidato.id
        candidatos[id] = candidato
        return candidato
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail={"msg": f"Candidato não encontrado. {id}"})


@ app.delete("/candidatos/{id}")
async def delete_candidato(id: int, db: Any = Depends(simulacao_db)):
    if id in candidatos:
        del candidatos[id]
        # return JSONResponse(status_code = status.HTTP_204_NO_CONTENT)
        return Response(status_code=status.HTTP_204_NO_CONTENT)
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail={"msg": f"Candidato não encontrado. {id}"})


@ app.get("/calcularVotos")
async def calcular(id_1: int = Query(default=1, gt=0),
                   id_2: int = Query(default=2, gt=0),
                   id_3: Optional[int] = Query(default=None, gt=0),
                   classe: str = Header(default=None),
                   db: Any = Depends(simulacao_db)):

    total_votos: int = candidatos[id_1]["votos"] + candidatos[id_2]["votos"]
    if id_3:
        total_votos += id_3

    print(f"classe: {classe}")

    return {"total_votos": total_votos}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("main:app", host="127.0.0.1", port=8000,
                log_level="info", reload=True)
