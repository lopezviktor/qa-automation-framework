[![CI](https://github.com/lopezviktor/qa-automation-framework/actions/workflows/ci.yml/badge.svg)](https://github.com/lopezviktor/qa-automation-framework/actions/workflows/ci.yml)

# QA Automation Framework (PyTest)

<p align="center">
  <img src="https://skillicons.dev/icons?i=python,githubactions&perline=6" />
</p>

A lightweight **QA Automation framework** built with **Python** and **PyTest** to validate REST APIs through **automated testing**, **contract validation**, **basic security checks**, and **CI pipelines**.

This project is designed as a **realistic example of how QA Automation / SDET practices are applied in production environments**, focusing on fast feedback, system reliability, and maintainability.

---

## 🎯 Project Purpose

The goal of this project is to demonstrate how automated tests can protect an API-based system by:

- Detecting breaking changes early
- Enforcing API contracts between services
- Validating error handling and security-related behaviour
- Providing fast and reliable feedback through CI

Rather than testing everything on every change, the framework follows a **layered testing strategy** similar to what is used in professional software teams.

---

## 🧪 Testing Strategy

The test suite is organised using **PyTest markers**, allowing selective execution depending on the context:

- **Smoke tests**  
  Fast, critical checks executed on every push and pull request to ensure the API is reachable and core endpoints respond correctly.

- **Regression tests**  
  Broader functional coverage, including parametrised tests and negative scenarios, executed separately to avoid slowing down daily development.

- **Contract tests**  
  JSON Schema validation to ensure API responses maintain a stable structure and do not introduce breaking changes.

- **Security-oriented tests**  
  Basic checks to ensure error responses do not leak internal implementation details such as stack traces, system paths, or database errors.

---

## 🔄 CI Design

The project uses **GitHub Actions** with two complementary workflows:

- **CI (Push / Pull Request)**  
  Runs **smoke tests only** to provide fast feedback and block breaking changes early.

- **Nightly Regression (Scheduled / Manual)**  
  Runs **regression + contract + security** test suites to provide deeper coverage without impacting developer productivity.

This separation reflects a common CI strategy used in medium-to-large software teams.

---

## 📊 Test Reports

Smoke test executions generate **JUnit XML reports**, which are:

- Produced automatically during CI runs
- Uploaded as **CI artifacts** for traceability
- Kept out of the Git repository to avoid committing generated files

This allows teams to inspect test results without polluting the codebase.

---

## 🛠️ Tech Stack

- **Python 3.13**
- **PyTest**
- **Requests**
- **jsonschema**
- **GitHub Actions**

---

## 🗂️ Project Structure

```text
qa-automation-framework/
├── tests/
│   ├── api/
│   │   └── test_posts_api.py
│   ├── schemas/
│   │   └── post_schema.py
│   ├── conftest.py
│   └── test_health.py
├── .github/
│   └── workflows/
│       ├── ci.yml
│       └── nightly.yml
├── README.md
```

---

## ▶️ Running the Tests Locally

1. Create and activate a virtual environment:
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```

2. Install dependencies:
   ```bash
   pip install pytest requests jsonschema
   ```

3. Run the full test suite:
   ```bash
   pytest
   ```

4. Run specific test layers:
   ```bash
   pytest -m smoke
   pytest -m regression
   pytest -m contract
   pytest -m security
   ```

---

## 🔍 Key Engineering Decisions

- Smoke tests run on every push to provide fast feedback
- Heavier test suites are executed nightly to maximise coverage without slowing development
- API contracts are enforced through schema validation
- Security checks focus on safe failure and information disclosure prevention
- Test reports are handled as CI artifacts instead of committed files

---

## 🚀 Roadmap

- Add authentication-aware API tests
- Extend schema validation to additional endpoints
- Introduce flaky test detection
- Add performance-related API checks

---

## 👨🏻‍🎓 Author

**Victor López**  
QA Automation / Software Engineering Student