# Phase 2 — GitHub Actions Secure CI Pipeline

## Project Overview

A security-focused Continuous Integration (CI) pipeline built with GitHub Actions that demonstrates modern DevSecOps practices by integrating automated testing, code quality checks, and security scanning directly into the development workflow.

This project follows the "Shift Left Security" approach by identifying vulnerabilities and quality issues early in the software development lifecycle before code reaches production.

The pipeline automatically performs:

* Unit testing
* Code linting
* Static security analysis
* Dependency vulnerability scanning
* Pull Request validation

---

# Objectives

The primary objectives of this project are:

* Build a production-style CI pipeline using GitHub Actions
* Automate testing and validation of Python applications
* Integrate security controls directly into the CI workflow
* Demonstrate Shift Left Security principles
* Enforce code quality standards
* Detect vulnerable dependencies before deployment
* Gain practical experience with DevSecOps automation

---

# Skills Demonstrated

This project demonstrates practical experience with:

### DevOps

* Continuous Integration (CI)
* GitHub Actions workflow automation
* Pipeline design and maintenance
* Automated testing

### DevSecOps

* Shift Left Security
* Static Application Security Testing (SAST)
* Dependency vulnerability scanning
* Security gate implementation
* Secure software development lifecycle practices

### Python

* Unit testing with Pytest
* Dependency management
* Virtual environments
* Project structure organization

### Git & Collaboration

* Branch-based development
* Pull Request validation
* Automated quality gates
* CI-driven code review processes

---

# Project Structure

```text
phase-2-github-actions-secure-ci-pipeline/
├── .github/
│   └── workflows/
│       └── secure-ci.yml
├── app/
│   ├── __init__.py
│   └── main.py
├── tests/
│   ├── __init__.py
│   └── test_main.py
├── docs/
├── config/
├── sample-output/
├── screenshots/
├── requirements.txt
├── pytest.ini
├── README.md
└── .gitignore
```

---

# Security Controls

The CI pipeline includes multiple automated security controls:

| Control                  | Tool           | Purpose                                   |
| ------------------------ | -------------- | ----------------------------------------- |
| Unit Testing             | Pytest         | Validate application functionality        |
| Code Quality             | Ruff           | Enforce coding standards                  |
| Static Security Analysis | Bandit         | Detect insecure coding practices          |
| Dependency Scanning      | pip-audit      | Identify known vulnerable packages        |
| Pull Request Validation  | GitHub Actions | Prevent unverified code from being merged |

These controls help reduce risk by ensuring security and quality checks occur automatically with every code change.

---

# CI Pipeline Workflow

The GitHub Actions workflow executes the following stages:

```text
Developer Push
        │
        ▼
GitHub Actions Trigger
        │
        ▼
Install Dependencies
        │
        ▼
Run Unit Tests
        │
        ▼
Run Ruff Linting
        │
        ▼
Run Bandit Security Scan
        │
        ▼
Run Dependency Audit
        │
        ▼
Pipeline Passes
```

If any stage fails, the workflow stops and reports the issue for remediation.

---

# Local Setup

Clone the repository:

```bash
git clone <repository-url>
cd phase-2-github-actions-secure-ci-pipeline
```

Create a virtual environment:

```bash
python3 -m venv venv
```

Activate the environment:

```bash
source venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

# Running Tests

Execute the unit test suite:

```bash
pytest
```

Expected output:

```text
3 passed
```

---

# Running Security Scans

### Ruff Code Quality Check

```bash
ruff check .
```

### Bandit Static Security Analysis

```bash
bandit -r app
```

### Dependency Vulnerability Scan

```bash
pip-audit
```

These scans can be run locally before pushing code to GitHub.

---

# GitHub Actions

The workflow is defined in:

```text
.github/workflows/secure-ci.yml
```

Workflow triggers include:

* Pushes to main
* Pushes to develop
* Feature branch updates
* Pull Requests targeting main

The pipeline automatically performs:

* Dependency installation
* Unit testing
* Linting
* Security scanning
* Dependency auditing

This ensures consistent validation across all development activities.

---

# Screenshots

## Project Structure

Shows the overall repository layout including application code, GitHub Actions workflow, tests, documentation, and security configuration.

![Project Structure](screenshots/project-structure-ci-pipeline.png)

---

## GitHub Actions Workflow Configuration

Displays the GitHub Actions workflow responsible for executing automated testing, linting, and security scans.

![Workflow YAML](screenshots/workflow-yaml-ci-pipeline.png)

---

## Successful Pytest Execution

Demonstrates successful execution of the automated unit test suite.

![Pytest Success](screenshots/pytest-success-ci-pipeline.png)

---

## Ruff Code Quality Validation

Shows the Ruff linter validating code quality and style standards.

![Ruff Success](screenshots/ruff-success-ci-pipeline.png)

---

## Bandit Security Scan

Demonstrates Static Application Security Testing (SAST) using Bandit to identify insecure coding patterns and common Python security issues.

![Bandit Security Scan](screenshots/bandit-scan-ci-pipeline.png)

---

## Dependency Vulnerability Scan

Shows dependency auditing with pip-audit to detect vulnerable third-party packages and software supply chain risks.

![pip-audit Scan](screenshots/pip-audit-scan-ci-pipeline.png)

---

## Successful GitHub Actions Pipeline

Demonstrates a successful end-to-end CI pipeline execution with all quality and security gates passing.

![GitHub Actions Success](screenshots/github-actions-success-ci-pipeline.png)


---

# Lessons Learned

Key lessons gained from this project include:

* Designing automated CI workflows
* Integrating security controls into developer pipelines
* Using GitHub Actions for workflow automation
* Implementing Shift Left Security principles
* Managing Python testing frameworks
* Automating dependency vulnerability management
* Building repeatable DevSecOps processes

---

# Future Improvements

Planned enhancements include:

* Secret scanning with TruffleHog or Gitleaks
* Software Composition Analysis (SCA) reporting
* Container image vulnerability scanning
* Automated code coverage reporting
* Security policy enforcement gates
* GitHub Advanced Security integration
* SARIF reporting and dashboard integration
* Automated deployment stages (CD)
* Infrastructure as Code validation
* Multi-environment pipeline support

```
```
