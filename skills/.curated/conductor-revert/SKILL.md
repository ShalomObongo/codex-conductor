---
name: conductor-revert
description: Use when a user asks to undo Conductor work at track, phase, or task level, including guided target selection, commit mapping, revert planning, conflict handling, and plan state synchronization.
---

# Conductor Revert

Perform git-aware revert operations aligned with Conductor logical units.

## Workflow
1. Read `references/protocol.md` fully before taking actions.
2. If the user includes a target scope (track, phase, task), treat it as initial intent and confirm.
3. Use `references/universal-file-resolution-protocol.md` to resolve tracks and implementation plans.
4. Use `references/track-schema.md` to map logical units to status and plan structure.
