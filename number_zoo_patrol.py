def find_missing_number(numbers):
    n = len(numbers) 
    total = (n + 1)*(n + 2)/2
    sum_of_numbers = sum(numbers) 
    return total - sum_of_numbers 