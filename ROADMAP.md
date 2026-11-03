# Roadmap

## 1. Establish independent project baselines

- Keep each project in its own repository or clearly bounded project directory.
- Record a verified standalone command and smoke test for each project.
- Reconcile the BIG_ANIMAL milestone with the actual pushed commit and current local changes before marking the workspace clean.

## 2. Implement the first integration contract

- Agree on the draft JSON envelope and local HTTP adapter conventions.
- Add health checks and versioned adapters only to projects with a real integration need.
- Start with AgentDash and InfoEngine; keep all integration optional.

## 3. Connect the intelligence and decision flow

- Add LLM_Organism and ComplexConscious as independent projects.
- Connect InfoEngine → LLM_Organism → ComplexConscious through documented payloads.
- Integrate RB-App as the dashboard/application surface without making it a runtime prerequisite for those projects.

## 4. Add training and analytics

- Add Cyber-Arena, Red_Teaming, and INFOPHYS-PIPELINE as separate projects.
- Define explicit, limited data flows for training results and analytics.
- Verify that analytics and training integrations cannot trigger actions in other projects implicitly.

## Completion gates

- Every project has a documented standalone command and smoke test before orchestration is expanded to process management.
- Every implemented integration has a contract version, health check, timeout, and failure test.
- `python scripts/lab.py check` validates the registry; `python -m unittest discover -s tests` passes.
