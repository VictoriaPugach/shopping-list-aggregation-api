# Security policy

## Supported version

Only the current `main` branch is supported while the service is in MVP.

## Reporting a vulnerability

Do not publish a security issue with a reproduction containing credentials or personal data. Contact the repository maintainers privately, describe the impact and steps to reproduce, and wait for a response before disclosing it publicly.

## MVP safeguards

The API must validate input against Recipe v1, limit the number of recipes per request, avoid logging request bodies by default, and never commit secrets. Use `.env` only for local configuration; it is intentionally ignored by Git.
