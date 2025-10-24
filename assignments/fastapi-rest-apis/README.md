# 📘 Assignment: Construindo APIs REST com FastAPI

## 🎯 Objective

Nesta tarefa, você aprenderá a construir APIs REST modernas e eficientes usando o framework FastAPI. Você criará uma API completa para gerenciar uma lista de tarefas (To-Do List), implementando operações CRUD (Create, Read, Update, Delete) e documentação automática.

## 📝 Tasks

### 🛠️	Configurar o Ambiente FastAPI

#### Description
Configure o ambiente de desenvolvimento e crie a estrutura básica de uma aplicação FastAPI. Você instalará as dependências necessárias e criará o arquivo principal da aplicação.

#### Requirements
Completed program should:

- Instalar FastAPI e Uvicorn usando pip
- Criar um arquivo `main.py` com uma aplicação FastAPI básica
- Implementar um endpoint de teste (`/` ou `/health`) que retorne uma mensagem de boas-vindas
- Executar a aplicação localmente e verificar se está funcionando


### 🛠️	Implementar Modelo de Dados

#### Description
Crie os modelos de dados usando Pydantic para representar as tarefas da To-Do List. Defina a estrutura dos dados que serão manipulados pela API.

#### Requirements
Completed program should:

- Criar um modelo Pydantic `Task` com campos: id, title, description, completed, created_at
- Implementar validação de dados usando tipos apropriados
- Criar uma lista em memória para armazenar as tarefas
- Adicionar algumas tarefas de exemplo para teste


### 🛠️	Criar Endpoints CRUD

#### Description
Implemente os endpoints da API REST para realizar operações CRUD nas tarefas. Cada endpoint deve seguir as convenções REST e retornar respostas apropriadas.

#### Requirements
Completed program should:

- `GET /tasks` - Listar todas as tarefas
- `GET /tasks/{task_id}` - Obter uma tarefa específica por ID
- `POST /tasks` - Criar uma nova tarefa
- `PUT /tasks/{task_id}` - Atualizar uma tarefa existente
- `DELETE /tasks/{task_id}` - Deletar uma tarefa
- Implementar tratamento de erros e códigos de status HTTP apropriados
- Validar dados de entrada usando modelos Pydantic


### 🛠️	Adicionar Documentação e Testes

#### Description
Aproveite a documentação automática do FastAPI e teste todos os endpoints da API. FastAPI gera automaticamente documentação interativa que pode ser acessada através do navegador.

#### Requirements
Completed program should:

- Acessar a documentação automática em `/docs` (Swagger UI)
- Testar todos os endpoints usando a interface Swagger
- Adicionar descrições e exemplos aos endpoints usando docstrings
- Verificar se todas as operações CRUD funcionam corretamente
- Documentar como executar e testar a aplicação no README