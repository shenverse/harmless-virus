def test_safety():
    from utils.safety import is_safe_environment, no_file_modification
    assert is_safe_environment() == True
    assert no_file_modification() == True
    print("safety tests passed")

if __name__ == "__main__":
    test_safety()
