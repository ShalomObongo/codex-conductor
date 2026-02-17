# Conductor Track Schema Reference

## Track Registry Section Shape

A track registry entry should include:

1. A section separator (`---`) for each track block.
2. A heading with status marker and track label.
3. A link to the track folder.

Common heading patterns supported:
- `## [ ] Track: <description>`
- `## [~] Track: <description>`
- `## [x] Track: <description>`
- `- [ ] **Track:** <description>`
- `- [~] **Track:** <description>`
- `- [x] **Track:** <description>`

## Status Markers

- `[ ]` pending/not started
- `[~]` in progress
- `[x]` complete

## Track Folder Layout

`conductor/tracks/<track_id>/`

Required files:
- `spec.md`
- `plan.md`
- `metadata.json`

Optional but recommended:
- `index.md` with links to local track files

## Plan Conventions

- Use markdown task checkboxes with explicit statuses.
- Keep phase headings stable and append checkpoint tags only when applicable.
- When a task is completed, append commit SHA shorthand if your workflow requires it.

## Track ID Convention

Preferred format:
- `<short_name>_<YYYYMMDD>`

Guidelines:
- `short_name` should be lowercase snake_case.
- Reuse existing `short_name` only when explicitly continuing the same track.
- Avoid creating duplicate active tracks with the same `short_name`.
