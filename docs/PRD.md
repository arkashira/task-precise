# Product Requirements Document – Task Precise CLI

**Project:** `task-precise`  
**Owner:** Senior Product / Engineering Lead  
**Date:** 2026‑06‑22  
**Version:** 1.0

---

## 1. Problem Statement

Axentx’s AI‑inference platform exposes a REST API that accepts “tasks” (e.g., inference jobs, fine‑tuning requests, data‑preprocessing jobs).  
Current onboarding for external developers is manual: they must:

1. Sign up via a web portal.
2. Copy an API key from the portal.
3. Manually craft HTTP requests or write boilerplate code.

This friction:

- **Delays** time‑to‑value for new users.
- **Increases support tickets** for “how to submit a task”.
- **Creates security gaps** when API keys are stored in ad‑hoc scripts.

We need a lightweight, reproducible, and secure command‑line interface that streamlines registration, key management, and task submission.

---

## 2. Target Users

| Persona | Role | Pain Points | Desired Outcome |
|---------|------|-------------|-----------------|
| **Developer** | Backend engineer, data scientist | • Time‑consuming onboarding<br>• Manual API key handling | • One‑click registration<br>• Secure key storage |
| **DevOps Engineer** | CI/CD pipeline integrator | • Need to automate task submission in pipelines | • CLI that can be scripted, supports env vars |
| **Product Manager** | AI product owner | • Track task status and metrics | • CLI that can query status and export logs |

**Primary audience:** Developers and DevOps engineers who will interact with Axentx’s inference API from scripts, CI/CD pipelines, or local machines.

---

## 3. Goals & Success Metrics

| Goal | Success Metric | Target |
|------|----------------|--------|
| **Reduce onboarding friction** | Avg. time from first login to first task submission | < 5 min |
| **Secure key handling** | Zero incidents of key leakage in support tickets | 0 incidents |
| **High adoption** | % of new API users who install the CLI | 80 % |
| **Reliability** | Task submission success rate | ≥ 99.5 % |
| **Developer satisfaction** | NPS score for CLI | ≥ 70 |

---

## 4. Key Features (Prioritized)

| Rank | Feature | Description | Acceptance Criteria |
|------|---------|-------------|---------------------|
| 1 | **Registration & API Key Generation** | `task-precise register` prompts for email/username, creates account via Axentx API, returns API key. | • CLI prompts user.<br>• Stores key in `~/.task-precise/config.yaml`. |
| 2 | **Secure Key Storage** | Keys encrypted with OS keychain (macOS Keychain / Windows Credential Manager / Linux libsecret). | • Key retrieval works across OS.<br>• No plaintext key in config. |
| 3 | **Task Submission** | `task-precise submit <task-spec.json>` posts task to Axentx API. | • Returns task ID.<br>• Handles HTTP errors gracefully. |
| 4 | **Status Polling** | `task-precise status <task-id>` shows current status, logs, and result URL. | • Polls until terminal state or timeout.<br>• Displays progress bar. |
| 5 | **Configuration & Environment Variables** | Support `TASK_PRECIS_API_KEY`, `TASK_PRECIS_ENDPOINT`. | • CLI reads env vars if present.<br>• Overrides config file. |
| 6 | **Help & Documentation** | `task-precise --help` lists commands, flags, and examples. | • Help output is clear and concise. |
| 7 | **Logging & Verbosity** | `-v/--verbose` prints detailed logs. | • Logs include request/response headers. |
| 8 | **Error Handling & Retry** | Automatic retries for transient network errors. | • Exponential backoff, max 3 retries. |
| 9 | **Extensibility Hooks** | Plugin system for custom task types. | • CLI can load plugins from `~/.task-precise/plugins`. |
| 10 | **Unit & Integration Tests** | 90 % code coverage, CI pipeline. | • All tests pass on PR. |

---

## 5. Success Metrics (Detailed)

| Metric | Definition | Measurement |
|--------|------------|-------------|
| **Onboarding Time** | Time from first CLI install to first successful task submission. | `time_to_first_task` (seconds) |
| **Key Leakage Incidents** | Number of support tickets citing accidental key exposure
