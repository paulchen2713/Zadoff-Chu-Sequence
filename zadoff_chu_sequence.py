from math import gcd
import numpy as np

def zadoff_chu_sequence(n_zc, u, q=0):
    """
    Generates a Zadoff-Chu sequence.

    Parameters:
    - n_zc (int): Length of the Zadoff-Chu sequence (must be a positive integer).
    - u (int): Root index of the Zadoff-Chu sequence (must satisfy 0 < u < n_zc and be coprime with n_zc).
    - q (int, optional): Cyclic shift parameter (default is 0).

    Returns:
    - numpy.ndarray: The generated Zadoff-Chu sequence as a NumPy array of complex numbers.

    Raises:
    - ValueError: If input parameters do not meet the required conditions.
    """

    # Validate input parameters
    if n_zc <= 0:
        raise ValueError('"n_zc" must be a positive integer.')
    if u <= 0 or u >= n_zc:
        raise ValueError('"u" must satisfy 0 < u < n_zc.')
    if gcd(n_zc, u) != 1:
        raise ValueError('"u" and "n_zc" must be coprime (gcd(n_zc, u) == 1).')

    # Determine whether n_zc is even or odd (cf = conjugate flag)
    cf = n_zc % 2

    # Generate sequence indices
    n = np.arange(n_zc)

    # Calculate the exponent for the Zadoff-Chu sequence
    exponent = -1j * np.pi * u * n * (n + cf + 2 * q) / n_zc

    # Generate the Zadoff-Chu sequence
    sequence = np.exp(exponent)

    return sequence

if __name__ == "__main__":
    zc_sequence = zadoff_chu_sequence(10, 7, 1)
    print(zc_sequence)


