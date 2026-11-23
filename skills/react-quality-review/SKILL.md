---
name: react-quality-review
description: Audit React and Next.js code for performance, rendering correctness, accessibility and regression risks. Use for React component reviews, slow interfaces, bundle and hydration concerns, or design-quality checks; deliver evidence-based fixes without modifying projects until approved.
---

# React Quality Review

1. Identify React/Next.js version, rendering strategy, deployment constraints and relevant source files. Do not assume Next.js-only APIs work in Vite.
2. Examine asynchronous request waterfalls, redundant fetches, import/bundle cost, expensive renders, effect dependencies, unstable state, hydration mismatch, and animation lifecycle.
3. Examine UI usability: semantic controls, keyboard/focus navigation, contrast, RTL layout, mobile breakpoints, reduced motion and loading/error states.
4. For each finding, cite file and line when available, severity, reproduced evidence versus hypothesis, smallest safe change, regression risk and verification test.
5. Preserve approved design, persistence logic, API behavior and existing functionality. Avoid unsolicited refactors, new dependencies or automated code changes.
6. Provide a prioritized review and test plan. Ask for approval before editing, merging or deploying.

This is an original, instruction-only adapter. It does not bundle or reproduce Vercel's rule corpus. See `references/UPSTREAM.md` for provenance and limits.
