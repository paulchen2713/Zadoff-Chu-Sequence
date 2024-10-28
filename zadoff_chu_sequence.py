import cmath
import math
import numpy as np

def print_sequence(symbols):
    for i, symbol in enumerate(symbols, start=1):
        # Ensure symbol is a complex number
        symbol = complex(symbol.real, symbol.imag)
        r = abs(symbol)
        theta = cmath.phase(symbol)
        print(f'#{i:02d}  {symbol.real:+.4f} {symbol.imag:+.4f}j, r = {r:.1f}, theta = {theta:+.4f} = {math.degrees(theta):+.1f}')

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
    if math.gcd(n_zc, u) != 1:
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
    print_sequence(zc_sequence)

#01  +1.0000 +0.0000j, r = 1.0, theta = +0.0000 = +0.0
#02  +0.9511 -0.3090j, r = 1.0, theta = -0.3142 = -18.0
#03  +0.3090 +0.9511j, r = 1.0, theta = +1.2566 = +72.0
#04  -0.0000 -1.0000j, r = 1.0, theta = -1.5708 = -90.0
#05  -0.8090 -0.5878j, r = 1.0, theta = -2.5133 = -144.0
#06  -0.0000 -1.0000j, r = 1.0, theta = -1.5708 = -90.0
#07  +0.3090 +0.9511j, r = 1.0, theta = +1.2566 = +72.0
#08  +0.9511 -0.3090j, r = 1.0, theta = -0.3142 = -18.0
#09  +1.0000 +0.0000j, r = 1.0, theta = +0.0000 = +0.0
#10  -0.5878 +0.8090j, r = 1.0, theta = +2.1991 = +126.0


