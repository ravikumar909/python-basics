# List Operations in Python
    # Author: RAVI KUMAR

    # Creating lists
    fruits = ["apple", "banana", "mango", "orange", "grapes"]
    numbers = [5, 2, 8, 1, 9, 3, 7, 4, 6]

    print("=== List Operations ===")
    print(f"Original fruits list: {fruits}")
    print(f"First fruit: {fruits[0]}")
    print(f"Last fruit: {fruits[-1]}")
    print(f"Number of fruits: {len(fruits)}")

    # Adding and removing
    fruits.append("pineapple")
    print(f"\nAfter append: {fruits}")
    fruits.remove("banana")
    print(f"After remove banana: {fruits}")

    # Sorting
    numbers_sorted = sorted(numbers)
    print(f"\nOriginal numbers: {numbers}")
    print(f"Sorted numbers: {numbers_sorted}")
    print(f"Max: {max(numbers)}, Min: {min(numbers)}, Sum: {sum(numbers)}")

    # List comprehension
    squares = [x**2 for x in range(1, 6)]
    print(f"\nSquares of 1-5: {squares}")

    even_numbers = [x for x in range(1, 21) if x % 2 == 0]
    print(f"Even numbers 1-20: {even_numbers}")

    # Looping through list
    print("\nFruits list:")
    for i, fruit in enumerate(fruits, 1):
      print(f"  {i}. {fruit}")