"""
One rotation is described per line with the following aspects:
The dial goes from 0 to 99
L indicates that the rotation should be towards LOWER numbers
R indicates that the rotation should be towards HIGHER numbers
The number indicates how MANY clicks to rotate in the designated direction (l-down, r-up)

FUNCTIONALITIES I NEED:
1) A function that loops through the input list and on each iteration:
          RECEIVES two inputs: the current dial location, and rotation input
          RETURNS one output: the new dial location
          AND--> if the new dial location that's about to be returned is ZERO, we should add 1 to a 0-tracker
"""

"""
--If the input number is larger than the current location number, THEN it's guaranteed to pass through 0
 at some point and possibly several times
--If its 100 or above (the input) then we can look for an equation
--

if its between 25 and 75, another type of caluclation

if it's 25 or below, another type of caluclation
-- an R that's less than 75 will never pass through 0
-- an L that's less than 25 will never pass through 0

"""


class DialInput:
    def __init__(self, rotation_input: list[str]):
        self.direction = str(rotation_input[0])
        self.distance = int(rotation_input[1:])

class Dial:
    def __init__(self, current_location: int):
        self.current_location = current_location
        self.dial_length = 100

    def count_zero_passes(self, input: DialInput) -> int:
        zeros_passed = 0
        # Rule 1 -- if the input distance is greater than 100, we are guaranteed to pass zero at least once, whether we land on zero again or not
        if input.distance > 100:
            # in the case of input 200 and current location of 50
            remainder = input.distance % 100
            # 0
            equally_dividable = input.distance-remainder
            #200
            zeros_passed = equally_dividable // 100
            # 200//100 = 2

            if input.direction == 'L' and self.current_location > 0 and remainder > self.current_location:
                zeros_passed = zeros_passed + 1
                # add 1 to the final zeros passed count

            distance_to_pass_zero = (100 - self.current_location) + 1

            
            if input.direction == 'R' and distance_to_pass_zero <= remainder:
                zeros_passed = zeros_passed + 1

            # if the direction is right...     
            return zeros_passed if remainder > 0 or self.current_location > 0 else zeros_passed -1
        
        if input.direction == 'L' and input.distance > self.current_location and self.current_location > 0:
            if self.current_location > 0:
                zeros_passed = 1
            return zeros_passed

        if input.direction == 'R' and self.current_location > 0:
            distance_to_pass_zero = (100 - self.current_location) + 1
            if distance_to_pass_zero <= input.distance:
                zeros_passed = 1
                return zeros_passed

        return zeros_passed
    

    def rotate(self, input: DialInput) -> int:
        direction = input.distance if input.direction == 'R' else -input.distance

        self.current_location = (self.current_location + direction) % self.dial_length
        return self.current_location

    
