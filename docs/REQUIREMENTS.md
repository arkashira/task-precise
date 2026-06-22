# Requirements.md

## Task Precise CLI

Task Precise is a lightweight command‑line interface that allows users to register, obtain an API key, and submit tasks to the Task Precise backend service.  
The CLI is intended to be cross‑platform, secure, and easy to use while providing a robust user experience.

---

## 1. Functional Requirements

| ID   | Requirement | Description |
|------|-------------|-------------|
| **FR‑1** | **User Registration** | The CLI must allow a new user to register by providing an email address and password. |
| **FR‑2** | **Input Validation** | The CLI must validate the email format and enforce a minimum password strength (≥ 8 characters, one uppercase, one lowercase, one digit, one special character). |
| **FR‑3** | **Verification Email** | Upon successful registration, the system must send a verification email containing a unique link. |
| **FR‑4** | **Account Verification** | The user must be able to verify their account by clicking the link, which activates the account on the backend. |
| **FR‑5** | **Login** | The CLI must support login with email and password. |
| **FR‑6** | **API Key Issuance** | After a successful login, the backend must return a 32‑character hexadecimal API key. |
| **FR‑7** | **Secure Storage** | The API key must be stored locally in an encrypted form (e.g., OS keychain or file encrypted with a user‑specific key). |
| **FR‑8** | **Task Submission** | The CLI command `task-precise submit <description>` must send a task to the backend. |
| **FR‑9** | **Task Validation** | The CLI must validate that the task description is non‑empty and ≤ 500 characters. |
| **FR‑10** | **Task Response** | On successful submission, the CLI must display the task ID and initial status. |
| **FR‑11** | **Status Query** | The CLI command `task-precise status <task_id>` must retrieve and display the current status of the specified task. |
| **FR‑12** | **Cancellation** | The CLI command `task-precise cancel <task_id>` must request cancellation of the specified task and report the outcome. |
| **FR‑13** | **Task Listing** | The CLI command `task-precise list` must display the last 20 tasks submitted by the user, sorted by submission time. |
| **FR‑14** | **Configuration Management** | The CLI command `task-precise config` must allow viewing and editing of local configuration (e.g., API endpoint, log level). |
| **FR‑15** | **Help & Usage** | The CLI must provide comprehensive help text for all commands (`--help`). |

---

## 2. Non‑Functional Requirements

| ID   | Requirement | Description |
|------|-------------|-------------|
| **NFR‑1** | **Performance** | API calls for status queries must return within **2 s**; task submissions must return within **5 s** under normal network conditions. |
| **NFR‑2** | **Security** | • API key must be stored encrypted.<br>• All network traffic must use HTTPS.<br>• Passwords are never logged. |
| **NFR‑3** | **Authentication** | The backend uses JWT tokens with a 24 h expiration; the CLI must refresh tokens automatically. |
| **NFR‑4** | **Reliability** | The CLI must retry failed HTTP requests up to **3** times with exponential back‑off (initial 1 s). |
| **NFR‑5** | **Logging** | Logs are written to
