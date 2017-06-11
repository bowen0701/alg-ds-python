def square_root(n, steps=20):
    """Newton's Method for approximating square root:
    
    - Initial guess: old_guess = n / 2
    - Iterations: new_guess = 1/2 * (old_guess + n / old_guess)
    """
    sqroot = n / 2
    for k in range(steps):
        sqroot = 1 / 2 * (sqroot + n / sqroot)
    return sqroot
