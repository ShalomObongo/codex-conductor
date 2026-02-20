# Changelog

## Unreleased

### Changed

- Synced Conductor skill protocols with upstream Conductor updates through 2026-02-20, including interactive confirmation/approval flow improvements in:
  - `conductor-setup`
  - `conductor-new-track`
  - `conductor-implement`
  - `conductor-review`
  - `conductor-revert`
- Added Codex compatibility notes for upstream `ask_user` interactions and model-selection directives.
- Added Codex Plan mode warning to `README.md` for Conductor workflow consistency.
- Updated release workflow upload step to use an environment variable for `tag_name` interpolation safety.

## [2.0.0](https://github.com/ShalomObongo/codex-conductor/compare/conductor-v1.0.0...conductor-v2.0.0) (2026-02-20)


### ⚠ BREAKING CHANGES

* migrate Conductor from Gemini extension to Codex skills catalog

### Features

* add /conductor:review command ([d4749d3](https://github.com/ShalomObongo/codex-conductor/commit/d4749d320ae983a12064488eb4b605529b0841e9))
* add /conductor:review command ([d6e382a](https://github.com/ShalomObongo/codex-conductor/commit/d6e382a980a816339c9ca9904a4744a635af7bd0))
* Add GitHub Actions workflow to package and upload release assets. ([5e0fcb0](https://github.com/ShalomObongo/codex-conductor/commit/5e0fcb0d4d19acfd8f62b08b5f9404a1a4f53f14))
* Add GitHub Actions workflow to package and upload release assets. ([20858c9](https://github.com/ShalomObongo/codex-conductor/commit/20858c90b48eabb5fe77aefab5a216269cc77c09))
* **conductor:** address review comments to make recommendations more conversational ([8630f35](https://github.com/ShalomObongo/codex-conductor/commit/8630f358f1d4ecf9e6c2815d0c607cf8c49ee3e8))
* **conductor:** implement tracks directory abstraction ([caeb814](https://github.com/ShalomObongo/codex-conductor/commit/caeb8146bec590eda35bc7934b796656804fcf9a))
* **conductor:** make review recommendations more conversational ([44446c6](https://github.com/ShalomObongo/codex-conductor/commit/44446c6338bdc5159fd8d9c7cf4c362e48d34e40))
* **conductor:** make review recommendations more conversational ([ec3dd99](https://github.com/ShalomObongo/codex-conductor/commit/ec3dd996afd98e7c695cc8dee79f3779b8e1d105))
* **conductor:** sync upstream protocol upgrades and Codex adaptations ([387a8ab](https://github.com/ShalomObongo/codex-conductor/commit/387a8abd7dcc290e87ffbaf607f7b663a932b8f7))
* **conductor:** update review process to commit fixes and update plan ([c26980a](https://github.com/ShalomObongo/codex-conductor/commit/c26980a5b9f952974c8c3cbcd82dc8c3ab2911f9))
* Implement Universal File Resolution Protocol ([fe902f3](https://github.com/ShalomObongo/codex-conductor/commit/fe902f32762630e674f186b742f4ebb778473702))
* integrate release asset packaging into release-please workflow ([3ef512c](https://github.com/ShalomObongo/codex-conductor/commit/3ef512c3320e7877f1c05ed34433cf28a3111b30))
* introduce index markdown files and the Universal File Resolution Protocol ([bbb69c9](https://github.com/ShalomObongo/codex-conductor/commit/bbb69c9fa8d4a6b3c225bfb665d565715523fa7d))
* introduce index.md files for file resolution ([cbd24d2](https://github.com/ShalomObongo/codex-conductor/commit/cbd24d2b086697a3ca6e147e6b0edfedb84f99ce))
* migrate Conductor from Gemini extension to Codex skills catalog ([cb38435](https://github.com/ShalomObongo/codex-conductor/commit/cb38435357b33f2349d905412d7731fc67e7f9b1))
* **review:** update review process to commit fixes and update plan ([0d533be](https://github.com/ShalomObongo/codex-conductor/commit/0d533be1c3ebfc07fd04cf8219ddc5964343c24a))
* **styleguide:** Add comprehensive Google C# Style Guide summary ([6672f4e](https://github.com/ShalomObongo/codex-conductor/commit/6672f4ec2d2aa3831b164635a3e4dc0aa6f17679))
* **styleguide:** Add comprehensive Google C# Style Guide summary ([e222aca](https://github.com/ShalomObongo/codex-conductor/commit/e222aca7eb7475c07e618b410444f14090d62715))


### Bug Fixes

* build tarball outside source tree to avoid self-inclusion ([830f584](https://github.com/ShalomObongo/codex-conductor/commit/830f5847c206a9b76d58ebed0c184ff6c0c6e725))
* **ci:** fallback to GITHUB_TOKEN when BOT_RELEASE_TOKEN is unset ([d56e6ad](https://github.com/ShalomObongo/codex-conductor/commit/d56e6ad6f25030930333e3486ab335edde3c5c8e))
* commit changed conductor files at the end of newTrack ([232c08b](https://github.com/ShalomObongo/codex-conductor/commit/232c08b3c99e362981019a6b8e7ca8de55d78357))
* Commit conductor files at the end of :newTrack ([#94](https://github.com/ShalomObongo/codex-conductor/issues/94)) ([232c08b](https://github.com/ShalomObongo/codex-conductor/commit/232c08b3c99e362981019a6b8e7ca8de55d78357))
* **conductor:** ensure track completion and doc sync are committed automatically ([f6a1522](https://github.com/ShalomObongo/codex-conductor/commit/f6a1522d0dea1e0ea887fcd732f1b47475dc0226))
* **conductor:** ensure track completion and doc sync are committed automatically ([e3630ac](https://github.com/ShalomObongo/codex-conductor/commit/e3630acc146a641f29fdf23f9c28d5d9cdf945b8))
* **conductor:** move pre-initialization overview before resume check ([774fb49](https://github.com/ShalomObongo/codex-conductor/commit/774fb49119d1f4d8d87dff22cbc14924fdb02a5b))
* **conductor:** move pre-initialization overview before resume check ([f2b7ba5](https://github.com/ShalomObongo/codex-conductor/commit/f2b7ba5c8963990ad454853692182f9367a099be)), closes [#81](https://github.com/ShalomObongo/codex-conductor/issues/81)
* **conductor:** remove hardcoded path hints in favor of Universal File Resolution Protocol ([6b14aaa](https://github.com/ShalomObongo/codex-conductor/commit/6b14aaa6f8bffd29b2dc3eb5fc22b2ed1d19418d))
* Correct typos, step numbering, and documentation errors ([ab9516b](https://github.com/ShalomObongo/codex-conductor/commit/ab9516ba6dd29d0ec5ea40b2cb2abab83fc791be))
* Correct typos, step numbering, and documentation errors ([d825c32](https://github.com/ShalomObongo/codex-conductor/commit/d825c326061ab63a4d3b8928cbf32bc3f6a9c797))
* Correct typos, trailing whitespace and grammar ([484d5f3](https://github.com/ShalomObongo/codex-conductor/commit/484d5f3cf7a0c4a8cbbcaff71f74b62c0af3dd35))
* Correct typos, trailing whitespace and grammar ([94edcbb](https://github.com/ShalomObongo/codex-conductor/commit/94edcbbd0102eb6f9d5977eebf0cc3511aff6f64))
* improve error message when required files are missing in review command ([d61c588](https://github.com/ShalomObongo/codex-conductor/commit/d61c588c6d4adc3393468180d62f13097f589e4c))
* Replace manual text input with interactive options ([b49d770](https://github.com/ShalomObongo/codex-conductor/commit/b49d77058ccd5ccedc83c1974cc36a2340b637ab))
* Replace manual text input with interactive options ([746b2e5](https://github.com/ShalomObongo/codex-conductor/commit/746b2e5f0a5ee9fc49edf8480dad3b8afffe8064))
* **setup:** clarify definition of 'track' in setup flow ([819dcc9](https://github.com/ShalomObongo/codex-conductor/commit/819dcc989d70d572d81655e0ac0314ede987f8b4))
* **setup:** Enhance project analysis protocol to avoid excessive token consumption. ([#6](https://github.com/ShalomObongo/codex-conductor/issues/6)) ([1e60e8a](https://github.com/ShalomObongo/codex-conductor/commit/1e60e8a96e5abeab966ff8d5bd95e14e3e331cfa))
* standardize Markdown checkbox format for tracks and plans ([92080f0](https://github.com/ShalomObongo/codex-conductor/commit/92080f0508ca370373adee1addec07855506adeb))
* standardize Markdown checkbox format for tracks and plans ([84634e7](https://github.com/ShalomObongo/codex-conductor/commit/84634e774bc37bd3996815dfd6ed41a519b45c1d))
* **styleguide:** Clarify usage of 'var' in C# guidelines for better readability ([a67b6c0](https://github.com/ShalomObongo/codex-conductor/commit/a67b6c08cac15de54f01cd1e64fff3f99bc55462))
* **styleguide:** Enhance C# guidelines with additional rules for constants, collections, and argument clarity ([eea7495](https://github.com/ShalomObongo/codex-conductor/commit/eea7495194edb01f6cfa86774cf2981ed012bf73))
* **styleguide:** Update C# formatting rules and guidelines for consistency ([50f39ab](https://github.com/ShalomObongo/codex-conductor/commit/50f39abf9941ff4786e3b995d4c077bfdf07b9c9))
* **styleguide:** Update C# guidelines by removing async method suffix rule and adding best practices for structs, collection types, file organization, and namespaces ([8bfc888](https://github.com/ShalomObongo/codex-conductor/commit/8bfc888b1b1a4191228f0d85e3ac89fe25fb9541))
* **styleguide:** Update C# guidelines for member ordering and enhance clarity on  string interpolation ([0e0991b](https://github.com/ShalomObongo/codex-conductor/commit/0e0991b73210f83b2b26007e813603d3cd2f0d48))

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
