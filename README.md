![Python](https://img.shields.io/badge/Python-3.10%2B-blue.svg)
![pytest](https://img.shields.io/badge/tests-pytest-green.svg)
![License](https://img.shields.io/badge/license-MIT-yellow.svg)

## Description

Homework №3 for the module **"Working with date, time and advanced string processing"**.  
This repository contains Python implementations and tests for tasks from **Module 3** of the program *"Algorithms and Data Structures"*.

### Implemented tasks:

1. **Days from Today**
   - Function: `get_days_from_today(date)`
   - Calculates the number of days between a given date (`YYYY-MM-DD`) and today's date.

2. **Lottery Number Generator**
   - Function: `get_numbers_ticket(min, max, quantity)`
   - Returns a sorted list of unique random numbers within the specified range.

3. **Phone Number Normalizer** *(optional)*
   - Function: `normalize_phone(phone_number)`
   - Normalizes phone numbers into international format `+38...` for SMS distribution.

---

## Project structure

```bash
goit-algo-hw-03/
├── src/goit_algo_hw_03/
│   ├── task1_days_from_today.py
│   ├── task2_lottery.py
│   └── task3_normalize_phone.py
│
├── tests/
│   ├── test_task1_days_from_today.py
│   ├── test_task2_lottery.py
│   └── test_task3_normalize_phone.py
│
├── README.md
└── pyproject.toml

