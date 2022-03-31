'''models = [{'make':'Nokia', 'model':216, 'color':'Black'}, {'make':'Mi Max', 'model':2, 'color':'Gold'},
          {'make':'Samsung', 'model': 7, 'color':'Blue'}]
print("Original list of dictionaries :")
print(models)
sorted_models = sorted(models, key = lambda x: x['color'])
print("\nSorting the List of dictionaries :")
print(sorted_models)'''

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# returns True if number is even
def check_even(number):
    if number % 2 == 0:
          return True
    return False
# Extract elements from the numbers list for which check_even() returns True
even_numbers_iterator = filter(check_even, numbers)
# converting to list
even_numbers = list(even_numbers_iterator)
print(even_numbers)
# Output: [2, 4, 6, 8, 10]

print(id(numbers))

