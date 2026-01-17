[![CI](https://github.com/lopezviktor/qa-automation-framework/actions/workflows/ci.yml/badge.svg)](https://github.com/lopezviktor/qa-automation-framework/actions/workflows/ci.yml)

# QA Automation Framework (PyTest)

This repository contains a QA Automation framework built with **Python** and **PyTest**, focused on **API testing**, **contract validation**, and **CI integration**.

The project is designed to demonstrate how automated tests can be used to validate API behaviour, data integrity, and contracts in a production-like environment.

---

## 🎯 Project Goals

- Validate REST API behaviour using automated tests
- Apply **contract testing** with JSON Schema
- Cover **positive and negative scenarios**
- Ensure reproducibility using **CI (GitHub Actions)**
- Follow clean, maintainable QA automation practices

---

## 🧪 What is tested

The framework currently validates the following aspects of a public REST API:

- API availability and status codes
- Correct response structure and data types
- Contract compliance using JSON Schema
- Behaviour for non-existent resources (negative testing)
- Multiple inputs using test parametrization

---

## 🛠️ Tech Stack

- **Python 3.13**
- **PyTest**
- **Requests**
- **jsonschema**
- **GitHub Actions (CI)**

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
│       └── ci.yml
├── README.md
```

---

## ▶️ How to run the tests locally

1. Create and activate a virtual environment:
    ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```

2. Install dependencies:
   ```bash
   pip install pytest requests jsonschema
   ```

3. Run the test suite:
   ```bash
   pytest -q
   ```

---

## Continuous Integration

All tests are automatically executed on every push and pull request using GitHub Actions.

This ensures:
- Environment-independent execution (Linux runner)
- Early detection of breaking changes
- Consistent and reproducible test results

---

## 🚀 Future Improvements

- API schema validation for additional endpoints
- Test markers (smoke, regression)
- Retry and timeout handling
- Security-focused API tests
- Integration with Jenkins

----

## 👨🏻‍🎓 Author

Victor López
QA Automation / Software Engineering Student