# Dependency Matrix

The table distinguishes project availability from the design goal that each project can run alone. “Runs alone” is a target until a project-specific smoke test and launch command are documented. Integration edges are optional data/control connections, not prerequisites for starting the source project.

| Project | Workspace status | Runs alone | Provides | Planned integrations |
|---|---|---|---|---|
| RB-App | Planned | ✅ Target | Dashboard application | Cyber-Arena, INFOPHYS-PIPELINE |
| InfoEngine | Present | ✅ Target | Intelligence | LLM_Organism, ComplexConscious, RB-App, INFOPHYS-PIPELINE |
| LLM_Organism | Planned | ✅ Target | Agents | ComplexConscious, RB-App, INFOPHYS-PIPELINE |
| ComplexConscious | Planned | ✅ Target | Decisions | RB-App, INFOPHYS-PIPELINE |
| BIG_ANIMAL | Present | ✅ Target | Simulation | InfoEngine, INFOPHYS-PIPELINE, AgentDash |
| Cyber-Arena | Planned | ✅ Target | Training | INFOPHYS-PIPELINE |
| Red_Teaming | Planned as a separate repo | ✅ Target | Red-team research tooling | Cyber-Arena, AgentDash |
| INFOPHYS-PIPELINE | Planned | ✅ Target | Analytics | AgentDash |
| AgentDash | Prototype present | ✅ Target | Dashboard and operator view | InfoEngine, LLM_Organism, ComplexConscious, RB-App, Cyber-Arena, BIG_ANIMAL |

`lab.json` is the machine-readable source for project paths and planned edges. Check the current local view with:

```sh
python scripts/lab.py status
python scripts/lab.py matrix
python scripts/lab.py check
```

Current Red_Teaming-related scripts live under `Renzo-Hacker-Lab/red-team`; that directory is not yet a standalone repository. AgentDash currently refers to the cockpit prototype in `claudecode/claudecore/agentdash`, not a deployed service.
