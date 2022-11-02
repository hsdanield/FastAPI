from fastapi import APIRouter

router = APIRouter()

@router.get("/api/v1/usuarios")
async def get_candidatos():
    return {"msg": "Rota Versao 1 para Usuario"}
