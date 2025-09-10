# TODO: Clean Architecture & Hexagonal Improvements

## Completed Tasks ✅

- [x] Use dependency injection for repositories and services in FastAPI routes
- [x] Decouple domain and API models with mapping functions
- [x] Raise custom domain exceptions and map to HTTP errors
- [x] Use environment variables for configuration (e.g., DB URL)
- [x] Add .env example and update README with .env usage instructions
- [x] Add/Improve testing setup (unit, integration, in-memory repo)
- [x] Document architecture and best practices in README
- [x] Add more robust error handling (custom exceptions for other cases)
- [x] Review and clean up all imports and dependencies
- [x] Configure code formatting tools (black, isort)
- [x] Set up type checking with mypy and linting with flake8

## Next Tasks 🎯

- [ ] Apply type hints and docstrings to all modules:
  - [ ] Domain models and exceptions
  - [ ] Application services
  - [ ] Infrastructure components
  - [ ] Web routes and controllers
- [ ] Set up CI/CD pipeline with GitHub Actions:
  - [X] Run tests
  - [X] Check types with mypy
  - [X] Verify formatting with black/isort
  - [X] Run flake8 linting
  - [ ] Build and publish Docker image
- [ ] Add API documentation:
  - [X] Set up ReDoc/Swagger UI
  - [ ] Add detailed endpoint descriptions
  - [ ] Document request/response schemas
  - [ ] Add example requests
- [ ] Add database migrations with Alembic:
  - [X] Set up migration environment
  - [X] Create initial migration
- [ ] Implement security features:
  - [ ] User authentication (JWT)
  - [ ] Role-based authorization
  - [ ] Rate limiting middleware
  - [ ] CORS configuration

## Infrastructure Improvements 🛠

- [ ] Set up logging and monitoring:
  - [ ] Configure structured logging
  - [ ] Add request tracing
  - [ ] Set up health check endpoints
  - [ ] Add metrics collection
- [ ] Implement caching layer:
  - [ ] Add Redis integration
  - [ ] Cache frequent queries
  - [ ] Implement cache invalidation
- [ ] Set up local development environment:
  - [ ] Create Docker Compose setup
  - [ ] Add development utilities
  - [ ] Document local setup process

## Future Enhancements 🚀

- [ ] Add GraphQL support:
  - [ ] Set up Strawberry-GraphQL
  - [ ] Define GraphQL schema
  - [ ] Add resolvers
- [ ] Implement advanced features:
  - [ ] WebSocket support for real-time updates
  - [ ] Event sourcing for post history
  - [ ] Full-text search capability
- [ ] Performance optimizations:
  - [ ] Add query optimization
  - [ ] Implement connection pooling
  - [ ] Set up load testing
  - [ ] Add performance benchmarks

- [x] Use dependency injection for repositories and services in FastAPI routes
- [x] Decouple domain and API models with mapping functions
- [x] Raise custom domain exceptions and map to HTTP errors
- [x] Use environment variables for configuration (e.g., DB URL)
- [x] Add .env example and update README with .env usage instructions
- [x] Add/Improve testing setup (unit, integration, in-memory repo)
- [x] Document architecture and best practices in README
- [x] Add more robust error handling (custom exceptions for other cases)
- [ ] Add type hints and docstrings for all public functions/classes
- [ ] Review and clean up all imports and dependencies
