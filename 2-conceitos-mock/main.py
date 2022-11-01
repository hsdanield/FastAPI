from distutils.log import debug
from fastapi import FastAPI
from fastapi import HTTPException
from fastapi import status

app = FastAPI()

eleicoes = {
    1: {
        "titulo": "Lula",
        "cargo": "Presidente",
        "votos": 60345999,
        "porcentagem_votos": 50.90
    },

    2: {
        "titulo": "Bolsonaro",
        "cargo": "Presidente",
        "votos": 58206354,
        "porcentagem_votos": 49.10
    }
}


@app.get("/eleicoes")
async def get_eleicoes():
    return eleicoes

@app.get("/eleicoes/{id}")
async def get_eleicoes(id: int):
    try:
        return eleicoes[id]
    except KeyError:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail={"msg": "Candidato não encontrado."})



if __name__ == "__main__":
    import uvicorn

    uvicorn.run("main:app", host="127.0.0.1", port=8000,
                log_level="info", reload=True)
