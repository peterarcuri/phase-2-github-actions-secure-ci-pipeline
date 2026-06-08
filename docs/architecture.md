# CI Pipeline Architecture

## Overview

This project implements a security-focused Continuous Integration (CI) pipeline using GitHub Actions. The pipeline automatically validates code quality, functionality, and security whenever code is pushed to the repository or submitted through a Pull Request.

The goal is to demonstrate DevSecOps principles by integrating security controls directly into the software development lifecycle.

---

## Architecture Diagram

```text
Developer
    │
    ▼
Git Commit
    │
    ▼
Git Push / Pull Request
    │
    ▼
GitHub Repository
    │
    ▼
GitHub Actions Workflow
    │
    ├── Install Dependencies
    │
    ├── Run Unit Tests (Pytest)
    │
    ├── Run Linting (Ruff)
    │
    ├── Run SAST Scan (Bandit)
    │
    ├── Run Dependency Audit (pip-audit)
    │
    ▼
Pass / Fail Decision
    │
    ▼
Merge Approved or Rejected
```

---

## Components

### GitHub Actions

GitHub Actions serves as the automation engine responsible for executing the CI workflow whenever a trigger event occurs.

Workflow triggers include:

* Push to main branch
* Pull Requests targeting main

---

### Pytest

Pytest validates application functionality through automated unit tests.

Responsibilities:

* Verify application behavior
* Prevent regressions
* Ensure code changes do not break existing functionality

---

### Ruff

Ruff performs static code quality analysis.

Responsibilities:

* Detect style violations
* Enforce coding standards
* Improve maintainability

---

### Bandit

Bandit performs Static Application Security Testing (SAST).

Responsibilities:

* Detect insecure coding patterns
* Identify common Python security issues
* Support secure software development practices

---

### pip-audit

pip-audit scans project dependencies for known vulnerabilities.

Responsibilities:

* Detect vulnerable packages
* Validate dependency security
* Improve software supply chain security

---

## Pipeline Execution Flow

1. Developer pushes code to GitHub.
2. GitHub Actions workflow is triggered.
3. Dependencies are installed.
4. Unit tests execute.
5. Linting checks run.
6. Security scans execute.
7. Dependency audit executes.
8. Results are reported.
9. Merge decision is based on pipeline success.

---

## Benefits

* Automated quality assurance
* Early vulnerability detection
* Consistent validation process
* Reduced manual review effort
* Improved software security posture
* Demonstration of Shift Left Security practices
