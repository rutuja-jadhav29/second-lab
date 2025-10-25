##  Objective
To create a reproducible MLOps workflow that automatically:

- Builds a Python project in a virtual environment  
- Executes both **Pytest** and **Unittest** suites on every push to GitHub  
- Reports results through **GitHub Actions** and artifact uploads  

---


##  Repository Structure

```bash
second-lab/
├── .github/
│ └── workflows/
│ └── test.yml # CI workflow file
│
├── src/
│ ├── Todolist.py # Core application logic
│ ├── test_pytest.py # Pytest test cases
│ ├── test_unittest.py # Unittest test cases
│ ├── requirements.txt # Dependencies
│ └── README.md
│
├── Makefile # Command shortcuts
└── README.md

```


---

##  Key Module – `Todolist.py`

Implements a simple **Task Management System** for adding, deleting, and marking tasks completed.  

| Function | Description |
|-----------|--------------|
| `add_task()` | Adds a new task and saves it to file |
| `remove_task()` | Removes a specific task by index |
| `mark_task_completed()` | Marks a task as completed |
| `display_tasks()` | Prints all existing tasks |

---

## Tests

Two frameworks ensure reliability:

### ✅ **Pytest**
- Concise, function-based tests  
- Quick validations of task addition and deletion  

### ✅ **Unittest**
- Class-based structured tests with setup/teardown  
- Ensures To-Do List operations behave consistently  

---

## Makefile Shortcuts

| Command | Description |
|----------|--------------|
| `make install` | Install dependencies |
| `make test` | Run both test frameworks |
| `make pytest` | Run only pytest |
| `make unittest` | Run only unittest |

---

## How This Repo Differs from the Professor’s

| Feature | Professor’s Repository | This Implementation |
|----------|------------------------|----------------------|
| **Code Module** | `calculator.py` (simple math) | `Todolist.py` (real-world CRUD logic) |
| **Testing** | Only Pytest demo | Dual frameworks (Pytest + Unittest) |
| **Structure** | Single flat folder | Modular `src/` folder |
| **Workflows** | One YAML | One modern CI workflow for both tests |
| **Environment** | Manual setup | Automated Makefile + requirements.txt |
| **Error Handling** | Minimal | Added validations & clear messages |
| **Artifacts** | None | Workflow logs + test reports |
| **Python Version** | 3.8 only | Compatible 3.8 – 3.11 |

---

## Results and Validation
- Every push triggers **GitHub Actions** automatically.  
- Green checks confirm successful runs for both test suites.  
- Logs and test results are available under the **Actions** tab.  

---

## Summary
This lab demonstrates how to integrate **Continuous Integration (CI)** into a Python project.  
It uses:
- Modular, testable Python code  
- Dual testing frameworks  
- Automated pipelines with GitHub Actions  

The result: a fully reproducible, continuously verified Python workflow — exactly how MLOps is done in the real world 


