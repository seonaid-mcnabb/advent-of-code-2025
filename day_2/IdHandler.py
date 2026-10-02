class IDHandler:
    def __init__(self):
        self.name = "ID_handler"

    def filter_and_sum_invalid_ids(self, id_range_list: list[str]) -> list[int]:
        invalid_ids = []

        for range in id_range_list:
            range_start, range_end = range.split('-')
            start_num_length = len(range_start)
            end_num_length = len(range_end)

            if start_num_length == end_num_length:
                start = range_start
                end = range_end
                invalid_ids.extend(self.process(start, end))

            else:
                next_digit_boundary = 10 ** start_num_length
                largest_poss_num = next_digit_boundary - 1
                start = range_start
                end = str(largest_poss_num)
                section_2_start = str(next_digit_boundary)
                section_2_end = range_end
                invalid_ids.extend(self.process(start, end))
                invalid_ids.extend(self.process(section_2_start, section_2_end))

        result = sum(invalid_ids)
        print(result)

        return result

    def process(self, start, end):
                invalid_ids = []
                range_has_odd_digits = len(start) % 2 != 0
                if range_has_odd_digits:
                     return []
                
                start_left = int(start[:len(start) // 2])
                start_right = int(start[len(start) // 2:])
                end_left = int(end[:len(end) // 2])
                end_right = int(end[len(end) // 2:])
        
                half_digit_count = len(str(start_left))
        
                # Establish the bounds
                if start_left >= start_right:
                    first_repeated_half = start_left
                else:
                    first_repeated_half = start_left + 1
        
                if end_left <= end_right:
                    last_repeated_half = end_left
                else:
                    last_repeated_half = end_left - 1
        
                repeated_half_multiplier = 10 ** half_digit_count + 1
        
                for repeated_half in range(first_repeated_half, last_repeated_half + 1):
                    invalid_id = repeated_half * repeated_half_multiplier
                    invalid_ids.append(invalid_id)

                return invalid_ids