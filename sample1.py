"""
This module provides a simple add function and demonstrates its usage.
"""
# Define a function named 'add' that takes two arguments, 'number1' and 'number2'.
def add(number1, number2):
    # The function returns the sum of 'number1' and 'number2'.
    """
    Return the sum of two numbers.
    
    Parameters:
        number1: The first number to add.
        number2: The second number to add.
    
    Returns:
        The sum of number1 and number2.
    """
    return number1 + number2

# Initialize the variable 'NUM1' with the value 4.
NUM1 = 4

# Initialize the variable 'NUM2' with the value 5.
NUM2 = 5

# Call the 'add' function with 'NUM1' and 'NUM2' as arguments and store the result in 'TOTAL'.
TOTAL = add(NUM1, NUM2)

# Print the result of adding 'NUM1' and 'NUM2' using an f-string.
RESULT_TEXT = (
    f"The sum of {NUM1} "
    f"and {NUM2} "
    f"is {TOTAL}"
)
print(RESULT_TEXT)
