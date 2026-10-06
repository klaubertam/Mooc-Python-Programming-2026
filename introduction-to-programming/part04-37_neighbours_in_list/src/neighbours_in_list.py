def longest_series_of_neighbours(numbers):
    if len(numbers) <= 1:
        return len(numbers)
    max_length = 1 
    current_length = 1
    for i in range(len(numbers) - 1):
        if abs(numbers[i + 1] - numbers[i]) == 1:
            current_length += 1
        else:
            if current_length > max_length:
                max_length = current_length
            current_length = 1
    if current_length > max_length:
        max_length = current_length
    return max_length