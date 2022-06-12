class Solution:
    def strongPasswordCheckerII(self, password: str) -> bool:
        # It has at least 8 characters.
        if len(password) < 8:
            return False

        # It contains at least one lowercase letter.
        if password.lower() == password:
            return False

        # It contains at least one uppercase letter.
        if password.upper() == password:
            return False

        # It contains at least one digit.
        if not (set(password) & set("0123456789")):
            return False

        # It contains at least one special character.
        if not (set(password) & set("!@#$%^&*()-+")):
            return False

        # It does not contain 2 of the same character in adjacent positions
        for ch in string.ascii_lowercase + "0123456789" + "!@#$%^&*()-+":
            if ch*2 in password:
                return False

        return True
