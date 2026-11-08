# AI Marketing Engine

MVP foundation for an AI-assisted affiliate marketing and advertising agency operations platform.

## Current status
Foundation only. The API supports health, agent discovery, workspace creation, campaign creation/listing and queued agent-run records. Agent runs do not yet call an LLM or execute in the background. The dashboard is a static Next.js shell. No social, affiliate, OpenAI Ads or billing integrations are connected. Not production-ready for public multi-tenant use until authentication and tenant authorization are implemented.

## Local development
Backend: `cd backend && pip install -r requirements.txt && uvicorn app.main:app --reload`
Tests: `cd backend && pytest -q`
Frontend: `cd frontend && npm install && npm run dev`

Copy `backend/.env.example` to `backend/.env`. SQLite is the local default. Railway PostgreSQL should be attached to the backend service using the `DATABASE_URL` variable reference.

## Railway deployment
This is a monorepo with two Railway services:

1. **API service**: create a service from this repository, set its Root Directory to `/backend`, and use the included `backend/railway.json` configuration. Set `ENVIRONMENT=production`, `CORS_ORIGINS` to the deployed frontend origin, and `DATABASE_URL` to `${{Postgres.DATABASE_URL}}` after adding a Railway PostgreSQL service.
2. **Web service**: create a second service from the same repository, set its Root Directory to `/frontend`, and use `frontend/railway.json`. Set `NEXT_PUBLIC_API_URL` to the public API URL (including `/api/v1` only if the frontend expects that prefix).
3. Add a Railway PostgreSQL database and reference its connection string from the API service. Keep secrets in Railway variables, never in Git.
4. Generate public domains for the API and web services, then verify `/api/v1/health` and the dashboard.

Railway configuration files are included, but no Railway project, services, database, domain, or deployment has been created or verified yet. Review Railway's current resource pricing before provisioning.
