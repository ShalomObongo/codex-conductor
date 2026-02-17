# Changelog

## 1.0.0 (2026-02-17)

### Breaking Changes

- Replaced Gemini extension command surface with Codex skills.
- Removed legacy command manifests and Gemini-specific context files.
- Adopted OpenAI-style skills catalog layout under `skills/.curated`.

### Added

- Added curated skills:
  - `conductor-setup`
  - `conductor-new-track`
  - `conductor-implement`
  - `conductor-status`
  - `conductor-revert`
  - `conductor-review`
- Added shared references in `skills/_shared`.
- Added build and validation scripts for skills packaging and regression checks.
- Added `validate-skills` GitHub Actions workflow.

### Changed

- Updated release workflow to gate releases on skill validation.
- Moved Conductor templates into `skills/.curated/conductor-setup/assets/templates`.

### Migration Examples

| Previous Gemini Command | Codex Skill |
| --- | --- |
| `conductor:setup` | `$conductor-setup` |
| `conductor:newTrack` | `$conductor-new-track` |
| `conductor:implement` | `$conductor-implement` |
| `conductor:status` | `$conductor-status` |
| `conductor:revert` | `$conductor-revert` |
| `conductor:review` | `$conductor-review` |
