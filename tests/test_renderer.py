def test_text_data():
    from models.text_data import LOG_LINES, WARNING_POPUPS
    assert len(LOG_LINES) > 0
    assert len(WARNING_POPUPS) > 0
    print("text data tests passed")

if __name__ == "__main__":
    test_text_data()
