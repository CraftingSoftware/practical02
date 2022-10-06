"""
Manage permits for parking.
"""


class PermitManager:
    def __init__(self):
        self.next_sticker_number = 0
        self.permits = dict()

    def __next_sticker(self):
        """
        Increment the next sticker number and return the current sticker number.
        """
        sticker = self.next_sticker_number
        self.next_sticker_number += 1
        return sticker

    def issue(self, owner_id, license_plate, make, model):
        """
        Issue the owner a permit.

        Args:
            owner_id: Allegheny ID of the owner.
            license_plate: License plate number of the owner's car.
            make: Make of the owner's car.
            model: Model of the owner's car.

        Returns:
            The sticker number for the owner.

        Raises:
            ValueError: When a permit has already been issued to the owner.
        """
        # Raise a ValueError if permit has already been issued to owner
        if owner_id in self.permits:
            raise ValueError("A permit has already been issued to owner.")

        # If permit not yet issued, issue it
        self.permits[owner_id] = {
            "license_plate": license_plate,
            "make": make,
            "model": model,
            "sticker_number": self.__next_sticker(),
        }
        return self.permits[owner_id]["sticker_number"]

    def revoke(self, owner_id):
        """
        Revoke an owner's permit.

        Args:
            owner_id: Allegheny ID of the owner.

        Raises:
            KeyError: When a permit for the owner does not exist.
        """
        try:
            # Try removing the permit using the owner_id as the key
            self.permits.pop(owner_id)
        except (KeyError):
            # Catch the KeyError raised by .pop when owner_id is not a key and raise another KeyError describing the failed revocation.
            raise KeyError(
                f"A permit for the owner with Allegheny ID {owner_id} does not exist, so a permit cannot be revoked."
            )

    def can_park(self, license_plate):
        """
        Check if the owner with the license plate number has been issued a permit.

        Args:
            license_plate: License plate number to check.

        Returns:
            True if the owner of the license plate number has been issued a permit, False otherwise.
        """
        for permit in self.permits.values():
            if permit["license_plate"] == license_plate:
                return True
        return False

    def get_sticker_number(self, owner_id):
        """
        Get the sticker number for an owner.

        Args:
            owner_id: Allegheny ID of the owner.

        Returns:
            The sticker number for the owner.
        """
        return self.permits[owner_id]["sticker_number"]
