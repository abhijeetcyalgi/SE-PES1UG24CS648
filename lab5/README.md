# Lab 5: Static Code Analysis

## Overview
This laboratory assignment enhances Python code quality, security, and PEP 8 style by using static code analysis tools (**Pylint**, **Bandit**, and **Flake8**) on `bank_account_system.py`.

## Tools Used
* **Pylint (v4.1.3):** Strict code reviewer checking logic errors, code quality, design smells, and computing a code score out of 10.
* **Bandit (v1.9.4):** Security scanner targeting Common Weakness Enumerations (CWEs), dangerous function calls, and cryptographic vulnerabilities.
* **Flake8 (v7.4.1):** Style and syntax checker enforcing PEP 8 guidelines, line lengths, and unused symbols.

## Lab Execution & Results

### 1. Initial State (Before Fixes)
* **Pylint Score:** `5.62 / 10` (Multiple warnings: mutable default argument, bare except, eval-used, missing docstrings, invalid function naming, unmanaged open calls)
* **Bandit Findings:** `6 issues` (2 High, 1 Medium, 3 Low: shell injection, weak MD5 hash, unsafe eval, bare except pass, insecure random, hardcoded secret)
* **Flake8 Violations:** `7 violations` (unused imports, long lines > 79 chars, bare except, unused local variables, comparison to None, missing final newline)

### 2. Final State (After Fixes)
* **Pylint Score:** **`10.00 / 10`** (Perfect rating, exceeding the >9.5 requirement)
* **Bandit Findings:** **`0 issues`** (All security issues completely resolved)
* **Flake8 Violations:** **`0 violations`** (100% PEP 8 compliant)

## Deliverables in this Directory
* `bank_account_system.py`: Fully cleaned, refactored, and secured Python module.
* `issues.md`: Detailed documentation table of all identified issues, line numbers, and resolution approaches.
* `reflection.md`: In-depth answers to the 4 lab reflection questions on static analysis.
* `pylint_report.txt` / `pylint_report_before.txt` / `pylint_report_after.txt`: Pylint reports before and after.
* `bandit_report.txt` / `bandit_report_before.txt` / `bandit_report_after.txt`: Bandit security reports before and after.
* `flake8_report.txt` / `flake8_report_before.txt` / `flake8_report_after.txt`: Flake8 style reports before and after.

## Verification Commands
To reproduce and verify the static analysis reports locally:
```bash
# Run script
python bank_account_system.py

# Run Pylint (Rating: 10.00/10)
pylint bank_account_system.py

# Run Bandit (0 issues)
bandit -r bank_account_system.py

# Run Flake8 (0 issues)
flake8 bank_account_system.py
```
