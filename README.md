# Option C Semester Repo — Week 01 Complete Assignment (Validation)

This package gives you a **fully specified Week 01** quiz (12 tasks) so you can validate:
- GitHub Classroom autograding
- workflow + tests_bank copying
- late penalty application

## What to do (instructor)

1) Create a GitHub repo from this template (or drop these files into your semester template repo).
2) Run locally:

```bash
python tools/validate_w01_local.py
```

3) Push to GitHub and confirm Actions shows a passing run.

## Before releasing to students

Ensure `weeks/w01/answers.py` is the **student template** (stubs).  
This repo includes:
- `weeks/w01/answers_student_template.py` (stubs)
- `weeks/w01/answers_solution.py` (reference solution)

`tools/validate_w01_local.py` will restore the stubs after running the solution locally.

## Student workflow

- Read `weeks/w01/quiz.qmd`
- Implement `q01()`..`q12()` in `weeks/w01/answers.py`
- Commit + push

Autograding runs on each push.
