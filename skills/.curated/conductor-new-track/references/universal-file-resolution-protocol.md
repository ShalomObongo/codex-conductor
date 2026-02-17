# Universal File Resolution Protocol

Use this protocol to resolve Conductor files reliably across project and track scopes.

## Resolution Steps

1. Identify the relevant index file.
- Project context index: `conductor/index.md`
- Track context index: `<track_folder>/index.md`

2. Resolve track index when starting from a track ID.
- Read the tracks registry and locate the track entry.
- Follow the track folder link from the registry.
- Use `<track_folder>/index.md`.
- Fallback: if the registry link is unavailable, use `conductor/tracks/<track_id>/index.md`.

3. Read the index and find the label.
- Match exact or semantically equivalent labels.

4. Resolve path relative to the index directory.
- Example: `./workflow.md` from `conductor/index.md` resolves to `conductor/workflow.md`.

5. Fallback to default paths if index/link lookup fails.

6. Verify final path exists on disk before using it.

## Default Paths (Project)

- Product Definition: `conductor/product.md`
- Product Guidelines: `conductor/product-guidelines.md`
- Tech Stack: `conductor/tech-stack.md`
- Workflow: `conductor/workflow.md`
- Tracks Registry: `conductor/tracks.md`
- Tracks Directory: `conductor/tracks/`

## Default Paths (Track)

- Specification: `conductor/tracks/<track_id>/spec.md`
- Implementation Plan: `conductor/tracks/<track_id>/plan.md`
- Metadata: `conductor/tracks/<track_id>/metadata.json`
