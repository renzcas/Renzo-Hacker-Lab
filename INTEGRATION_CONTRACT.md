# Integration Contract (Draft)

**Status:** proposal; no cross-project adapters are implemented yet.

## Principles

- Each project owns its source, dependencies, configuration, state, and standalone lifecycle.
- A project must remain usable without the other projects. `runs_alone` in `lab.json` is a design target, not a claim that the current workspace has verified every project's launch path.
- Integrations are optional adapters. One project's failure must not corrupt another project's state.
- The lab orchestrator reports inventory and proposed connections; it does not start processes or run project actions until safe, explicit commands are registered.

## Local transport

For the first local integration, use HTTP with JSON over loopback (`127.0.0.1`). A project may expose an adapter only when it has a concrete integration need. Do not require a service/API just to appear in the registry.

An adapter should provide:

- `GET /healthz`, returning a successful status only when the adapter can serve requests.
- A versioned API path such as `/api/v1/...`.
- Bounded request timeouts, clear error responses, and no hidden retries for mutating operations.
- Configuration through environment variables or local config; never hard-code credentials.

The transport can be revisited if a specific project cannot reasonably expose a local HTTP adapter. The manifest's integration edges do not imply that these endpoints exist today.

## Shared event envelope

Cross-project events use UTF-8 JSON with this common envelope; `payload` is project-specific and must be documented by its producer.

```json
{
  "contract_version": "1",
  "event_id": "unique-event-id",
  "occurred_at": "2026-01-01T00:00:00Z",
  "source": "InfoEngine",
  "type": "example.updated",
  "correlation_id": "optional-workflow-id",
  "payload": {}
}
```

`event_id`, `occurred_at`, `source`, and `type` are required. `correlation_id` is optional. Consumers must ignore unknown fields, reject unsupported major contract versions with an explicit error, and avoid treating delivery as exactly-once. Producers should make repeated delivery safe.

## Data and safety boundaries

- No shared database or direct reads of another project's private files. Exchange only documented API payloads.
- Bind local adapters to loopback by default. Remote access requires a separately reviewed deployment design.
- Do not transmit secrets, credentials, or unnecessary personal data in events or logs.
- Keep simulation, training, analytics, and operator actions separate. Integrations may present or analyze results; they must not silently trigger actions in another project.
- Log adapter failures with the source, operation, and correlation ID where available, while redacting sensitive values.

## Versioning and compatibility

The envelope version identifies the shared contract; project APIs version independently. Additive optional fields are compatible. Breaking changes require a new major contract/API version and a documented migration window. Registry paths and integration edges are local workspace metadata, not public API guarantees.

## Initial connection flow

The target operator flow is AgentDash → InfoEngine → LLM_Organism → ComplexConscious → RB-App → Cyber-Arena. BIG_ANIMAL, Red_Teaming, and INFOPHYS-PIPELINE remain independent and may provide or consume explicitly documented data. These are proposed integration edges, not hard runtime dependencies.
