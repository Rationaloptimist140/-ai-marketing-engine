# Architecture

MVP is a modular monolith: Next.js frontend, FastAPI backend, SQLAlchemy persistence, PostgreSQL in production and SQLite for tests. Agent definitions and prompts are version-controlled. Agent execution is represented by persisted run records; a worker adapter will be added later. External actions must pass through approval and integration adapters. Business records are workspace-scoped.

## Trust boundaries
- Browser to API: authenticated session required before production.
- API to database: parameterised ORM operations.
- Agent to tools: allow-listed tools only; no arbitrary code execution.
- Agent to external platform: disabled until permission, policy and human approval checks pass.

Render blueprint is provided at repository root. Production secrets belong in Render environment settings, never in Git.
