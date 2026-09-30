# Restaurant Agent Engineering Scaffold

Start the Restaurant AI Agent Backend project with a working FastAPI service,
a responsive Juniper & Stone restaurant website, automated quality checks,
local data-service definitions, GitHub workflow templates, and an engineering
documentation structure.

## Create your private implementation repository

Use this repository as a **GitHub template**, not a normal fork. A repository
created from the public template can be private, while a normal fork of a
public repository remains public.

### GitHub website

1. Select **Use this template**.
2. Select **Create a new repository**.
3. Choose your account and a project name.
4. Set visibility to **Private**.
5. Create the repository, then clone it locally.

### GitHub CLI

```bash
gh repo create YOUR_REPOSITORY_NAME \
  --private \
  --template jessieffff/restaurant-agent-engineering-scaffold \
  --clone
```

## Quick start

Requirements:

- Python 3.11, 3.12, or 3.13
- Git
- Docker with Docker Compose
- GNU Make

GitHub CLI authentication is needed for guarded merging. Ollama is needed when
you reach the local model gateway. `make doctor` reports both as later
requirements without blocking the initial setup; follow your course schedule
for their exact session.

Prepare the local environment:

```bash
make bootstrap
make doctor
make check
```

In the generated GitHub repository, open **Actions → quality → Run workflow**
and confirm the first quality run passes.

Start the restaurant website and API during early development:

```bash
make run
```

Open:

- Restaurant website: <http://127.0.0.1:8000/>
- API documentation: <http://127.0.0.1:8000/docs>
- Liveness: <http://127.0.0.1:8000/health/live>
- Readiness: <http://127.0.0.1:8000/health/ready>

The website presents a fictional restaurant's menu, hours, reservation form,
and Ask Juniper chat interface. Reservation submission and chat sending remain
inactive until you connect the corresponding backend and Agent workflows.
Neither control returns a simulated booking or a scripted Agent reply.

Start the local service stack:

```bash
make up
make logs
```

Local services:

| Service | Address |
|---|---|
| API | <http://127.0.0.1:8000> |
| PostgreSQL with pgvector | `127.0.0.1:5432` |
| Valkey | `127.0.0.1:6379` |
| RabbitMQ AMQP | `127.0.0.1:5672` |
| RabbitMQ management | <http://127.0.0.1:15672> |

The credentials in `.env.example` are local-development placeholders only.
Do not reuse them outside the local environment.

## What is included

- FastAPI application factory
- Responsive restaurant website with original, locally served illustration,
  sample menu and hours, reservation-form shell, and accessible chat dialog
- Liveness and application-level readiness endpoints
- Pydantic settings loaded from environment variables
- Unit tests
- Ruff linting and formatting
- Strict mypy configuration
- GitHub Actions quality workflow
- Dockerfile
- Docker Compose services for PostgreSQL/pgvector, Valkey, and RabbitMQ
- Zero-cost pull-request merge guard for GitHub Free private repositories
- Issue and pull-request templates
- ADR, evidence, runbook, incident, and engineering-documentation templates
- Local bootstrap and environment doctor scripts

## Why this foundation is included

| Foundation | Purpose |
|---|---|
| Runnable FastAPI service | Verifies the Python environment and provides the first executable vertical slice |
| Restaurant website starter | Makes the final customer journey visible from day one without implementing Agent or booking behavior for you |
| Quality checks and CI | Establishes one repeatable lint, type, test, and evidence workflow |
| Local data services | Provides the PostgreSQL, vector, cache, and messaging systems used across later sessions |
| GitHub templates and merge guard | Standardizes task delivery and provides a zero-cost controlled merge path |
| Engineering documentation | Preserves decisions, contracts, operations knowledge, measurements, and evidence as the system grows |

## What you build during the course

- Versioned customer, staff, and agent APIs
- API-backed restaurant details and a real customer journey through the
  website: Agent chat, reservation confirmation, takeout, and handoff
- PostgreSQL schema, migrations, constraints, indexes, and transactions
- Dependency-aware readiness for PostgreSQL, Valkey, and RabbitMQ
- Reservation and ordering domains
- Idempotency and concurrency controls
- Valkey caching and rate limiting
- LangGraph workflows, model gateway, typed tools, and confirmation safety
- Student-authored, versioned task Skills for reservations, policy answers, and
  takeout: `SKILL.md` playbooks selected on demand by an Agent-side registry
- RAG ingestion, retrieval, citations, isolation, and evaluation
- RabbitMQ topology, outbox relay, workers, retries, and dead letters
- Authentication, authorization, audit, and PII controls
- Logs, metrics, traces, SLOs, alerts, runbooks, and incident evidence
- Load testing and performance optimization
- Kubernetes deployment, smoke tests, and rollback

## Project layout

```text
.
├── .github/                 GitHub workflow and collaboration templates
├── docs/                    Architecture, contracts, evidence, and operations
├── scripts/                 Bootstrap and environment checks
├── src/restaurant_agent/
│   ├── agent/               LangGraph workflow added during the course
│   │   └── skills/           Student-authored SKILL.md files added during the course
│   ├── api/                 FastAPI routes
│   ├── core/                Configuration and cross-cutting application setup
│   ├── domain/              Reservation, ordering, and restaurant rules
│   ├── platform/            Database, cache, broker, model, and telemetry adapters
│   ├── rag/                 Ingestion, retrieval, citations, and evaluation
│   ├── web/                 Restaurant page, styles, script, and original illustration
│   └── worker/              Relay and asynchronous workers
└── tests/                   Automated tests
```

The template does not include completed Skills. During the course, put
`reservation`, `restaurant-policy`, and `takeout` under
`src/restaurant_agent/agent/skills/` so they can ship with the Python
package and container. Each Skill describes when and how to complete a task;
it does **not** grant tool permissions or contain restaurant-specific prices
and unreviewed policies. The Agent must use server-enforced typed tools for
reads and writes, keep explicit confirmation for writes, and test Skill
selection, no-match fallback, and loaded versions.

## Grow the website with the system

- First, use the sample menu and hours as static starter content. Move them
  into versioned structured data and replace the page content with API
  responses when you implement restaurant information services.
- Connect the reservation form only after the backend supports availability,
  prepare, a visible summary, later explicit confirmation, and a safe write.
- Connect Ask Juniper to the actual Agent runtime and typed tools. Use the
  policy knowledge pipeline for cited answers, then add the takeout workflow.
- In the capstone, start from the website and demonstrate a complete synthetic
  customer journey. Preserve the accessible dialog and failure states as the
  UI evolves. A public domain is optional; the local zero-cost path is required.

## First project task

After setup:

1. Run `make check`.
2. Open the restaurant website and API documentation.
3. Read `CONTRIBUTING.md`.
4. Create the first Task Issue.
5. Create a short-lived branch from `main`.
6. Make one bounded change and open a pull request.
7. Preserve the CI link in `docs/evidence/ledger.md`.

## Pull-request merge guard

Before Session 3, install and authenticate GitHub CLI:

```bash
gh auth login
```

Verify and squash-merge a pull request only after its CI checks pass:

```bash
make merge PR=123 DRY_RUN=1
make merge PR=123
```

The guard requires an open, current, mergeable pull request targeting `main`,
verifies every reported check is passing, locks the merge to the verified head
commit, squash-merges, and deletes the source branch.

## Safety

- Use synthetic data only.
- Keep unimplemented website actions inactive; never present a placeholder as
  a completed reservation or a live Agent response.
- Never commit `.env`, credentials, access tokens, private keys, or real PII.
- Keep deterministic tests independent from hosted model availability.
- Keep every required workflow on a zero-payment path.

## License

MIT. See [LICENSE](LICENSE).
