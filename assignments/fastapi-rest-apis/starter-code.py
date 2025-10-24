"""
FastAPI To-Do List API - Starter Code
=====================================

Este é o código inicial para construir uma API REST com FastAPI.
Complete as tarefas seguindo as instruções no README.md.

Para executar:
1. Instale as dependências: pip install fastapi uvicorn
2. Execute: uvicorn main:app --reload
3. Acesse: http://localhost:8000/docs

"""

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime

# Criar a aplicação FastAPI
app = FastAPI(
    title="To-Do List API",
    description="Uma API REST simples para gerenciar tarefas",
    version="1.0.0"
)

# TODO: Implementar o modelo Pydantic para Task
class Task(BaseModel):
    id: int
    title: str
    description: Optional[str] = None
    completed: bool = False
    created_at: datetime

# TODO: Model para criar uma nova task (sem id e created_at)
class TaskCreate(BaseModel):
    title: str
    description: Optional[str] = None
    completed: bool = False

# TODO: Model para atualizar uma task
class TaskUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    completed: Optional[bool] = None

# Lista em memória para armazenar as tarefas
tasks_db: List[Task] = [
    Task(
        id=1,
        title="Aprender FastAPI",
        description="Estudar a documentação do FastAPI",
        completed=False,
        created_at=datetime.now()
    ),
    Task(
        id=2,
        title="Implementar API REST",
        description="Criar endpoints CRUD para tarefas",
        completed=False,
        created_at=datetime.now()
    )
]

# Contador para IDs únicos
next_id = 3

# Endpoint de teste / health check
@app.get("/")
async def root():
    """Endpoint de boas-vindas e health check."""
    return {"message": "Bem-vindo à To-Do List API!", "status": "online"}

# TODO: Implementar GET /tasks - Listar todas as tarefas
@app.get("/tasks", response_model=List[Task])
async def get_tasks():
    """Retorna todas as tarefas."""
    pass  # Substituir por implementação

# TODO: Implementar GET /tasks/{task_id} - Obter tarefa por ID
@app.get("/tasks/{task_id}", response_model=Task)
async def get_task(task_id: int):
    """Retorna uma tarefa específica por ID."""
    pass  # Substituir por implementação

# TODO: Implementar POST /tasks - Criar nova tarefa
@app.post("/tasks", response_model=Task, status_code=201)
async def create_task(task: TaskCreate):
    """Cria uma nova tarefa."""
    pass  # Substituir por implementação

# TODO: Implementar PUT /tasks/{task_id} - Atualizar tarefa
@app.put("/tasks/{task_id}", response_model=Task)
async def update_task(task_id: int, task_update: TaskUpdate):
    """Atualiza uma tarefa existente."""
    pass  # Substituir por implementação

# TODO: Implementar DELETE /tasks/{task_id} - Deletar tarefa
@app.delete("/tasks/{task_id}")
async def delete_task(task_id: int):
    """Deleta uma tarefa."""
    pass  # Substituir por implementação

# Função auxiliar para encontrar tarefa por ID
def find_task_by_id(task_id: int) -> Optional[Task]:
    """Encontra uma tarefa pelo ID."""
    for task in tasks_db:
        if task.id == task_id:
            return task
    return None

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)