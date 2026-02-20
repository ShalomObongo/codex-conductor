# Conductor Skills for Codex

**Measure twice, code once.**

Conductor is a Codex-focused skills catalog for **Context-Driven Development**.
It turns Codex into a proactive project manager that follows a strict protocol to specify, plan, implement, review, and safely revert software changes.

Instead of jumping directly into code, Conductor enforces a predictable lifecycle:
**Context -> Spec & Plan -> Implement -> Review -> Revert (if needed)**.

> [!WARNING]
> **Do not mix Conductor with Codex Plan mode in the same run**
> Conductor already owns its own planning/approval lifecycle. When running Conductor skills, stay in Codex Default mode to avoid state conflicts.

## Why Conductor

- **Plan before build**: Create explicit specs and implementation plans before coding.
- **Context as source of truth**: Keep product context, tech stack, workflow, and style guides in-repo.
- **Execution discipline**: Track progress in `plan.md` and `tracks.md` with auditable status markers.
- **Team consistency**: Standardize how contributors and agents work across tracks.
- **Git-aware safety**: Revert by logical unit (track, phase, task), not just commit guesswork.

## Included Skills

| Skill | Purpose |
| --- | --- |
| `$conductor-setup` | Initialize Conductor context, templates, and first-track scaffolding |
| `$conductor-new-track` | Create a new track and generate `spec.md` + `plan.md` |
| `$conductor-implement` | Execute tasks from a selected track plan |
| `$conductor-status` | Summarize progress, current work, blockers, and next action |
| `$conductor-review` | Review implementation against plan, workflow, and quality standards |
| `$conductor-revert` | Revert tracks/phases/tasks with guided confirmations |

## Install

**Recommended:** use the one-line installer/updater (no clone required).

Run in terminal:

```bash
curl -fsSL https://raw.githubusercontent.com/ShalomObongo/codex-conductor/main/scripts/update_conductor_skills.sh | bash -s -- --ref main
```

After installation, restart Codex so new skills are loaded.

## Updating Skills

There are two update channels:

1. **Rolling updates (`main`)**: always install latest from the default branch.
2. **Pinned updates (`tag`)**: install from a specific version tag for stability.

### One-line update (latest `main`)

```bash
curl -fsSL https://raw.githubusercontent.com/ShalomObongo/codex-conductor/main/scripts/update_conductor_skills.sh | bash -s -- --ref main
```

Pinned version (example):

```bash
curl -fsSL https://raw.githubusercontent.com/ShalomObongo/codex-conductor/main/scripts/update_conductor_skills.sh | bash -s -- --ref v1.0.0
```

### Paste into Codex (chat command)

Paste this exact line into Codex to have it install/update skills for you:

```text
Run this command now to install/update all Conductor skills: curl -fsSL https://raw.githubusercontent.com/ShalomObongo/codex-conductor/main/scripts/update_conductor_skills.sh | bash -s -- --ref main
```

### Update using the bundled script

Clone this repository and run:

```bash
chmod +x scripts/update_conductor_skills.sh
scripts/update_conductor_skills.sh
```

Install from a specific tag:

```bash
scripts/update_conductor_skills.sh --ref v1.0.0
```

By default, this updates skills in `$CODEX_HOME/skills` (or `~/.codex/skills`).
After running updates, restart Codex.

### Update manually with `$skill-installer`

This is a fallback option if you do not want to use the one-line script.
Install each skill from `main` (or swap `main` with a tag in the URL):

```text
$skill-installer install https://github.com/ShalomObongo/codex-conductor/tree/main/skills/.curated/conductor-setup
$skill-installer install https://github.com/ShalomObongo/codex-conductor/tree/main/skills/.curated/conductor-new-track
$skill-installer install https://github.com/ShalomObongo/codex-conductor/tree/main/skills/.curated/conductor-implement
$skill-installer install https://github.com/ShalomObongo/codex-conductor/tree/main/skills/.curated/conductor-status
$skill-installer install https://github.com/ShalomObongo/codex-conductor/tree/main/skills/.curated/conductor-review
$skill-installer install https://github.com/ShalomObongo/codex-conductor/tree/main/skills/.curated/conductor-revert
```

## Usage Lifecycle

### 1. Set Up Project Context

Use `$conductor-setup` once per repository to establish:

- `conductor/product.md`
- `conductor/product-guidelines.md`
- `conductor/tech-stack.md`
- `conductor/workflow.md`
- `conductor/code_styleguides/`
- `conductor/tracks.md`

Example prompt:

```text
Use $conductor-setup to initialize this repository.
```

### 2. Start a Track

Use `$conductor-new-track` to generate track-specific artifacts:

- `conductor/tracks/<track_id>/spec.md`
- `conductor/tracks/<track_id>/plan.md`
- `conductor/tracks/<track_id>/metadata.json`

Example prompt:

```text
Use $conductor-new-track to plan a dark mode feature for settings.
```

### 3. Implement the Track

Use `$conductor-implement` to execute plan tasks and update status markers.

Example prompt:

```text
Use $conductor-implement to execute the next pending track.
```

### 4. Operate Day-to-Day

- `Use $conductor-status to summarize current progress and blockers.`
- `Use $conductor-review to review the in-progress track.`
- `Use $conductor-revert to revert the last completed phase.`

## Skill Reference

| Skill | Primary Inputs | Typical Outputs |
| --- | --- | --- |
| `$conductor-setup` | Repo state, user product answers | Initialized `conductor/` context files and templates |
| `$conductor-new-track` | Track description/scope | New track folder with spec/plan/metadata + tracks registry update |
| `$conductor-implement` | Optional track scope | Task execution, plan state changes, track completion updates |
| `$conductor-status` | Optional track scope | Progress report with totals, active task, blockers |
| `$conductor-review` | Track or working-tree scope | Prioritized findings and recommended fixes |
| `$conductor-revert` | Track/phase/task target | Revert plan + executed git revert flow (with confirmations) |

## Migration Map

This release is a hard cutover from Gemini extension commands to Codex skills.

| Legacy Command | Codex Skill |
| --- | --- |
| `conductor:setup` | `$conductor-setup` |
| `conductor:newTrack` | `$conductor-new-track` |
| `conductor:implement` | `$conductor-implement` |
| `conductor:status` | `$conductor-status` |
| `conductor:review` | `$conductor-review` |
| `conductor:revert` | `$conductor-revert` |

## Repository Layout

```text
skills/.curated/
  conductor-setup/
  conductor-new-track/
  conductor-implement/
  conductor-status/
  conductor-review/
  conductor-revert/
skills/_shared/
scripts/build_skills.py
scripts/validate_skills.py
```

## Development

Build shared references into each curated skill:

```bash
python3 scripts/build_skills.py
```

Validate structure, metadata, and legacy-string regression checks:

```bash
python3 scripts/validate_skills.py
```

## Resources

- [Using skills in Codex](https://developers.openai.com/codex/skills)
- [Create custom skills in Codex](https://developers.openai.com/codex/skills/create-skill)
- [Agent Skills specification](https://agentskills.io/spec)
- [openai/skills catalog conventions](https://github.com/openai/skills)

## License

Apache License 2.0 (see `LICENSE`).
