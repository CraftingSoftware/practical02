# Reflection on Writing Maintainable Tests

## Describe the code that someone would write to import the `PermitManager` class. Then, describe the code someone would write to use the `PermitManager` class to issue a permit, revoke a permit, and check whether an owner can park based on their license plate number

You must write `from permit_manager import PermitManager` to import the `PermitManager` class.

Then, you need to construct a `PermitManager` object:

```python
permit_manager = PermitManager()
```

Finally, you can use the `permit_manager` to issue and revoke permits:

```python
permit_manager.issue(
    owner_id="1234567", license_plate="ABC WXYZ", make="toyota", model="camry"
)
permit_manager.revoke("1234567")
```

And to check if an owner can park:

```python
permit_manager.can_park('ABC WXYZ')
```

## Explain what the `@pytest.fixture(autouse=True)` decorator does and how the `setup` function improves the clarity of all other tests, mentioning the global-level `PermitManager` object

When a function in a pytest file is decorated by `@pytest.fixture(autouse=True)`, it will always run before (and after) every other test in the file. The `setup` function is used to construct a `PermitManager` object, which is accessible at the global level so that all tests have access to it. Notably, this `permit_manager` object is reconstructed for every test. The `setup` function improves the clarity of all other tests by obviating their need to each construct a `PermitManager` object, which is a tedious and irrelevant initialization step.

## Identify two reasons why the `test_permit_manager` test is unclear

The test name is not descriptive--it does not describe the behavior under test or the expected output. There are no comments to emphasize the behavior within the test body. There is an irrelevant detail of issuing a permit to another owner, which is not involved at all in the behavior under test.

## Propose at least one way to improve the maintainability of the `test_permit_manager` test

The test could be renamed to describe the behavior under test and the expected output. A comment could be written to describe the behavior test within the test body. The irrelevant detail could be removed.

## Explain why the `test_next_sticker_increments_next_sticker_number` test is brittle

This test is brittle because it does not test via the public API--it tests a private method called `_next_sticker`, which is just an implementation detail underlying the public API. If the `PermitManager` is refactored (e.g. `_next_sticker` is renamed or so that stickers are generated using UUIDs instead of incrementally), then this test will break even though the behavior, which is that each owner receives a unique sticker number, has not changed. This test is brittle then because it broke even though no real bugs were introduced.

## Considering the existence of the `test_issue_assigns_unique_sticker_numbers` test, determine whether the `test_next_sticker_increments_next_sticker_number` test should be removed and explain how you made this determination

Yes, `test_next_sticker_increments_next_sticker_number` can be removed. This is because the behavior expected by the user--that each owner receives a unique sticker number--is tested by `test_issue_assigns_unique_sticker_numbers` and `_next_sticker`'s ability to generate unique sticker numbers is tested through this test.
