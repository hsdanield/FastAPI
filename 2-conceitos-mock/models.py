from typing import Optional
from pydantic import BaseModel



class Eleicao(BaseModel):
    id: Optional[int] = None
    cargo: str
    votos: int
    porcentagem_votos: float