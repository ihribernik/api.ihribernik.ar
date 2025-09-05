# 📝 Blog API con Flask + Arquitectura Hexagonal ( blog.ihribernik.ar )

Este proyecto es un **ejemplo de arquitectura moderna** para construir una API de un blog usando **Flask**, aplicando los principios de **Clean Code** y **Arquitectura Hexagonal (Ports & Adapters)**.

---

## 🚀 Principios de diseño

- **Dominio independiente**: la lógica del blog (posts, comentarios, usuarios) vive en entidades y servicios de dominio, sin depender de Flask ni de la base de datos.
- **Puertos (Interfaces)**: definen lo que la app necesita del mundo externo (repositorios, notificaciones, etc.).
- **Adaptadores**: implementan esos puertos para cosas concretas (SQLAlchemy, API Flask, etc.).
- **Inversión de dependencias**: el dominio no sabe nada del framework, el framework sabe del dominio.

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
│   │   ├── web/             # API Flask/FastAPI (controllers, routes)
│   │   ├── db/              # Modelos y config de SQLAlchemy / migrations
│   │   ├── auth/            # JWT, OAuth2, etc.
│   │   └── config.py
│   │
│   ├── main.py              # Entry point de Flask (WSGI app)
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

2. Creá un entorno virtual e instalá dependencias:

   ```bash
   python -m venv venv
   .\venv\Scripts\activate   # En Windows
   # source venv/bin/activate   # En Linux/Mac

   pip install -r requirements.txt
   ```

---

## ▶️ Ejecución de la API

Iniciá la app de Flask:

```bash
flask --app app/main.py run --reload
```

La API quedará disponible en:

```bash
http://127.0.0.1:5000/api
```

---

## 📌 Endpoints disponibles

- `POST /api/posts` → Crear un post nuevo.
  **Body JSON:**

  ```json
  {
    "title": "Mi primer post",
    "content": "Contenido del post",
    "author": "ivan"
  }
  ```

- `GET /api/posts` → Listar todos los posts.

---

## 🧪 Testing

Se recomienda usar **Pytest**.

1. Instalá pytest:

   ```bash
   pip install pytest
   ```

2. Ejecutá los tests:

   ```bash
   pytest
   ```

Los tests usan un **InMemoryRepository** para no depender de Flask ni de la base de datos.

---

## 🔮 Próximos pasos

- Agregar autenticación (JWT).
- Implementar repositorios con distintas bases de datos (Postgres, MongoDB).
- Extender con comentarios y usuarios.
- Reemplazar Flask por FastAPI sin tocar la lógica de dominio.

---

## 📖 Recursos recomendados

- [Arquitectura Hexagonal explicada](https://alistair.cockburn.us/hexagonal-architecture/)
- [Clean Architecture de Uncle Bob](https://blog.cleancoder.com/)

---

✨ Con esta estructura tu API es mantenible, extensible y fácil de testear.
