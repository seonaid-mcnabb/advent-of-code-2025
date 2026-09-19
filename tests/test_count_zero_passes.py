import pytest
from Dial import Dial, DialInput

"""(0, "R787", 87, 7),
        (50, "R150", 0, 1),
        (0, "R100", 0, 0),
        (0, "R800", 0, 7),
        (1, "R200", 1, 2),
        (99, "R200", 99, 2),
        (50, "R200", 50, 2),
        (0,  "R200", 0, 1),
        (1,  "R200", 1, 2),
        (50, "R250", 50, 2),
        (50, "L250", 50, 0)"""

@pytest.mark.parametrize(
    "current_location, rotation_input, expected_location, expected_zeros_passed",
    [
        (16, "L824", 92, 9)
    ]
)
def test_input_over_100(current_location, rotation_input, expected_location, expected_zeros_passed):
    dial = Dial(current_location)
    dial_input = DialInput(rotation_input)

    zeros_passed = dial.count_zero_passes(dial_input)

    new_location = dial.rotate(dial_input)
    assert zeros_passed == expected_zeros_passed
    assert new_location == expected_location

@pytest.mark.parametrize(
    "current_location, rotation_input, expected_location, expected_zeros_passed",
    [
        (1, "L3", 98, 1),
        (23, "L22", 1, 0),
        (18, "L19", 99, 1),
        (24, "L24",0, 0),
        (50, "L52", 98, 1),
        (72, "L73", 99, 1),
        (72, "L72", 0, 0),
        (98, "L99", 99, 1),
        (98, "L98", 0, 0),
        (0, "L2",98, 0)
    ]
)
def test_left_rotation_zero_passes(current_location, rotation_input, expected_location, expected_zeros_passed):
    dial = Dial(current_location)
    dial_input = DialInput(rotation_input)

    zeros_passed = dial.count_zero_passes(dial_input)

    new_location = dial.rotate(dial_input)
    assert zeros_passed == expected_zeros_passed
    assert new_location == expected_location


@pytest.mark.parametrize(
    "current_location, rotation_input, expected_location, expected_zeros_passed",
    [
        (99, "R3", 2, 1),
        (80, "R21", 1, 1)
    ]
)
def test_right_rotation_zero_passes(current_location, rotation_input, expected_location, expected_zeros_passed):
    dial = Dial(current_location)
    dial_input = DialInput(rotation_input)

    zeros_passed = dial.count_zero_passes(dial_input)

    new_location = dial.rotate(dial_input)
    assert zeros_passed == expected_zeros_passed
    assert new_location == expected_location
