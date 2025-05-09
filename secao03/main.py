from fastapi import FastAPI
from fastapi import HTTPException 
from fastapi import status 
from fastapi import Path
from fastapi import Query
from typing import Optional, Any, List
from models import Curso
from time import sleep
from fastapi import Depends

def fake_db():
    try:
        print("Abrindo conexão com o banco de dados")
        sleep(1)
    finally:
        print("Fechando conexão com o banco de dados...")
        sleep(1) 

app = FastAPI(title = "API do Curso de FastAPI",
              version = "0.1",
              description = "Essa é a descrição da minha API")

cursos = {
    1: { 
        "titulo": "Programação para Leigos",
        "aulas": 112,
        "horas": 58
    },
    
    2: { 
        "titulo": "Algoritmos e Lógica de Programação",
        "aulas": 87,
        "horas": 67 
    }
}

@app.get('/cursos', 
        description = "Retorna todos os cursos ou uma lista vazia",
        summary = "Retorna todos os cursos",
        response_model = List[Curso]
        )
async def get_cursos(db: Any = Depends(fake_db)):
    return cursos

@app.get('/cursos/{curso_id}')
async def get_curso(curso_id: int = Path(title = 'ID do curso', description = 'Deve ser entre 1 e 2', gt = 0, lt = 3)):
    try: 
        curso = cursos[curso_id]
        return curso
    except KeyError:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Curso não encontrado.')

@app.get('/calculadora')
async def calcular(
    a: int = Query(gt=5),
    b: int = Query(gt=10),
    c: Optional[int] = None
):
    soma = a + b
    if c is not None:
        soma += c
    return {"resultado": soma}    

@app.post('/cursos')
async def post_curso(curso: Curso, status_code = status.HTTP_201_CREATED):
    next_id: int = len(cursos) + 1
    cursos[next_id] = curso
    del curso.id
    return curso

@app.put('/cursos/{curso_id}')
async def put_curso(curso_id: int, curso: Curso):
    if curso_id in cursos: 
        cursos[curso_id] = curso
        del curso.id

        return curso
    else:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND,
                detail = f"Não existe curso com o identificador {curso_id}")

@app.delete('/cursos/{curso_id}')
async def delete_curso(curso_id: int):
    if curso_id in cursos:
        del cursos[curso_id]
        return Response(status_code=status.HTTP_209_NO_CONTENT)  # Sem conteúdo
    else:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Não existe curso com o identificador {curso_id}"
        )

if __name__ == '__main__':
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True) 
