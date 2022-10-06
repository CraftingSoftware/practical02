# Practical 02: Setting Up GitHub Actions

## Due: October 7th, 2022 by midnight

## Introduction

In this practical assignment, you will set up GitHub Actions to run markdown linting, spell check, Python program, `sort.py`, and its test cases from lab 03\. By the end of this exercise, you should have the tools and knowledge to be able to demonstrate mastery of the following essential technical skills of software engineering:

- How to set up GitHub Actions workflow

Please refer to [GitHub Actions documentation](https://docs.github.com/en/actions/learn-github-actions) as needed.

## Instructions

### Setting Up GitHub Actions

Create a `.yml` file inside `.github` directory of your practical repository. Create a GitHub Actions workflow with three jobs:

1. `markdown` with `name: Lint Markdown` that runs linting on Markdown documents
2. `spelling` with `name: Check Spelling` that runs spell-checker on Markdown documents.
3. `python` with `name: Run Python` that uses `poetry` to run Python program called `permit_manager.py` and the test suite in the `test_permit_manager.py`.
4. `gatorgrade` with `name: Run GatorGrader` that runs `gatorgrade`.

### Reflection

Answer all questions in `writing/reflection.md`. As you do, commit your changes using best commit practices. Instead of creating a commit at the end with the message, "Answer reflection questions", you should commit after answering each question and describe your changes in the commit messages.

## Running GatorGrader

You can gain an approximation of your progress on this assignment by running [GatorGrader](https://github.com/GatorEducator/gatorgrader) locally. You do need to have `gatorgrade` and Python installed to be able to run this command (see instructions above).

```bash
gatorgrade --config config/gatorgrade.yml
```

## Receiving Assistance

If you are having trouble completing any part of this project, then please talk with either the course instructor or a student technical leader during the practical session. Alternatively, you may ask questions in the Discord channel for this course. Finally, you can schedule a meeting during the course instructor's office hours.

## Practical Assessment

The grade that a student receives on this practical assignment is a checkmark grade (0 or 1) and is based on:

- **GitHub Actions CI Build Status**: Students are encouraged to repeatedly try to complete the assignment until it passes all GitHub Actions jobs. Students will receive a checkmark grade if their last before-the-deadline build passes and a green ✔ appears in their GitHub commit log instead of a red ✗.

Students will receive 1 if their solution passes all GatorGrader checks and receives a green ✔ in their last commit.

All grades for this project will be reported through a student's GitHub gradebook repository.
