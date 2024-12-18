# Find pi to to nth number


LIMIT = 20  # number of decimal places to calculate pi to

# other implemenations
# The Algorithms Python/maths/pi_monte_carlo_estimation.py
# The Algorithms Python/maths/pi_generator.py

# ask for user input OR accept a sys args (cli)
# use rich for butter STDOUT
# different method of calcualtion (show tqdm)


def pi_to_nth(limit=LIMIT):
    if limit == 0:
        return 0

    # XXX: does it make any difference to start from n to 1 (reverse summuation series!)
    return ((-1) ** (limit - 1)) / (2 * limit - 1) + pi_to_nth(limit - 1)


# FIXME:
# ((-1) ** limit) / (2 * limit + 1)
# ((-1) **( limit - 1)) / (2 * limit - 1)
# ((-1) ** (limit - 1)) / (2 * limit - 1)


def pi_to_nth2(limit):
    """
    Calculate pi to the nth term using Leibniz's formula recursively.

    :param limit: Number of terms to compute
    :return: Approximation of pi
    """
    if limit == 0:
        return 0

    # Recursive call for the sum of the first (limit-1) terms
    sum_previous = pi_to_nth2(limit - 1)

    # Calculate the current term
    current_term = ((-1) ** (limit - 1)) / (2 * limit - 1)

    # Add the current term to the sum of previous terms
    return sum_previous + current_term


if __name__ == "__main__":
    print(4 * pi_to_nth(500))
