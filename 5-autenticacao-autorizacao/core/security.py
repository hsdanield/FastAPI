from passlib.context import CryptContext

CRIPTO = CryptContext(schemes=["bcrypt"], deprecated="auto")


def verificar_senha(senha: str, hash_senha: str) -> bool:
    """
    Função de verificação de senha, comparando a senha em texto, e o hash
    que esta salvo no banco de dados.
    """
    return CRIPTO.verify(senha, hash_senha)


def gerar_hash_senha(senha: str) -> str:
    """
    Função que gera e retorna o hash da senha
    """
    return CRIPTO.hash(senha)
