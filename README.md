# 🚀 Tdd Bdd Final Project

> Professional Python project implementing Tdd Bdd Final Project

[![Python](https://img.shields.io/badge/Python-3.12-3776AB.svg)](https://img.shields.io/badge/)
[![Docker](https://img.shields.io/badge/Docker-Ready-2496ED.svg)](https://img.shields.io/badge/)
[![Flask](https://img.shields.io/badge/Flask-3.0-000000.svg)](https://img.shields.io/badge/)
[![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-2.0-D71F00.svg)](https://img.shields.io/badge/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Docker](https://img.shields.io/badge/Docker-Ready-2496ED.svg?logo=docker)](Dockerfile)

[English](#english) | [Português](#português)

---

## English

### 🎯 Overview

**Tdd Bdd Final Project** is a production-grade Python application complemented by CSS, HTML, JavaScript, Shell that showcases modern software engineering practices including clean architecture, comprehensive testing, containerized deployment, and CI/CD readiness.

The codebase comprises **2,550 lines** of source code organized across **27 modules**, following industry best practices for maintainability, scalability, and code quality.

### ✨ Key Features

- **🐳 Containerized**: Docker support for consistent deployment
- **🏗️ Object-Oriented**: 7 core classes with clean architecture
- **📐 Clean Architecture**: Modular design with clear separation of concerns
- **🧪 Test Coverage**: Unit and integration tests for reliability
- **📚 Documentation**: Comprehensive inline documentation and examples
- **🔧 Configuration**: Environment-based configuration management

### 🏗️ Architecture

```mermaid
graph TB
    subgraph Client["🖥️ Client Layer"]
        A[Web Client]
        B[API Documentation]
    end
    
    subgraph API["⚡ API Layer"]
        C[Middleware Pipeline]
        D[Route Handlers]
        E[Business Logic]
    end
    
    subgraph Data["💾 Data Layer"]
        F[(Primary Database)]
        G[Cache]
    end
    
    A --> C
    B --> C
    C --> D --> E
    E --> F
    E --> G
    
    style Client fill:#e1f5fe
    style API fill:#f3e5f5
    style Data fill:#fff3e0
```

```mermaid
classDiagram
    class Product
    class Category
    class ProductFactory
    class DataValidationError
```

### 🚀 Quick Start

#### Prerequisites

- Python 3.12+
- pip (Python package manager)
- Docker and Docker Compose (optional)

#### Installation

```bash
# Clone the repository
git clone https://github.com/galafis/tdd-bdd-final-project.git
cd tdd-bdd-final-project

# Create and activate virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

#### Running

```bash
# Run the application
python src/main.py
```

### 🐳 Docker

```bash
# Build the Docker image
docker build -t tdd-bdd-final-project .

# Run the container
docker run -d -p 8000:8000 --name tdd-bdd-final-project tdd-bdd-final-project

# View logs
docker logs -f tdd-bdd-final-project

# Stop and remove
docker stop tdd-bdd-final-project && docker rm tdd-bdd-final-project
```

### 🧪 Testing

```bash
# Run all tests
pytest

# Run with coverage report
pytest --cov --cov-report=html

# Run specific test module
pytest tests/test_main.py -v

# Run with detailed output
pytest -v --tb=short
```

### 📁 Project Structure

```
tdd-bdd-final-project/
├── bin/
│   └── setup.sh
├── features/
│   ├── steps/
│   │   ├── load_steps.py
│   │   └── web_steps.py
│   └── environment.py
├── service/
│   ├── common/
│   │   ├── __init__.py
│   │   ├── cli_commands.py
│   │   ├── error_handlers.py
│   │   ├── log_handlers.py
│   │   └── status.py
│   ├── static/
│   │   ├── css/
│   │   ├── images/
│   │   └── js/
│   ├── __init__.py
│   ├── config.py
│   ├── models.py
│   └── routes.py
├── tests/         # Test suite
│   ├── __init__.py
│   ├── factories.py
│   ├── test_cli_commands.py
│   ├── test_models.py
│   └── test_routes.py
├── Dockerfile
├── LICENSE
├── Makefile
├── README.md
├── requirements.txt
└── setup.cfg
```

### 🛠️ Tech Stack

| Technology | Description | Role |
|------------|-------------|------|
| **Python** | Core Language | Primary |
| **Docker** | Containerization platform | Framework |
| **Flask** | Lightweight web framework | Framework |
| **SQLAlchemy** | SQL toolkit and ORM | Framework |
| CSS | 5 files | Supporting |
| JavaScript | 3 files | Supporting |
| Shell | 1 files | Supporting |
| HTML | 1 files | Supporting |

### 🚀 Deployment

#### Cloud Deployment Options

The application is containerized and ready for deployment on:

| Platform | Service | Notes |
|----------|---------|-------|
| **AWS** | ECS, EKS, EC2 | Full container support |
| **Google Cloud** | Cloud Run, GKE | Serverless option available |
| **Azure** | Container Instances, AKS | Enterprise integration |
| **DigitalOcean** | App Platform, Droplets | Cost-effective option |

```bash
# Production build
docker build -t tdd-bdd-final-project:latest .

# Tag for registry
docker tag tdd-bdd-final-project:latest registry.example.com/tdd-bdd-final-project:latest

# Push to registry
docker push registry.example.com/tdd-bdd-final-project:latest
```

### 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request. For major changes, please open an issue first to discuss what you would like to change.

1. Fork the project
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

### 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

### 👤 Author

**Gabriel Demetrios Lafis**
- GitHub: [@galafis](https://github.com/galafis)
- LinkedIn: [Gabriel Demetrios Lafis](https://linkedin.com/in/gabriel-demetrios-lafis)

---

## Português

### 🎯 Visão Geral

**Tdd Bdd Final Project** é uma aplicação Python de nível profissional, complementada por CSS, HTML, JavaScript, Shell que demonstra práticas modernas de engenharia de software, incluindo arquitetura limpa, testes abrangentes, implantação containerizada e prontidão para CI/CD.

A base de código compreende **2,550 linhas** de código-fonte organizadas em **27 módulos**, seguindo as melhores práticas do setor para manutenibilidade, escalabilidade e qualidade de código.

### ✨ Funcionalidades Principais

- **🐳 Containerized**: Docker support for consistent deployment
- **🏗️ Object-Oriented**: 7 core classes with clean architecture
- **📐 Clean Architecture**: Modular design with clear separation of concerns
- **🧪 Test Coverage**: Unit and integration tests for reliability
- **📚 Documentation**: Comprehensive inline documentation and examples
- **🔧 Configuration**: Environment-based configuration management

### 🏗️ Arquitetura

```mermaid
graph TB
    subgraph Client["🖥️ Client Layer"]
        A[Web Client]
        B[API Documentation]
    end
    
    subgraph API["⚡ API Layer"]
        C[Middleware Pipeline]
        D[Route Handlers]
        E[Business Logic]
    end
    
    subgraph Data["💾 Data Layer"]
        F[(Primary Database)]
        G[Cache]
    end
    
    A --> C
    B --> C
    C --> D --> E
    E --> F
    E --> G
    
    style Client fill:#e1f5fe
    style API fill:#f3e5f5
    style Data fill:#fff3e0
```

### 🚀 Início Rápido

#### Prerequisites

- Python 3.12+
- pip (Python package manager)
- Docker and Docker Compose (optional)

#### Installation

```bash
# Clone the repository
git clone https://github.com/galafis/tdd-bdd-final-project.git
cd tdd-bdd-final-project

# Create and activate virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

#### Running

```bash
# Run the application
python src/main.py
```

### 🐳 Docker

```bash
# Build the Docker image
docker build -t tdd-bdd-final-project .

# Run the container
docker run -d -p 8000:8000 --name tdd-bdd-final-project tdd-bdd-final-project

# View logs
docker logs -f tdd-bdd-final-project

# Stop and remove
docker stop tdd-bdd-final-project && docker rm tdd-bdd-final-project
```

### 🧪 Testing

```bash
# Run all tests
pytest

# Run with coverage report
pytest --cov --cov-report=html

# Run specific test module
pytest tests/test_main.py -v

# Run with detailed output
pytest -v --tb=short
```

### 📁 Estrutura do Projeto

```
tdd-bdd-final-project/
├── bin/
│   └── setup.sh
├── features/
│   ├── steps/
│   │   ├── load_steps.py
│   │   └── web_steps.py
│   └── environment.py
├── service/
│   ├── common/
│   │   ├── __init__.py
│   │   ├── cli_commands.py
│   │   ├── error_handlers.py
│   │   ├── log_handlers.py
│   │   └── status.py
│   ├── static/
│   │   ├── css/
│   │   ├── images/
│   │   └── js/
│   ├── __init__.py
│   ├── config.py
│   ├── models.py
│   └── routes.py
├── tests/         # Test suite
│   ├── __init__.py
│   ├── factories.py
│   ├── test_cli_commands.py
│   ├── test_models.py
│   └── test_routes.py
├── Dockerfile
├── LICENSE
├── Makefile
├── README.md
├── requirements.txt
└── setup.cfg
```

### 🛠️ Stack Tecnológica

| Tecnologia | Descrição | Papel |
|------------|-----------|-------|
| **Python** | Core Language | Primary |
| **Docker** | Containerization platform | Framework |
| **Flask** | Lightweight web framework | Framework |
| **SQLAlchemy** | SQL toolkit and ORM | Framework |
| CSS | 5 files | Supporting |
| JavaScript | 3 files | Supporting |
| Shell | 1 files | Supporting |
| HTML | 1 files | Supporting |

### 🚀 Deployment

#### Cloud Deployment Options

The application is containerized and ready for deployment on:

| Platform | Service | Notes |
|----------|---------|-------|
| **AWS** | ECS, EKS, EC2 | Full container support |
| **Google Cloud** | Cloud Run, GKE | Serverless option available |
| **Azure** | Container Instances, AKS | Enterprise integration |
| **DigitalOcean** | App Platform, Droplets | Cost-effective option |

```bash
# Production build
docker build -t tdd-bdd-final-project:latest .

# Tag for registry
docker tag tdd-bdd-final-project:latest registry.example.com/tdd-bdd-final-project:latest

# Push to registry
docker push registry.example.com/tdd-bdd-final-project:latest
```

### 🤝 Contribuindo

Contribuições são bem-vindas! Sinta-se à vontade para enviar um Pull Request.

### 📄 Licença

Este projeto está licenciado sob a Licença MIT - veja o arquivo [LICENSE](LICENSE) para detalhes.

### 👤 Autor

**Gabriel Demetrios Lafis**
- GitHub: [@galafis](https://github.com/galafis)
- LinkedIn: [Gabriel Demetrios Lafis](https://linkedin.com/in/gabriel-demetrios-lafis)
