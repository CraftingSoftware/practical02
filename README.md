# Writing Maintainable Tests with pytest

## Due: Tuesday, September 27th, 2022 at 2:30 pm

## Introduction

In this lab assignment, you will write maintainable tests for a parking management system. You will also assess existing tests for their maintainability and propose ways to improve their maintainability. Through this exercise, you will put into practice the following learning objective(s):

- How to run tests with pytest and analyze its results
- How to write tests with pytest that contain assertions and can expect exceptions
- How to write maintainable tests

## Instructions

Please perform each of the following steps in order.

### Analyze `permit_manager.py`

Read through the code in `permit_manager.py` and in `writing/reflection.md` describe the code that someone would write to import the `PermitManager` class. Then, describe the code someone would write to use the `PermitManager` class to issue a permit, revoke a permit, and check whether an owner can park based on their license plate. In your description, choose reasonable values for any arguments you need to supply. For example, according to the comments in `permit_manager.py`, `owner_id` is the owner's Allegheny ID. Since Allegheny IDs are seven-digit long strings, whenever you need to supply an `owner_id` to a method, choose any seven-digit long string.

### Analyze `tests/test_permit_manager.py`

Read through the test code in `tests/test_permit_manager.py`. Notice that it contains three existing tests--`test_permit_manager`, `test_next_sticker_increments_next_sticker_number`, and `test_issue_assigns_unique_sticker_numbers`--and boilerplate for four additional tests. Also notice that it contains a `setup` function that is decorated by the `@pytest.fixture(autouse=True)` decorator and that constructs a global-level `PermitManager` object. Referring to the [pytest documentation on autouse fixtures](https://docs.pytest.org/en/latest/how-to/fixtures.html#autouse-fixtures-fixtures-you-don-t-have-to-request) and asking for clarification as needed from the instructor and technical leaders, in `writing/reflection.md`, explain what the `@pytest.fixture(autouse=True)` decorator does and how the `setup` function improves the clarity of all other tests. Your response should mention the global-level `PermitManager` object.

### Assess the Maintainability of Existing Tests in `tests/test_permit_manager.py`

The `test_permit_manager` test was written to verify that the `revoke` method of the `PermitManager` class raises a `KeyError` if a permit for the owner does not exist. In `writing/reflection.md`, identify two reasons why this test is unclear. Then, in `writing/reflection.md`, propose at least one way to improve the maintainability of this test.

The `test_next_sticker_increments_next_sticker_number` test was written to verify the behavior of the `__next_sticker` method of the `PermitManager` class. In `writing/reflection.md`, explain why this test is brittle. Considering the existence of the `test_issue_assigns_unique_sticker_numbers` test, determine whether the `test_next_sticker_increments_next_sticker_number` test should be removed and explain how you made this determination. Do not actually remove the `test_next_sticker_increments_next_sticker_number` test.

### Write Maintainable Tests for `permit_manager.py`

Using the boilerplate as a guide, in `tests/test_permit_manager.py`, write maintainable tests for the following behaviors of the `PermitManager` class in `permit_manager.py`:

- **Test 1**: _Given_ a permit has not been issued to an owner, _then_ the owner should not be able to park.
- **Test 2**: _When_ a permit is issued to an owner, _then_ the owner should be able to park.
- **Test 3**: _Given_ a permit is issued to an owner, _when_ trying to issue a permit again to the owner, _then_ a `ValueError` is raised.
- **Test 4**: _Given_ a permit is issued to an owner, _when_ the permit is revoked from the owner, _then_ the owner should not be able to park.

All maintainable tests must:

- Contain an assertion
- Be complete and concise
- Be structured to emphasize behavior
- Have names that describe the behavior under test and the expected behavior

In your tests, whenever needed, please choose reasonable values (such as `"ABC WXYZ"` for a license plate) for any arguments you need to supply.

## GatorGrade

You can check the baseline requirements of this project by running department's assignment checking `gatorgrade` tool To use `gatorgrade`, you first need to make sure you have Python installed. Then, if you haven't done so already, you need to install `gatorgrade`:

- [install `pipx`](https://pypa.github.io/pipx/installation/)
- install `gatorgrade` with `pipx install gatorgrade`

Finally, you can run `gatorgrade`:

`gatorgrade --config config/gatorgrade.yml`

## Receiving Assistance

If you are having trouble completing any part of this assignment, then please talk with either the course instructor or a student technical leader during the lab session. Alternatively, you may ask questions in the Discord channel for this course. Finally, you can schedule a meeting during the course instructor's office hours.

## Assessment Strategy

This assignment will be assessed based on the following components:

- **Percentage of Passing GatorGrader Checks**: If source code is required, you should repeatedly update the implementation of your source code until it passes all of the GatorGrader checks by, for instance, producing the correct output. If technical writing is required, you should repeatedly revise your technical writing until it also passes all of GatorGrader's checks about, for instance, the length of its content.
- **Percentage of Passing GitHub Actions Checks**: You will receive checkmarks for any additional checks on source code and/or technical writing, other than the "Run GatorGrader" check, that are encoded in GitHub Actions. You will receive a checkmark for each passing GitHub Actions check. As with the previous grading component, you are encouraged to repeatedly amend your source code and/or technical writing until all of your GitHub Actions checks pass.

  - Please note that the "Check Spelling" GitHub Actions check may flag proper nouns or other real words if the dictionary it uses does not contain them. If your "Check Spelling" GitHub Actions check is failing due to a correctly spelled word being incorrectly flagged as "unknown" by CSpell, you will need to add the word to the list of words in `.github/cspell.json`.

- **Mastery of Software Engineering Concepts and Skills**: You will receive a checkmark for demonstrating mastery of each of the following concepts and skills of software engineering exercised in this assignment that is not checked by GatorGrader. If you receive checkmarks for all of the following concepts and skills and have all GatorGrader checks pass, you will know that you have mastered all of the learning objectives of this assignment. For this assignment, you must:

  - Make small, focused commits
  - Write commit messages that abide by [the seven rules of a great Git commit](https://cbea.ms/git-commit/message)
  - Correctly explain what the `@pytest.fixture(autouse=True)` decorator does
  - Correctly identify two reasons why `test_permit_manager` is unclear
  - Correctly explain why `test_next_sticker_increments_next_sticker_number` is brittle
  - Write tests that are maintainable
