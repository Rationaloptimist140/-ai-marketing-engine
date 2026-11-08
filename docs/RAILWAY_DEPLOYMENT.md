# Railway deployment

## Target topology

- `web`: Next.js frontend, built from `/frontend`
- `api`: FastAPI backend, built from `/backend`
- `Postgres`: Railway-managed PostgreSQL service

Each application service is deployed from the same GitHub repository with a different Root Directory. The Railway configuration file is located in that service's root directory.

## Create the project

1. In Railway, create a new project and deploy from the GitHub repository `Rationaloptimist140/-ai-marketing-engine`.
2. Create the API service. Set its Root Directory to `/backend`. Railway should detect `railway.json` in that directory and use the Dockerfile in the same directory.
3. Add a PostgreSQL service to the project.
4. In the API service variables, set:
   - `ENVIRONMENT=production`
   - `DATABASE_URL=${{Postgres.DATABASE_URL}}` (use the actual Railway PostgreSQL service name in the reference)
   - `CORS_ORIGINS=https://<your-web-domain>`
5. Create a second service from the same repository for the frontend. Set its Root Directory to `/frontend`.
6. Set `NEXT_PUBLIC_API_URL` to the public API origin. The frontend is currently a scaffold and is not yet wired to the API.
7. Generate Railway domains for the API and frontend. Verify the API health endpoint at `/api/v1/health` and open the frontend domain.

## Cost controls

- Start with the smallest suitable service resources and scale only after measuring actual usage.
- Avoid adding Redis, workers, observability add-ons, or extra replicas until the MVP requires them.
- Check Railway's current pricing and usage dashboard before enabling paid resources. Costs depend on runtime, memory, CPU, storage, and network usage; this repository does not assume a fixed monthly price.
- Configure usage alerts/budgets in Railway where available.

## Security and production readiness

- Keep API keys and database credentials in Railway variables, never commit them.
- Restrict `CORS_ORIGINS` to the actual frontend domain.
- Implement authentication, workspace membership checks, migrations, backups, and rate limits before exposing multi-tenant functionality to customers.
- Do not treat a successful container health check as proof that the application is production-ready.

## Deployment status

Configuration only. No Railway project, service, database, domain, or deployment has been created or verified by this repository change.
