from ..context import generate_password
import string

symbols = "!@#$%^&*()"

def test_password_symbols():
    result = generate_password()
    if not any([i for i in symbols]):
        assert 1 == 2, "There were no symbols within the password."
    assert result.lower() != result, "All of the characters were lowercase."
    assert result.upper() != result, "All of the characters were uppercase."


