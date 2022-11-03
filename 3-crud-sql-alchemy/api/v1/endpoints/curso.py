from typing import List

from fastapi import APIRouter
from fastapi import status
from fastapi import Depends
from fastapi import HTTPException
from fastapi import Response

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from models.curso_model import CursoModel
from schemas.curso_schema import CursoSchema
from core.deps import get_session

router = APIRouter()


# POST CURSO
@router.post("/", status_code=status.HTTP_201_CREATED, response_model=CursoSchema)
async def post_curso(curso: CursoSchema, db: AsyncSession = Depends(get_session)):

    novo_curso = CursoModel(
        titulo=curso.titulo,
        aulas=curso.aulas,
        horas=curso.horas
    )

    db.add(novo_curso)
    await db.commit()

    return CursoSchema(novo_curso)

# GET CURSOS
@router.get("/", response_model=List[CursoSchema])
async def get_cursos(db: AsyncSession = Depends(get_session)):
    async with db as session:
        query = select(CursoModel)
        result = await session.execute(query)
        cursos: List[CursoModel] = result.scalars().all()
        return cursos


# GET BY ID
@router.get("/{curso_id}", status_code=status.HTTP_200_OK, response_model=CursoSchema)
async def get_curso(curso_id: int, db: AsyncSession = Depends(get_session)):
    async with db as session:
        query = select(CursoModel).filter(CursoModel.id == curso_id)
        result = await session.execute(query)
        curso = result.scalar_one_or_none()

        if curso:
            return curso
        else:
            raise HTTPException(detail="Curso não encontrado.",
                                status_code=status.HTTP_404_NOT_FOUND)

# PUT CURSO


@router.put("/{id_curso}", status_code=status.HTTP_202_ACCEPTED, response_model=CursoSchema)
async def post_curso(curso_id: int, curso: CursoSchema, db: AsyncSession = Depends(get_session)):

    async with db as session:
        query = select(CursoModel).filter(CursoModel.id == curso_id)
        result = await session.execute(query)
        curso_model = result.scalar_one_or_none()

        if curso_model:
            curso_model.titulo = curso.titulo
            curso_model.aulas = curso.aulas
            curso_model.horas = curso.horas
            await session.commit()
            return curso_model
        else:
            raise HTTPException(detail="Curso não encontrado.",
                                status_code=status.HTTP_404_NOT_FOUND)


# DELETE CURSO
@router.delete("/{id_cruso}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_curso(curso_id: int, db: AsyncSession = Depends(get_session)):
    async with db as session:
        query = select(CursoModel).filter(CursoModel.id == curso_id)
        result = await session.execute(query)
        curso_model = result.scalar_one_or_none()

        if curso_model:
            await session.delete(curso_model)
            await session.commit()
            return Response(status_code=status.HTTP_204_NO_CONTENT)

        else:
            raise HTTPException(detail="Curso não encontrado.",
                                status_code=status.HTTP_404_NOT_FOUND)
