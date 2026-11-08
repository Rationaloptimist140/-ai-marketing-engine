# Security baseline and launch blockers

- Add authentication and role-based access before exposing the service publicly.
- Enforce workspace ownership in every read and write; current MVP has no user identity layer and is not production-safe for multi-user use.
- Add PostgreSQL row-level security or equivalent tenant enforcement before client onboarding.
- Encrypt integration credentials using a managed secret store/KMS.
- Add audit events for approvals, exports and external actions.
- Add rate limits, request size limits, CSRF/session protections as applicable, and dependency scanning.
- Never expose API keys to the browser.
- External publishing, spending and client outreach require explicit approval.
