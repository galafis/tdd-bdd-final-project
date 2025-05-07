# Projeto Final TDD / BDD: Microsserviço de Catálogo de Produtos

Este repositório contém o projeto final desenvolvido para o curso **Introdução a TDD/BDD**, demonstrando a aplicação de Test Driven Development (TDD) e Behavior Driven Development (BDD) na criação de um microsserviço de backend para um catálogo de produtos de uma aplicação de eCommerce.

## Visão Geral do Projeto

O objetivo deste projeto é criar um microsserviço robusto e bem testado que gerencia um catálogo de produtos. Administradores podem utilizar uma interface de UI (não inclusa neste backend) para manter o catálogo, interagindo com as funcionalidades expostas por este serviço.

O microsserviço foi desenvolvido em Python utilizando o framework Flask e SQLAlchemy para persistência de dados. Foram implementadas funcionalidades CRUD (Create, Read, Update, Delete) para produtos, além de listagens e buscas por nome, categoria e disponibilidade.

Um novo campo `image_url` foi adicionado ao modelo de `Product` para permitir o armazenamento de URLs de imagens dos produtos.

## Funcionalidades Implementadas

O microsserviço de catálogo de produtos suporta as seguintes operações:

*   **Criar Produto:** Adicionar um novo produto ao catálogo.
*   **Ler Produto:** Obter detalhes de um produto específico pelo seu ID.
*   **Atualizar Produto:** Modificar informações de um produto existente.
*   **Deletar Produto:** Remover um produto do catálogo.
*   **Listar Todos os Produtos:** Obter uma lista de todos os produtos cadastrados.
*   **Listar Produtos por Nome:** Buscar produtos que correspondam a um nome específico.
*   **Listar Produtos por Categoria:** Filtrar produtos por sua categoria.
*   **Listar Produtos por Disponibilidade:** Filtrar produtos com base em sua disponibilidade.

## Tecnologias e Práticas Utilizadas

*   **Python:** Linguagem de programação principal.
*   **Flask:** Microframework web para desenvolvimento da API RESTful.
*   **SQLAlchemy:** ORM para interação com o banco de dados (configurado para SQLite em ambiente de teste e PostgreSQL para produção).
*   **TDD (Test Driven Development):** Desenvolvimento orientado a testes unitários utilizando `pytest` e `unittest`.
*   **BDD (Behavior Driven Development):** Desenvolvimento orientado a comportamento utilizando `behave` (arquivos de feature e steps não foram o foco desta intervenção, mas a estrutura está presente).
*   **Coverage:** Análise de cobertura de testes para garantir a qualidade do código.
*   **Git & GitHub:** Controle de versão e hospedagem do repositório.

## Configuração e Execução

1.  **Clone o repositório:**
    ```bash
    git clone https://github.com/galafis/tdd-bdd-final-project.git
    cd tdd-bdd-final-project
    ```

2.  **Crie e ative um ambiente virtual (recomendado):**
    ```bash
    python3 -m venv .venv
    source .venv/bin/activate
    ```

3.  **Instale as dependências:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Execute os testes (para verificar a configuração e funcionalidade):**
    ```bash
    python -m pytest --cov=service
    ```
    Os testes são configurados para rodar com um banco de dados SQLite em memória.

5.  **Para executar o serviço localmente (requer configuração de um banco de dados PostgreSQL ou ajuste no `service/config.py` para SQLite):**
    ```bash
    flask run
    ```
    Por padrão, o serviço tentará se conectar a um PostgreSQL em `postgresql://postgres:postgres@localhost:5432/postgres`. Para desenvolvimento e testes mais simples, você pode alterar a `DATABASE_URI` em `service/config.py` para `sqlite:///products.db`.

## Estrutura do Projeto

*   `service/`: Contém a lógica principal do microsserviço.
    *   `models.py`: Define os modelos de dados (ex: `Product`, `Category`) e interações com o banco.
    *   `routes.py`: Define as rotas da API e a lógica de cada endpoint.
    *   `common/`: Módulos utilitários (handlers de erro, logs, etc.).
    *   `__init__.py`: Inicialização da aplicação Flask.
    *   `config.py`: Configurações da aplicação.
*   `tests/`: Contém os testes unitários.
    *   `test_models.py`: Testes para os modelos de dados.
    *   `test_routes.py`: Testes para as rotas da API.
    *   `factories.py`: Fábricas para geração de dados de teste.
*   `features/`: Contém os arquivos para testes BDD (cenários e steps).
    *   `products.feature`: Cenários de BDD para as funcionalidades dos produtos.
    *   `steps/`: Implementação dos steps dos cenários BDD.
*   `requirements.txt`: Lista de dependências Python do projeto.
*   `README.md`: Este arquivo.
*   `LICENSE`: Licença do projeto (Apache License 2.0).
*   `.gitignore`: Especifica arquivos e diretórios a serem ignorados pelo Git.

## Licença

Distribuído sob a Licença Apache 2.0. Veja `LICENSE` para mais informações.

## Autor Original do Template

John Rofrano, Senior Technical Staff Member, DevOps Champion, @ IBM Research

---

Este README foi atualizado para refletir as modificações e o estado atual do projeto como um microsserviço de catálogo de produtos funcional e testado.

