from typing import Optional
from pydantic import BaseModel


class Candidato(BaseModel):
    id: Optional[int] = None
    cargo: str
    nome: str
    votos: int
    porcentagem_votos: float