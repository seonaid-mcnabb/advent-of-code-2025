"""
One rotation is described per line with the following aspects:
The dial goes from 0 to 99
L indicates that the rotation should be towards LOWER numbers
R indicates that the rotation should be towards HIGHER numbers
The number indicates how MANY clicks to rotate in the designated direction (l-down, r-up)
"""

DIAL_LENGTH = 100
LEFT = 'L'
RIGHT = 'R'

class RotationInstruction:
    def __init__(self, rotation_input: list[str]):
        self.direction = str(rotation_input[0])
        self.distance = int(rotation_input[1:])

class Dial:
    def __init__(self, current_location: int):
        self.current_location = current_location
        self.dial_length = DIAL_LENGTH

    def count_zero_passes(self, rotation_instruction: RotationInstruction) -> int:
        zeros_passed = 0
        
        if rotation_instruction.distance > self.dial_length:
            remaining_distance = rotation_instruction.distance % self.dial_length
            equally_dividable = rotation_instruction.distance - remaining_distance
            zeros_passed = equally_dividable // self.dial_length

            if self.will_pass_zero(rotation_instruction.direction, self.current_location, remaining_distance):
                zeros_passed = zeros_passed + 1

            started_at_zero = self.current_location == 0
            completed_full_rotations = remaining_distance == 0

            return zeros_passed -1 if started_at_zero and completed_full_rotations else zeros_passed

        if self.will_pass_zero(rotation_instruction.direction, self.current_location, rotation_instruction.distance):
            zeros_passed = zeros_passed + 1

        return zeros_passed


    def will_pass_zero(self, rotation_direction, current_location, remaining_distance):
        if rotation_direction == LEFT:
            return current_location > 0 and remaining_distance > current_location
        else:
            distance_to_pass_zero = (self.dial_length - current_location) + 1
            return distance_to_pass_zero <= remaining_distance

    
    def rotate(self, rotation_instruction: RotationInstruction) -> int:
        direction = rotation_instruction.distance if rotation_instruction.direction == 'R' else -rotation_instruction.distance

        self.current_location = (self.current_location + direction) % self.dial_length
        return self.current_location

    
