# AI Marketing Engine

MVP foundation for an AI-assisted affiliate marketing and advertising agency operations platform.

## Current status
Foundation only. The API supports health, agent discovery, workspace creation, campaign creation/listing and queued agent-run records. Agent runs do not yet call an LLM or execute in the background. The dashboard is a static Next.js shell. No social, affiliate, OpenAI Ads or billing integrations are connected. Not production-ready for public multi-tenant use until authentication and tenant authorization are implemented.

## Local development
Backend: `cd backend && pip install -r requirements.txt && uvicorn app.main:app --reload`
Tests: `cd backend && pytest -q`
Frontend: `cd frontend && npm install && npm run dev`

Copy `backend/.env.example` to `backend/.env`. SQLite is the local default; Render uses PostgreSQL through `DATABASE_URL`.

A Render blueprint is provided in `render.yaml`. Deployment has not been performed.
