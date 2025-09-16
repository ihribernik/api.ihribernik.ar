# 🏗️ App Boilerplate (FastAPI + SQLAlchemy 2)

Este proyecto sigue una arquitectura **inspirada en DDD / Clean Architecture**, separando claramente dominio, aplicación, infraestructura y presentación.

---

## 📂 Estructura de directorios

```text
app/
├── core/                # Configuración y utilidades globales
│   ├── config.py
│   ├── logging.py
│   ├── dependencies.py
│   └── utils.py
│
├── domain/              # Entidades y lógica de negocio pura
│   ├── entities/
│   │   ├── user.py
│   │   ├── post.py
│   │   └── tag.py
│   ├── services/
│   │   └── auth_service.py
│   └── exceptions.py
│
├── application/         # Casos de uso y DTOs
│   ├── use_cases/
│   │   ├── create_post.py
│   │   └── register_user.py
│   └── dto/
│       ├── user_dto.py
│       └── post_dto.py
│
├── infrastructure/      # Adaptadores (ORM, repos, auth, etc.)
│   ├── orm/
│   │   ├── base.py
│   │   ├── user_orm.py
│   │   └── post_orm.py
│   ├── repositories/
│   │   └── user_repository.py
│   ├── mappers/
│   │   └── user_mapper.py
│   ├── auth/
│   │   └── jwt_service.py
│   └── database/
│       └── session.py
│
├── presentation/
│   ├── api/
│   │   ├── routes/
│   │   ├── error_handlers.py
│   │   └── middlewares/
│   │       ├── logging_middleware.py
│   │       ├── timing_middleware.py
│   │       └── auth_middleware.py (si aplica)
│   └── schemas/         # Pydantic schemas
        ├── user_schema.py
        └── post_schema.py
```

---

## ✅ Convenciones y buenas prácticas

### Domain

- Entidades son **puras** (`dataclasses` o `attrs`), sin herencia de ORM.
- Excepciones específicas (`DomainValidationError`, etc.) en `exceptions.py`.
- Services encapsulan reglas de negocio, no acceden directo a DB.

### Application

- Cada caso de uso en `application/use_cases/`.
- DTOs viven en `application/dto/` (sin Pydantic).
- Los casos de uso orquestan repositorios + servicios de dominio.

### Infrastructure

- Modelos ORM en `infrastructure/orm/`.
- Repositorios devuelven objetos de **dominio**, no ORM.
- Mappers manejan conversión ORM ↔ domain.
- `auth/` encapsula JWT y hashing de contraseñas.

### Presentation

- Routes organizadas por contexto en `routes/`.
- Schemas (Pydantic) en `schemas/`.
- `error_handlers.py` centraliza el manejo de excepciones.
- Uso de `Depends(get_current_user)` en endpoints protegidos.

### Core

- `config.py` usa **Pydantic BaseSettings** para variables de entorno.
- `logging.py` define formato y nivel de logs.
- `utils.py` contiene funciones reutilizables (`utc_now`, `slugify`, etc.).

---

## 🧪 Tests

La carpeta `tests/` refleja la estructura de `app/`:

- **Unit tests** → entidades y servicios de dominio.
- **Integration tests** → repositorios (DB de test).
- **E2E tests** → API con `TestClient`.

---

## 🚀 Run

```bash
# Crear entorno
python -m venv .venv
source .venv/bin/activate   # Linux/Mac
.venv\Scripts\activate      # Windows

# Instalar deps
pip install -r requirements.txt

# Migraciones (ejemplo con Alembic)
alembic upgrade head

# Correr server
uvicorn app.main:app --reload
```

---

## 📌 Pendientes / Roadmap

- [ ] Documentar convenciones de naming.
- [ ] Definir manejo de `created_at` / `updated_at` centralizado en DB.
- [ ] Añadir CI/CD básico.
- [ ] Contenedores con Docker.
