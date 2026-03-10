from eva_data_analysis import text_to_duration, calculate_crew_size
import pytest

def test_text_to_duration_integer():
    """
    Test that text_to_duration function returns expected integer value when minutes are zero.
    """
    assert text_to_duration("10:00") == 10

def test_text_to_duration_float():
    """
    Test that text_to_duration function returns expected float value when minutes are not zero.
    """
    assert text_to_duration("10:20") == pytest.approx(10.33333333333333)

@pytest.mark.parametrize("input_value, expected_result", [
    ("Valentina Tereshkva;", 1),
    ("Judith Resnik; Sally Ride;", 2)
])
def test_calculate_crew_size(input_value, expected_result):
    """
    Test that calculate_crew_size returns expected crew size for typica crew entries
    """
    actual_result = calculate_crew_size(input_value)
    assert actual_result == expected_result

