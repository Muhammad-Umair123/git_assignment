import numpy as np

def basic():
    # Create a rank 1 ndarray that only contains integers
    a = np.array([1, 2, 3])  
    print(type(a))            # Prints "<type 'numpy.ndarray'>"
    print(a.shape)            # Prints "(3,)"
    print(a[0], a[1], a[2])   # Prints "1 2 3"
    a[0] = 5                  # Change an element of the ndarray
    print(a)                  # Prints "[5, 2, 3]"

    # Create a rank 2 ndarray that only contains integers
    b = np.array([[1,2,3],[4,5,6]])   
    print(b.shape)                     # Prints "(2, 3)"
    print(b[0, 0], b[0, 1], b[1, 0])   # Prints "1 2 4"

    # Create a 2x2x2 array of all zeros
    c = np.zeros((2,2,2))


basic()