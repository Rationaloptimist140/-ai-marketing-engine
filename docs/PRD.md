# MVP Product Requirements

## Objective
A multi-tenant marketing operations platform supporting internal affiliate campaigns and agency client campaigns.

## MVP scope
- Workspaces of type `internal` and `client`.
- Campaign CRUD foundation.
- Eight-agent registry and queued execution records.
- Human approval as a hard gate before external actions.
- API health and agent discovery endpoints.
- Dashboard shell.
- PostgreSQL-compatible persistence and SQLite test mode.

## Out of scope
Live ad account integrations, automated social publishing, automated outreach, affiliate ingestion, billing, authentication/production tenant authorization, background agent execution and model calls.

## Acceptance criteria
API starts locally; health and registry work; workspaces and campaigns persist; agent requests queue without external actions; cross-workspace campaign lookup is rejected; tests pass.
