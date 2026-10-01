"""
Story: Some incorrect product ids have been entered into the gift shop database

Input: A csv of id ranges
wherein 11 - 22, for example, is the first id, and 22 is the last id: TWO NUMBERS SEPARATED BY A DASH

What constitutes an invalid id?
--any id which is made only of some sequence of digits repeated twice (ie. 22 is invalid, but 221 is not)

Considerations:
--NONE of the numbers have leading zeros

Output:
--Examine the list of id ranges and extract all of the invalid ids from those ranges.
--> once that list is obtained, we must sum them all together.
"""

from tokenize import String


class GiftShopProduct:
    def __init__(self):
        self.name = "GiftShopProduct"

    def filter_invalid_ids(self, id_list: list[str]) -> list[int]:
        invalid_ids = []
        latest_invalid_number = 0

        for id in id_list:
            start, end = id.split('-')
            start_length = len(start)
            end_length = len(end)

            ## Immediate exit in the case that both numbers in range have odd digits
            if start_length % 2 != 0 and end_length % 2 != 0:
                return

            # If my length is four, I only want to grab half of each (start and end)
            start_first_half = int(start[:len(start) // 2])
            start_second_half = int(start[len(start) // 2:])
            end_first_half = int(end[:len(end) // 2])
            end_second_half = int(end[len(end) // 2:])
            
            # We should calculate this for the number of times we want to loop
            expected_steps = end_first_half - start_first_half
            # Edge cases when to add another step or subtract it
            start_digit_in_invalid_range = start_first_half >= start_second_half
            if start_digit_in_invalid_range:
                expected_steps += 1

            if end_first_half > end_second_half:
                expected_steps -=1


            power = len(str(start_first_half))
            if start_digit_in_invalid_range:
                latest_invalid_number = (start_first_half * 10 ** power) + start_first_half
                invalid_ids.append(latest_invalid_number)
            else:
                new_num = start_first_half + 1
                latest_invalid_number = new_num * 10 ** power + new_num
                invalid_ids.append(latest_invalid_number)

            increase_rate = 10 ** power + 1

            for i in range (expected_steps -1):
               latest_invalid_number = latest_invalid_number + increase_rate
               invalid_ids.append(latest_invalid_number)

            print(invalid_ids)

        return len(invalid_ids)

    def sum_invalid_ids(self, invalid_ids: list[int]) -> int:
        return 0
