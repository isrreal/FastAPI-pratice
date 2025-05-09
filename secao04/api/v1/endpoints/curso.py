from typing import List
from fastapi import APIRouter, status, Depends, HTTPException, Response

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from models.curso_model import CursoModel
from schemas.curso_schema import CursoSchema
from core.deps import get_session

router = APIRouter()

# POST Curso
@router.post('/', status_code=status.HTTP_201_CREATED, 
        response_model=CursoSchema,
        description='Envia um novo curso para cadastrar.', 
        summary="Cria um novo curso.", 
        response_description="Curso criado com sucesso." )
        
async def post_curso(curso: CursoSchema, db: AsyncSession = Depends(get_session)):
    novo_curso = CursoModel(titulo=curso.titulo, aulas=curso.aulas, horas=curso.horas)    
    db.add(novo_curso)
    await db.commit()
    
    return novo_curso

# GET Cursos
@router.get('/', response_model=List[CursoSchema],
        description='Retorna todos os cursos ou uma lista vazia.', 
        summary="Retorna todos os cursos.", 
        response_description="Cursos encontrados com sucesso.")
async def get_cursos(db: AsyncSession = Depends(get_session)):
    async with db as session:
        query = select(CursoModel)
        result = await session.execute(query)
        cursos: List[CursoModel] = result.scalars().all()
        
        return cursos 
    
# GET Curso
@router.get('/{curso_id}', response_model=CursoSchema, 
        status_code=status.HTTP_200_OK,
        description='Retorna o curso informado ou detalhamento de não encontrado.', 
        summary='Retorna o curso informado.', 
        response_description="Curso encontrado com sucesso.")

async def get_cursos(curso_id: int, db: AsyncSession = Depends(get_session)):
    async with db as session:
        query = select(CursoModel).filter(CursoModel.id == curso_id)
        result = await session.execute(query)
        curso = result.scalar_one_or_none()
        
        if curso:
            return curso
        else:
            raise HTTPException(detail="Curso não encontrado.", status_code=status.HTTP_404_NOT_FOUND)
        
# PUT Curso
@router.put('/{curso_id}', response_model=CursoSchema, 
        status_code=status.HTTP_202_ACCEPTED,
        description='Retorna os dados do curso informado para alteração ou curso não encontrado.', 
        summary='Altera o curso informado.', 
        response_description="Curso alterado com sucesso." )

async def put_curso(curso_id: int, curso: CursoSchema, db: AsyncSession = Depends(get_session)):
    async with db as session:
        query = select(CursoModel).filter(CursoModel.id == curso_id)
        result = await session.execute(query)
        curso_up = result.scalar_one_or_none()
        
        if curso_up:
            curso_up.titulo = curso.titulo
            curso_up.aulas =  curso.aulas
            curso_up.horas =  curso.horas
            
            await session.commit()
            
            return curso_up
        else:
            raise HTTPException(detail="Curso não encontrado.", status_code=status.HTTP_404_NOT_FOUND)
        
    
        
# DELETE Curso
@router.delete('/{curso_id}', status_code=status.HTTP_204_NO_CONTENT,
        description='Envia um curso para ser deletado.', 
        summary="Deleta o curso informado.",          
        response_description="Curso deletado com sucesso.")
async def delete_curso(curso_id: int, db: AsyncSession = Depends(get_session)):
    async with db as session:
        query = select(CursoModel).filter(CursoModel.id == curso_id)
        result = await session.execute(query)
        curso_del = result.scalar_one_or_none()
        
        if curso_del:
            await session.delete(curso_del)
            await session.commit()
                        
            return Response(status_code=status.HTTP_204_NO_CONTENT)
        else:
            raise HTTPException(detail="Curso não encontrado.", status_code=status.HTTP_404_NOT_FOUND)
