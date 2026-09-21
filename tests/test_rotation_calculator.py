import pytest
from Dial import Dial, RotationInstruction

@pytest.mark.parametrize(
    "current_location, rotation_input, expected_location",
    [
        (50, "R10", 60),
        (50, "L20", 30),
        (0, "L1", 99),
        (99, "R2", 1),
        (50, "R890", 40)
    ]
)
def test_single_rotation(current_location, rotation_input, expected_location):
    dial = Dial(current_location)
    dial_input = RotationInstruction(rotation_input)
    new_location = dial.rotate(dial_input)
    assert new_location == expected_location


def test_rotate_dial_with_multiple_inputs():
    rotation_inputs = ["R20", "L10", "R80"]
    dial = Dial(50)
    for input in rotation_inputs:
        dial_input = RotationInstruction(input)
        dial.rotate(dial_input)

    location = dial.current_location
    assert location == 40