"""
One rotation is described per line with the following aspects:
The dial goes from 0 to 99
L indicates that the rotation should be towards LOWER numbers
R indicates that the rotation should be towards HIGHER numbers
The number indicates how MANY clicks to rotate in the designated direction (l-down, r-up)

Example 1:
Dial starts at 11
R8 --> 19
L19--> 0
L1--> 99
R1--> 0

Example 2:
Dial starts at 5
L10 --> 95
R5 --> 0


CHALLENGE:
1) Our dial starts at 50
2) We get the input of rotations
3) The password is the NUMBER of times that the dial ends up pointing at 0 after any series of rotations

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

    ## My rotate function will accurately return the current location as - is
    def rotate(self, input: DialInput) -> int:
        direction = input.distance if input.direction == 'R' else -input.distance

        self.current_location = (self.current_location + direction) % self.dial_length
        return self.current_location
    
