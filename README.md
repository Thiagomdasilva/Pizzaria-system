🍕 Pizzaria System

Sistema de gerenciamento de pedidos para uma pizzaria
⸻

Autor

Thiago Marinho da Silva

Matrícula: 202322140

Curso: Engenharia de Software

⸻

Descrição

O Pizzaria System é uma aplicação Full Stack desenvolvida para realizar o gerenciamento completo de pedidos de uma pizzaria.

A aplicação possui uma arquitetura organizada baseada em princípios de Engenharia de Software e utiliza:

* React
* FastAPI
* MySQL
* Bootstrap
* Axios
* Docker
* Testes automatizados

⸻

Funcionalidades

Cadastro de pedidos

Permite registrar:

* Cliente
* Pizza escolhida
* Quantidade

⸻

Listagem de pedidos

Exibe todos os pedidos cadastrados.

⸻

Busca de pedidos

Permite localizar pedidos rapidamente.

⸻

Edição de pedidos

Atualiza os dados de pedidos já cadastrados.

⸻

Exclusão de pedidos

Remove pedidos do sistema com confirmação.

⸻

Dashboard

Apresenta informações resumidas dos pedidos cadastrados.

⸻

Sistema de Login

Controle de acesso do usuário.

⸻

Notificações

Mensagens de sucesso e erro para melhor experiência do usuário.

⸻

API REST

Endpoints:

* GET
* POST
* PUT
* DELETE

⸻

Testes Automatizados

Validação das funcionalidades principais do sistema.

⸻

Tecnologias Utilizadas

Frontend

* React
* Vite
* Bootstrap
* Axios
* React Icons

Backend

* Python
* FastAPI
* SQLAlchemy
* Pydantic
* Uvicorn

Banco de Dados

* MySQL

Ferramentas

* Docker
* Docker Compose
* Git
* GitHub

⸻

Arquitetura

O backend foi organizado utilizando conceitos de:

* Domain
* Use Cases
* Repository Pattern
* Factory Pattern
* Services
* Entities
* Interfaces

Estrutura principal:

backend/
├── api
├── domain
├── factories
├── infrastructure
├── repositories
├── schemas
├── services
├── tests
└── use_cases
frontend/
├── components
├── pages
└── services

⸻

Como executar

Backend

cd backend
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
uvicorn main:app --reload

Servidor:

http://localhost:8000

⸻

Frontend

cd frontend
npm install
npm run dev

Aplicação:

http://localhost:5173

⸻

Docker

Executar:

docker-compose up --build

⸻

Objetivos do Projeto

Este sistema foi desenvolvido para aplicar conceitos de:

* Engenharia de Software
* Desenvolvimento Full Stack
* APIs REST
* React
* FastAPI
* Banco de Dados
* Arquitetura em Camadas
* Padrões de Projeto
* Testes Automatizados

⸻

Resultado

O projeto entrega uma solução completa para gerenciamento de pedidos de uma pizzaria, permitindo cadastrar, consultar, editar e excluir pedidos através de uma interface moderna integrada a uma API desenvolvida em FastAPI.

⸻

Desenvolvido por

Thiago Marinho da Silva

Matrícula: 202322140

Engenharia de Software