# XPATH-Injection-Script

This repository contains a small Python script that demonstrates **XPath Injection** on an XML-backed login flow.

## What is XPath Injection?

XPath Injection happens when user input is concatenated directly into an XPath expression. An attacker can inject XPath syntax to alter the query logic and bypass authentication checks.

Example vulnerable query pattern:

```xpath
//user[username/text()='INPUT_USERNAME' and password/text()='INPUT_PASSWORD']
```

If the password input is injected with `' or '1'='1`, the final expression can become logically true.

## Files

- `/tmp/workspace/Jorge2033/XPATH-Injection-Script/xpath_injection.py`: demo script with vulnerable and safe modes.
- `/tmp/workspace/Jorge2033/XPATH-Injection-Script/requirements.txt`: Python dependency file.

## Setup

```bash
cd /tmp/workspace/Jorge2033/XPATH-Injection-Script
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Usage

### 1) Normal login attempt

```bash
python xpath_injection.py --username admin --password admin123
```

### 2) Injection against vulnerable mode (default)

```bash
python xpath_injection.py --username admin --password "' or '1'='1"
```

The vulnerable mode builds the XPath query via string concatenation, so injected syntax changes query behavior.

### 3) Safe mode (parameterized XPath)

```bash
python xpath_injection.py --safe --username admin --password "' or '1'='1"
```

Safe mode uses XPath variable binding and prevents the injection payload from changing query logic.

## Notes

This project is for educational and authorized security testing only.
