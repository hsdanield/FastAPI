from typing import Optional
from pydantic import BaseModel, validator


class Candidato(BaseModel):
    id: Optional[int] = None
    cargo: str
    nome: str
    votos: int
    porcentagem_votos: float

    
    @validator("nome")
    def validarNome(cls, value: str):
        palavras = value.split(" ")
    
        #Verificando se o NOME tem pelo menos 2 palavras
        if len(palavras) == 1:
            raise ValueError("O Nome deve ter pelo menos 2 palavras.")

        #Verificando se o NOME começa com letra maiuscula
        verificar_comeco_letra_minuscula = [palavra[0].islower() for palavra in palavras]
        if True in verificar_comeco_letra_minuscula:
            raise ValueError("O nome deve começar com Letra Maiuscula")

        return value