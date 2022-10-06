import pytest
from permit_manager import PermitManager

permit_manager = None


@pytest.fixture(autouse=True)
def setup():
    global permit_manager
    permit_manager = PermitManager()


def test_permit_manager():
    permit_manager.issue(
        owner_id="7654321", license_plate="CBA ZYXW", make="toyota", model="corolla"
    )
    with pytest.raises(KeyError):
        permit_manager.revoke(owner_id="1234567")


def test_next_sticker_increments_next_sticker_number():
    # Given the next sticker number is 10
    permit_manager.next_sticker_number = 10

    # When __next_sticker is called
    permit_manager._PermitManager__next_sticker()

    # Then the next sticker number should be 11
    assert permit_manager.next_sticker_number == 11


def test_issue_assigns_unique_sticker_numbers():
    # When permits are issued to two owners
    permit_manager.issue(
        owner_id="1234567", license_plate="ABC WXYZ", make="toyota", model="camry"
    )
    permit_manager.issue(
        owner_id="7654321", license_plate="CBA ZYXW", make="toyota", model="corolla"
    )

    # Then their sticker numbers should be unique
    assert permit_manager.get_sticker_number(
        "1234567"
    ) != permit_manager.get_sticker_number("7654321")


# Test 1
def test_can_park_permit_not_issued_is_false():
    # Given a permit has not been issued to an owner
    # Then the owner should not be able to park
    assert not permit_manager.can_park("ABC WXYZ")

# Test 2
def test_issue_enables_parking():
    # When a permit is issued to an owner
    permit_manager.issue(
        owner_id="1234567", license_plate="ABC WXYZ", make="toyota", model="camry"
    )

    # Then the owner should be able to park
    assert permit_manager.can_park("ABC WXYZ")

# Test 3
def test_issue_permit_already_issued_raises_valueerror():
    # Given a permit is issued to an owner
    permit_manager.issue(
        owner_id="1234567", license_plate="ABC WXYZ", make="toyota", model="camry"
    )

    # When trying to issue a permit again to the owner
    # Then a ValueError is raised
    with pytest.raises(ValueError):
        permit_manager.issue(
            owner_id="1234567", license_plate="ABC WXYZ", make="toyota", model="camry"
        )

# Test 4
def test_revoke_disables_parking():
    # Given a permit is issued to an owner
    permit_manager.issue(
        owner_id="1234567", license_plate="ABC WXYZ", make="toyota", model="camry"
    )

    # When the permit is revoked from the owner
    permit_manager.revoke("1234567")

    # Then the owner should not be able to park
    assert not permit_manager.can_park("ABC WXYZ")
