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

    # When _next_sticker is called
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


# TODO: Write Test 1
def test_<TODO>():
    # Given a permit has not been issued to an owner
    # Then the owner should not be able to park
    # TODO

# TODO: Write Test 2
def test_<TODO>():
    # When a permit is issued to an owner
    # TODO

    # Then the owner should be able to park
    # TODO

# TODO: Write Test 3
def test_<TODO>():
    # Given a permit is issued to an owner
    # TODO

    # When trying to issue a permit again to the owner
    # Then a ValueError is raised
    # TODO

# TODO: Write Test 4
def test_<TODO>():
    # Given a permit is issued to an owner
    # TODO

    # When the permit is revoked from the owner
    # TODO

    # Then the owner should not be able to park
    # TODO
