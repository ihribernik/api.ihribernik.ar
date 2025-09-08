# 📝 Blog API with FastAPI + Hexagonal Architecture (blog.ihribernik.ar)

This project demonstrates a **modern architecture** for building a blog API using **FastAPI**, applying **Clean Code** principles and **Hexagonal Architecture (Ports & Adapters)**.

---

## 🏛️ Architecture Overview

This project implements a **Hexagonal Architecture** (also known as Ports and Adapters) with Clean Architecture principles. The architecture is organized in concentric layers, each with a specific responsibility:

### Core Layers

1. **Domain Layer** (`app/domain/`)
   - Heart of the application
   - Contains business logic and rules
   - Pure Python with no external dependencies
   - Components:
     - `models/`: Domain entities (Post, User, etc.)
     - `ports/`: Interface definitions
     - `services/`: Domain services and business rules
     - `exceptions/`: Custom domain exceptions

2. **Application Layer** (`app/application/`)
   - Orchestrates use cases
   - Coordinates domain objects
   - Implements application services
   - Manages transactions and workflows

3. **Infrastructure Layer** (`app/infrastructure/`)
   - Implements technical capabilities
   - Adapts external technologies
   - Components:
     - `web/`: FastAPI routes and controllers
     - `database/`: SQLAlchemy models and config
     - `repositories/`: Data access implementations
     - `auth/`: Authentication mechanisms

### Key Principles

1. **Dependency Rule**
   - Dependencies flow inward
   - Domain layer has no external dependencies
   - Outer layers depend on inner layers

2. **Interface Segregation**
   - Ports define clear contracts
   - Each port serves a single purpose
   - Adapters implement specific ports

3. **Domain-Driven Design**

## 🛠️ Environment Configuration

This project uses environment variables for configuration. To get started:

**Setting up environment variables**:

1. Copy the example environment file:

```bash
cp .env.example .env
```

2. Configure your environment:
   - Edit `.env` with your specific settings
   - Never commit `.env` to version control
   - Keep `.env.example` updated with new variables

### Available Configuration Options

| Variable | Description | Default |
|----------|-------------|---------|
| `SQLALCHEMY_DATABASE_URL` | Database connection URL | `sqlite:///./test.db` |
| `DEBUG` | Enable debug mode | `false` |
| `API_TITLE` | API title for docs | "Blog API" |
| `API_VERSION` | API version | "1.0.0" |
| `API_PREFIX` | API route prefix | "/api" |
| `CORS_ORIGINS` | Allowed CORS origins | `["http://localhost:3000"]` |
| `POSTGRES_*` | PostgreSQL settings | See `.env.example` |

### Database Configuration

For development, you can use SQLite:

```env
SQLALCHEMY_DATABASE_URL=sqlite:///./test.db
```

For production, use PostgreSQL:

```env
SQLALCHEMY_DATABASE_URL=postgresql://user:password@localhost:5432/dbname
```
   - Rich domain models
   - Encapsulated business rules
   - Ubiquitous language in code

## 🌟 Best Practices

### 1. Code Organization

- **Single Responsibility**: Each module, class, and function has one job
- **Dependency Injection**: Services receive their dependencies
- **Interface-Based Design**: Program to interfaces, not implementations

### 2. Error Handling

- **Domain Exceptions**: Custom exceptions for business rules
- **Global Error Handler**: Consistent API error responses
- **Typed Exceptions**: Clear error hierarchies

### 3. Data Access

- **Repository Pattern**: Abstracts data storage
- **Unit of Work**: Manages transactions
- **Domain Models**: Separate from ORM models

### 4. API Design

- **RESTful Principles**: Resource-based URLs
- **OpenAPI/Swagger**: Comprehensive API documentation
- **Input Validation**: Schema-based request validation

### 5. Testing

- **Layered Testing**: Unit, integration, and E2E tests
- **Test Isolation**: Independent test environments
- **Mocking**: Isolation from external dependencies

### 6. Configuration

- **Environment Variables**: External configuration
- **Settings Management**: Centralized config handling
- **Feature Flags**: Toggle features (coming soon)

---

## 📂 Estructura de carpetas

```bash
blog.ihribernik.ar/
├── app/                     # Código de la aplicación
│   ├── domain/              # Core del negocio (independiente del framework/infraestructura)
│   │   ├── models/          # Entidades (Post, User, Comment)
│   │   ├── services/        # Casos de uso / lógica de negocio
│   │   └── ports/           # Interfaces (repositorios, UoW, servicios externos)
│   │
│   ├── application/         # Orquestación de casos de uso
│   │   └── blog_service.py
│   │
│   ├── infrastructure/      # Adaptadores al mundo real
│   │   ├── repositories/    # SQLAlchemy, InMemory, etc.
│   │   ├── web/             # API FastAPI (controllers, routes)
│   │   ├── db/              # Modelos y config de SQLAlchemy / migrations
│   │   ├── auth/            # JWT, OAuth2, etc.
│   │   └── config.py
│   │
│   ├── main.py              # Entry point de FastAPI (ASGI app)
│   └── __init__.py
│
├── tests/                   # Pruebas
│   ├── unit/                # Tests unitarios (dominio puro)
│   ├── integration/         # Tests de integración con repos/db
│   └── e2e/                 # Tests end-to-end de la API
│
├── migrations/              # Archivos de Alembic para la DB
├── scripts/                 # Scripts de administración/devops
├── docker/                  # Configs dockerizadas (Dockerfile, compose, nginx, etc.)
├── .env                     # Variables de entorno (local/dev)
├── requirements.txt          # Dependencias de producción
├── requirements-dev.txt      # Dependencias de desarrollo
└── README.md
```

---


## 🛠️ Instalación

1. Cloná el repositorio:

   ```bash
   git clone https://github.com/tu-usuario/blog-flask-hexagonal.git
   cd blog-flask-hexagonal
   ```

2. Instala dependencias con [uv](https://github.com/astral-sh/uv) o pip:

   ```bash
   uv pip install -r requirements.txt
   ```

3. Set up your environment variables:

   ```bash
   cp .env.example .env
   # Edit .env with your configurations
   ```

4. Database Setup (Choose one):

   **Option 1: Using Docker (Recommended)**

   ```bash
   # Start PostgreSQL container
   docker-compose up -d postgres

   # Wait for the container to be healthy
   docker-compose ps
   ```

   **Option 2: Local PostgreSQL**
   - Install PostgreSQL on your system
   - Create a database named `blog_ihribernik`
   - Update `.env` with your database credentials

5. Initialize the database:

   ```bash
   # Apply migrations
   alembic upgrade head
   ```

---


## ▶️ Ejecución de la API

Iniciá la app de FastAPI con uvicorn:

```bash
uvicorn app.main:app --reload
```

La API quedará disponible en:

```bash
http://127.0.0.1:8000
```

---

## 📌 Available Endpoints

### Blog Posts

- `POST /api/posts` → Create a new post

  ```json
  {
    "title": "My first post",
    "content": "Post content",
    "author": "ivan"
  }
  ```

- `GET /api/posts` → List all posts
- `GET /api/posts/{id}` → Get a specific post by ID

All endpoints are documented in detail in the OpenAPI/Swagger documentation at `/docs` or ReDoc at `/redoc`.

---

## 🧪 Testing

The project uses **pytest** for comprehensive testing across multiple layers:

### Test Structure

- **Unit Tests** (`tests/unit/`):
  - Test domain logic in isolation
  - Mock external dependencies
  - Focus on business rules and use cases

- **Integration Tests** (`tests/integration/`):
  - Test repository implementations
  - Use test database
  - Verify database operations

- **End-to-End Tests** (`tests/e2e/`):
  - Test complete API flows
  - Use FastAPI TestClient
  - Verify HTTP responses and payloads

### Running Tests

1. Install test dependencies:

   ```bash
   uv pip install -r requirements-dev.txt
   ```

2. Run tests with coverage:

   ```bash
   # Run all tests
   pytest

   # Run specific test types
   pytest tests/unit         # Unit tests only
   pytest tests/integration  # Integration tests only
   pytest tests/e2e         # E2E tests only

   # Run with specific markers
   pytest -m unit           # Unit tests
   pytest -m integration    # Integration tests
   pytest -m e2e           # E2E tests

   # Show coverage report
   pytest --cov=app --cov-report=html
   ```

### Test Configuration

- **pytest.ini**: Defines test markers and coverage settings
- **conftest.py**: Provides shared fixtures
- **Coverage**: Minimum 80% code coverage required
- **Database**: Uses SQLite for testing (fast and isolated)

The test suite uses **SQLAlchemy** for integration tests and an **InMemoryRepository** for unit tests to maintain isolation.

---

## 🌟 Features

- ✅ Clean Architecture with Domain-Driven Design
- ✅ FastAPI with modern Python type hints
- ✅ SQLAlchemy for database operations
- ✅ Comprehensive test suite
- ✅ API documentation with OpenAPI/Swagger
- ✅ Error handling middleware
- ✅ CORS configuration
- ✅ Database migrations with Alembic

## 🔮 Roadmap

- [ ] Authentication (JWT)
- [ ] User management
- [ ] Comments system
- [ ] PostgreSQL implementation
- [ ] Caching layer
- [ ] Rate limiting
- [ ] API versioning

---

## 📖 Recursos recomendados

- [Arquitectura Hexagonal explicada](https://alistair.cockburn.us/hexagonal-architecture/)
- [Clean Architecture de Uncle Bob](https://blog.cleancoder.com/)

---

✨ Con esta estructura tu API es mantenible, extensible y fácil de testear.
