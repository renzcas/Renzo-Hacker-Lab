# Duplicate and Naming Review

This is a filesystem comparison, not a recommendation to delete files. The root-level module directories include uncommitted workspace content; preserve that work until ownership and imports are verified.

## Overlapping module trees

Comparing same relative paths under each root directory and `big_animal/`:

| Root directory | Matching relative paths | Byte-identical files |
|---|---:|---|
| `agents/` vs `big_animal/agents/` | 6 | None |
| `engines/` vs `big_animal/engines/` | 10 | None |
| `events/` vs `big_animal/events/` | 2 | `event_types.py` |
| `organism/` vs `big_animal/organism/` | 3 | `organism_state.py` |
| `simulation/` vs `big_animal/simulation/` | 2 | None |
| `ui/` vs `big_animal/ui/` | 5 | None |

The repeated paths suggest overlapping ownership, but filename matches alone do not prove duplication. Some same-named modules differ in content and may contain unique behavior. Proposed direction: make `big_animal/` canonical for BIG_ANIMAL functionality, then trace imports and compare unique APIs before migrating or retiring any root-level modules.

## Suspicious names inside BIG_ANIMAL

- `big_animal/ui/worldheart_harmonics,py` and `big_animal/ui/worldheart_harmonics.py` have different sizes and contents. The comma-suffixed file is likely a naming artifact, but confirm imports and preserve any unique implementation before removal.
- `big_animal/worldheart/shielding.py` and `big_animal/worldheart/shirlding.py` have different sizes and contents. The latter looks misspelled; inspect references and behavior before choosing a canonical implementation.
- `docs/architechture.md` is an empty legacy file with a misspelled name. The canonical architecture draft is [ARCHITECTURE.md](./ARCHITECTURE.md).

## Safe cleanup sequence

1. Search imports and runtime references for each candidate file.
2. Compare public symbols and behavior; add tests for any behavior that must be retained.
3. Select the canonical implementation and update imports.
4. Run focused tests and a workspace smoke test.
5. Remove only files confirmed unused and redundant in a separate, reviewable change.
