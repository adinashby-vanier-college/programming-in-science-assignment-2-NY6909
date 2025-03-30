# Function 1: Lists - Finding the Maximum and Second Maximum in a List
# This function takes a list of numbers as input and returns the maximum and second maximum values.
def max_two_in_list(numbers):
    """
    Find the maximum and second maximum values in a list.
    
    Args:
        numbers: A list of numbers
        
    Returns:
        A tuple (max_value, second_max_value) or (max_value, None) if only one element
    """
    if not numbers:
        return None, None
    
    if len(numbers) == 1:
        return numbers[0], None
    
    # Create a sorted copy of the list in descending order
    sorted_nums = sorted(numbers, reverse=True)
    
    # First element is the maximum
    max_val = sorted_nums[0]
    
    # Find the second maximum (first value that's different from max)
    second_max = None
    for num in sorted_nums[1:]:
        if num != max_val:
            second_max = num
            break
    
    return max_val, second_max

# Function 2: Lists - Removing Duplicates and Sorting
# This function takes a list of numbers and returns a sorted list with duplicates removed.
def remove_duplicates_and_sort(numbers):
    """
    Remove duplicates from a list and sort the result.
    
    Args:
        numbers: A list of numbers
        
    Returns:
        A sorted list with duplicates removed
    """
    # Convert to set to remove duplicates, then to list and sort
    return sorted(list(set(numbers)))
# Function 3: Single-Dimensional Arrays - Cumulative Sum
# This function takes an array (list) of numbers and returns a new list where each element is the cumulative sum of the previous elements.
def cumulative_sum(numbers):
    """
    Calculate the cumulative sum of a list.
    
    Args:
        numbers: A list of numbers
        
    Returns:
        A new list where each element is the cumulative sum of the previous elements
    """
    result = []
    total = 0
    
    for num in numbers:
        total += num
        result.append(total)
        
    return result

# Function 4: Two-Dimensional Arrays - Matrix Transpose
# This function takes a 2D list (matrix) and returns its transpose.
def transpose_matrix(matrix):
    """
    Transpose a 2D matrix.
    
    Args:
        matrix: A 2D list representing a matrix
        
    Returns:
        The transpose of the input matrix
    """
    # Get the number of rows and columns in the original matrix
    rows = len(matrix)
    cols = len(matrix[0]) if rows > 0 else 0
    
    # Create a new matrix with dimensions swapped
    result = [[0 for _ in range(rows)] for _ in range(cols)]
    
    # Fill the transposed matrix
    for i in range(rows):
        for j in range(cols):
            result[j][i] = matrix[i][j]
            
    return result
# Function 5: Slicing - Extracting Every Nth Element
# This function takes a list and a step value N and returns every Nth element.
def slice_every_nth(lst, n):
    """
    Extract every nth element from a list.
    
    Args:
        lst: A list of elements
        n: The step value
        
    Returns:
        A new list containing every nth element from the original list
    """
    return lst[::n]

# Function 6: Arithmetic Operations with Arrays - Dot Product
# This function takes two lists of the same length and returns their dot product.
def dot_product(list1, list2):
    """
    Calculate the dot product of two lists of the same length.
    
    Args:
        list1: First list of numbers
        list2: Second list of numbers
        
    Returns:
        The dot product of the two lists
    """
    return sum(a * b for a, b in zip(list1, list2))

# Function 7: Arithmetic Operations with Arrays - Matrix Multiplication
# This function takes two 2D lists (matrices) and returns their matrix product.
def matrix_multiplication(matrix1, matrix2):
    """
    Perform matrix multiplication on two 2D lists (matrices).
    
    Args:
        matrix1: First 2D list
        matrix2: Second 2D list
        
    Returns:
        The matrix product of the two input matrices
    """
    # Get dimensions
    rows1 = len(matrix1)
    cols1 = len(matrix1[0])
    rows2 = len(matrix2)
    cols2 = len(matrix2[0])
    
    # Initialize result matrix with zeros
    result = [[0 for _ in range(cols2)] for _ in range(rows1)]
    
    # Perform matrix multiplication
    for i in range(rows1):
        for j in range(cols2):
            for k in range(cols1):
                result[i][j] += matrix1[i][k] * matrix2[k][j]
                
    return result