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


class IDHandler:
    def __init__(self):
        self.name = "GiftShopProduct"

    def filter_invalid_ids(self, id_list: list[str]) -> list[int]:
        invalid_ids = []

        for id in id_list:
            start, end = id.split('-')
            start_length = len(start)
            end_length = len(end)

            if start_length == end_length:
                section_1_start = start
                section_1_end = end
                invalid_ids.extend(self.process_sections(section_1_start, section_1_end))

            else:
                factor = 10 ** start_length
                largest_poss_num = factor -1
                section_1_start = start
                section_1_end = str(min(largest_poss_num, int(end)))
                section_2_start = str(int(section_1_end) + 1)
                section_2_end = end
                invalid_ids.extend(self.process_sections(section_1_start, section_1_end))
                invalid_ids.extend(self.process_sections(section_2_start, section_2_end))

        result = sum(invalid_ids)
        print(result)

        return result

    def process_sections(self, section_1_start, section_1_end):
                invalid_ids = []
                if len(section_1_start) % 2 != 0:
                     return []
                start_first_half = int(section_1_start[:len(section_1_start) // 2])
                start_second_half = int(section_1_start[len(section_1_start) // 2:])
                end_first_half = int(section_1_end[:len(section_1_end) // 2])
                end_second_half = int(section_1_end[len(section_1_end) // 2:])
        
                factor = len(str(start_first_half))
        
                # Establish the bounds
        
                1215 - 1420
                12 >= 15
                if start_first_half >= start_second_half:
                    first_valid_half = start_first_half
                else:
                    first_valid_half = start_first_half + 1
        
                14 <= 20
                if end_first_half <= end_second_half:
                    last_valid_half = end_first_half
                else:
                    last_valid_half = end_first_half - 1
        
                increase_rate = 10 ** factor + 1
        
                for half in range(first_valid_half, last_valid_half + 1):
                    invalid_id = half * increase_rate
                    invalid_ids.append(invalid_id)

                print(invalid_ids)

                return invalid_ids