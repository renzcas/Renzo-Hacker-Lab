# Renzo-Hacker-Lab Master Index

Renzo-Hacker-Lab is currently one Git repository containing several project areas. The directories are not separate Git repositories yet; the workspace can evolve into an integration platform without merging their source trees.

## Systems

| System | Status | Purpose | Current location |
|---|---|---|---|
| InfoEngine | Present; run status unverified | Knowledge and intelligence layer | `InfoEngine/` |
| BIG_ANIMAL | Present; operational status reported by user, not independently verified here | Dynamic simulation | `big_animal/` |
| ClaudeCode / Agent Runtime | Prototype present; run status unverified | Agent base, event bus, scanner, defender, and runtime | `claudecode/` |
| AgentDash | Cockpit prototype present | Operator-facing event dashboard | `claudecode/claudecore/agentdash/` |
| Red Team | Scripts present | Authorized recon and testing workflows | `Renzo-Hacker-Lab/red-team/` |
| Blue Team | Detection content present | Detection and defensive guidance | `Renzo-Hacker-Lab/blue-team/` |
| Labs | Training material present | Python and security skill development | `labs/` |
| ML Toolkit | Utilities and playground present | Modeling and dimensional-reduction experiments | `ml-toolkit/` |

`RB-App`, `LLM_Organism`, `ComplexConscious`, `Cyber-Arena`, `Red_Teaming` as a separate project, and `INFOPHYS-PIPELINE` are future project boundaries, not directories currently present at the workspace root.

## BIG_ANIMAL milestone

- **Status:** Operational (reported by the user; not independently verified in this workspace)
- **Commit:** `aff4c79` (reported by the user; commit object not found in the local repository)
- **Milestone:** Heartbeat verified (reported by the user)

The current workspace contains uncommitted changes under `big_animal/`, so the clean/pushed state is not verified here.

## Related documentation

- [Architecture draft](./ARCHITECTURE.md)
- [Integration contract](../INTEGRATION_CONTRACT.md)
- [Dependency matrix](../DEPENDENCY_MATRIX.md)
- [Roadmap](../ROADMAP.md)
- [Duplicate and naming review](./DUPLICATE_REVIEW.md)
