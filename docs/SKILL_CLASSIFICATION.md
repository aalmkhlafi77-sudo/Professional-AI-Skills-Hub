# Skill classification and installation readiness

Classification date: 2026-11-23. This is an inventory, not an approval or installation record.

## Categories

| Category | Sources | Current decision |
|---|---|---|
| Motion and cinematic UI | greensock/gsap-skills; zubair-trabzada/scroll-cinematic-claude | GSAP under review; cinematic candidate rejected |
| Web design | MustBeSimo/web-design-studio | Under review |
| Frontend development | vercel-labs/agent-skills | Under review |
| Browser testing | microsoft/playwright-cli; vercel-labs/agent-browser; lackeyjb/playwright-skill | Under review; compare official implementations first |
| Mobile development | expo/skills | Under review |
| Databases | supabase/agent-skills | Under review; PostgreSQL-specific |
| Monitoring and quality | getsentry/skills | Under review |
| Engineering workflows | obra/superpowers | Under review; verify approval gates |
| General/reference | openai/plugins; anthropics/skills | Under review; select individual skills only |
| Security and skill auditing | skills/skill-source-auditor (local) | Authored locally; packaging and runtime compatibility not verified |

## Installation queues

### Ready for ChatGPT and Codex
None verified. No external candidate currently passes the repository admission gates. Do not claim that repository presence means installed.

### Preparation queue
1. Validate and package local `skill-source-auditor` separately for each supported target.
2. Audit individual official skills, starting with GSAP, Vercel React guidance, and Microsoft browser testing.
3. Check exact immutable source, license, dependency chain, script behavior, test evidence, and ChatGPT/Codex installation requirements.
4. Record distinct readiness for ChatGPT and Codex. Compatibility with one does not establish compatibility with the other.
5. Move a skill to approved only after >=90/100, every mandatory gate PASS, reproducible sandbox tests, and named human reviewer.

### Rejected / quarantined
- `zubair-trabzada/scroll-cinematic-claude`: rejected in source catalog; never install without a new complete security review.

## Safety and execution
Classification does not authorize third-party script execution, remote installers, credential access, deployment, or automatic merges. See `docs/ADMISSION_POLICY.md` and `catalog/candidates.json`.
