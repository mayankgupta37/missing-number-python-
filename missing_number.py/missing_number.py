def missing_number(nums):
    n = len(nums)

    # Sum of numbers from 0 to n
    expected_sum = n * (n + 1) // 2

    # Sum of elements in the array
    actual_sum = sum(nums)

    # The missing number
    return expected_sum - actual_sum


# Example usage
if __name__ == "__main__":
    nums = [3, 0, 1]
    print("Missing Number:", missing_number(nums))