# External skills intake — design, review and mobile wave

Date: 2026-11-23. Status: **quarantined / unapproved**. No imported instruction was executed.

## Selected imports

| Source / skill | Immutable upstream commit | License evidence | Scope / reason | Remaining concerns |
|---|---|---|---|---|
| anthropics/skills — frontend-design | `e4bb5d960d87126ff3b3a8af1a104b7db67560ba` | Per-skill Apache-2.0 `LICENSE.txt` preserved | Distinctive art direction, typography, layout and non-generic visual design | Guidance-only; evaluate quality in real builds and avoid conflicting with existing design brief |
| getsentry/skills — find-bugs | `a582c51ee29d0f35e6ac321340796f77d43da733` | Repository Apache-2.0 retained in prior intake | Structured bug/security review checklist | Uses Git/GitHub CLI commands; review tool permissions and avoid assuming branch name/default branch |
| getsentry/skills — code-review | same pinned commit | Repository Apache-2.0 retained in prior intake | Code review for security, performance, tests and architecture | Some guidance is Sentry/Django-specific; adapt scope instead of treating it as universal truth |
| expo/skills — expo-design-system | `88d9bd79f3fa8452a778fbac65bae162c0b32ce4` | Expo plugin MIT license preserved | Native mobile design tokens, reusable components, anti-pattern audit | Expo/React Native only; avoid introducing second theme system; test real devices |

Imported 8 new files. Existing Sentry Apache license reused from already mirrored source. Total provenance manifest: 68 files across 7 upstream repositories, with immutable source commits and Git blob SHAs.

## Rejected / deferred source decisions

- Vercel Agent Skills remain unimported: no repository-level license file was found in the inspected tree. Individual frontmatter license declarations do not by themselves settle all redistribution questions for the full bundle. Keep evaluating only after confirming rights for every selected file.
- Do not bulk-import entire Anthropic, Expo, Sentry or OpenAI repositories. Select individual skills with clear applicability and license evidence.
- The community Web Design Studio source was already imported under MIT; no new scripts or templates from its much larger repository are included in this wave.

## Safety boundaries

- All files remain in `intake/`, outside the agent-discovered production `skills/` folder.
- No automatic installation, plugin/MCP setup, credentials, write-enabled target repo access or deployment.
- The provenance validator verifies byte identity only; it is not a malware scanner.
- No new runtime test was necessary for this text/reference-only intake change. Prior unrelated passing GSAP/Sentry smoke tests were not repeated.

## Admission status

All four newly selected skills remain `under_review`. Scores are intentionally unassigned. The 11 mandatory gates must each pass with evidence and a named reviewer, and the final weighted score must be at least 90/100. No external skill is approved by this import.
