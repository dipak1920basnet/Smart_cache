class Util:
    def __init__(self):
        pass

    def binary_search_doc(timestamps: dict, time):
        """
        Return doc_id of particular time
        """
        result = []
        left_index = 0
        # sort the dict by value to perform binary search on values
        sorted_dict = sorted(
            [(key, value) for key, value in timestamps.items()], key=lambda x: x[1]
        )
        right_index = len(sorted_dict) - 1

        # Perform binary search on sorted_dict
        while left_index <= right_index:
            mid_val = left_index + (right_index - left_index) // 2
            get_time = sorted_dict[mid_val]
            if get_time[1] == time:
                result.append(get_time[0])
                # Check for duplicates on both sides

                # Search left side for duplicates
                # This is to handle the case where multiple documents have the same timestamp
                left = mid_val - 1
                while left >= 0 and sorted_dict[left][1] == time:
                    result.append(sorted_dict[left][0])
                    left -= 1

                # Search right side for duplicates
                # This is to handle the case where multiple documents have the same timestamp
                right = mid_val + 1
                while right < len(sorted_dict) and sorted_dict[right][1] == time:
                    result.append(sorted_dict[right][0])
                    right += 1
                break
            elif get_time[1] < time:
                left_index = mid_val + 1
            else:
                right_index = mid_val - 1
        return sorted(result)
