# TODO - Alineación con Arquitectura Hexagonal / Clean Architecture

## Resumen rápido

- Objetivo: separar responsabilidades en Domain, Application (use-cases/puertos), Infrastructure (adaptadores) y Presentation (controllers), introducir Unit of Work, DTOs, composition root y cobertura de tests.
- Prioridad inicial: estabilizar puertos/DTOs + Unit of Work + centralizar DI + tests básicos.

### Prioridad Alta (hacer primero)

1. Introducir puertos de entrada (Use-cases) y DTOs

   - Archivos objetivo: app/application/services/_, app/presentation/api/routes/_.py
   - Tareas:
     - Crear interfaces de use-case (por ejemplo: CreatePostUseCase, GetPostUseCase).
     - Definir DTOs de entrada/salida (Application DTOs) separados de Pydantic (Presentation).
   - Criterio de aceptación: routers llaman a use-cases por interfaz usando DTOs.

2. Unit of Work (UoW)

   - Archivos objetivo: app/infrastructure/database/_, app/domain/repositories/_
   - Tareas:
     - Definir interfaz UoW (begin/commit/rollback) en application o domain.
     - Implementación SQLAlchemy que encapsule session y repositorios.
     - Convertir commits dispersos por repositorio a UoW.commit().
   - Criterio: transacciones consistentes y revertibles en errores.

3. Centralizar composition root / DI

   - Archivos objetivo: crear app/infrastructure/di.py (o app/containers.py)
   - Tareas:
     - Registrar repositorios concretos, UoW, servicios y adaptadores de auth.
     - Usar esa fábrica en dependencias FastAPI (replace scattered factories).
   - Criterio: un solo archivo orquesta bindings.

4. Manejo de errores de infra y mapping a errores de dominio
   - Archivos objetivo: app/infrastructure/repositories/sqlalchemy/\*, app/core/exceptions.py
   - Tareas:
     - Capturar errores DB (SQLAlchemy) y lanzar excepciones de dominio (DatabaseError, TransactionError).
     - Normalizar logging de errores.
   - Criterio: no leaks de errores SQL; tests que validen mapeo.

### Prioridad Media

5. Mejorar mappers y separarlos de repositorios

   - Archivos objetivo: app/infrastructure/mappers/\*.py
   - Tareas:
     - Mapear todos los campos necesarios.
     - Mantener responsabilidad única (mapper = dto/entity <-> orm).
   - Criterio: cobertura de campos y tests unitarios.

6. Separar Presentation DTOs (Pydantic) de Application DTOs

   - Archivos objetivo: app/presentation/schemas/_, app/application/dtos/_
   - Tareas:
     - Crear conversión explícita entre Pydantic schemas y Application DTOs.
   - Criterio: controllers no pasen primitivas directamente a servicios.

7. Exponer adaptadores de auth como puerto
   - Archivos objetivo: app/infrastructure/auth/\*, app/core/auth_interface.py
   - Tareas:
     - Definir interfaz AuthService y usarla via DI.
   - Criterio: posibilidad de intercambiar implementación (JWT/LDAP).

### Prioridad Baja

8. Eventos de dominio / bus

   - Archivos objetivo: app/core/events.py, adaptadores event-bus
   - Tareas: diseño simple para emitir eventos (audit, notifs).
   - Criterio: handlers desacoplados.

9. Logging, metrics y tracing
   - Archivos objetivo: middlewares, app/main.py
   - Tareas: middleware para request/logging y adaptador inyectable.
   - Criterio: logs correlacionables por request id.

### Tests (imprescindible)

- Unitarios dominio: modelos, validaciones e invariantes.
  - Carpeta: tests/unit/domain
- Integración repositorios con DB de prueba (sqlite ephemeral)
  - Carpeta: tests/integration
- Contract tests para repositorios (asegurar interfaz)
- E2E básicos de API (usar TestClient)
- Criterio: pipeline CI ejecuta tests y bloquea PRs.

### Operacional / infra

- Revisar configuración DB (pooling, engines) en app/infrastructure/database
- Añadir script/Makefile para tareas: lint, tests, run-local
- Criterio: comandos reproducibles en Windows (PowerShell/cmd) y CI.

### Estimaciones (orientativas)

- Small (S): 1-2 días
- Medium (M): 3-7 días
- Large (L): >1 semana
- Ejemplos:
  - Puertos + DTOs: M
  - UoW + refactor repositorios: M-L
  - DI central: S-M
  - Tests iniciales: M

### Checklist de PR (para cada cambio grande)

- [ ] Crear/actualizar interfaz y tests unitarios
- [ ] Implementación concreta + tests de integración
- [ ] Actualizar mappers y documentación interna
- [ ] Actualizar dependencias/di y routers
- [ ] Ejecutar pipeline local y CI

### Sugerencias inmediatas (próximo paso recomendado)

- Elegir patrón UoW (context manager SQLAlchemy) y crear archivo inicial:
  - app/application/uow.py (interfaz)
  - app/infrastructure/uow/sqlalchemy_uow.py (implementación)
- Crear app/infrastructure/di.py con bindings mínimos (PostRepository, UoW, AuthService).
- Escribir 3 tests: dominio simple, repo create+get (sqlite in-memory), API create post E2E.

Si querés, creo ahora:

- plantilla de app/infrastructure/di.py + ejemplo de UoW, o
- TODO desglosado en issues pequeños listos para crear PRs.
