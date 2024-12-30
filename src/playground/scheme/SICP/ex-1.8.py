# Correct Algorithm in Python


def in_delta_correct(guess1, guess2):
    return abs(guess1 - guess2) < 0.00001


def newton_improve_correct(guess, x):
    return (x / (guess**2) + 2 * guess) / 3


def newton_method_correct(guess, x):
    improved_guess = newton_improve_correct(guess, x)
    if in_delta_correct(guess, improved_guess):
        return guess  # why not returning improved_guess?
    # Answer: The stopping condition is when the difference between the guess and the improved guess is less than 0.00001.
    # This means that the guess is close enough to the improved guess, so we can return the guess.
    # If we returned the improved guess, the function would have to make one more recursive call to check if the stopping condition is met.
    # This is unnecessary, as the guess is already close enough to the improved guess to meet the stopping condition.
    # Therefore, we can return the guess without making an additional recursive call.
    # Example: If the guess is 1.73205 and the improved guess is 1.73205, the stopping condition is met, and we can return the guess.
    # If we returned the improved guess, the function would make one more recursive call to check if the stopping condition is met.
    # This is unnecessary, as the guess is already close enough to the improved guess to meet the stopping condition.

    else:
        return newton_method_correct(improved_guess, x)


def cube_root_correct(x):
    return newton_method_correct(1.0, x)


print(f"Correct Algorithm: Cube root of 27 is {cube_root_correct(27)}")


# =====================================


# Incorrect Algorithm in Python


def in_delta_incorrect(guess1, guess2):
    return abs(guess1 - guess2) < 0.00001


def newton_improve_incorrect(guess, x):
    return (x / (guess**2) + 2 * guess) / 3


def newton_method_incorrect(guess, x):
    if in_delta_incorrect(guess, x):
        return guess
    else:
        return newton_method_incorrect(newton_improve_incorrect(guess, x), x)


def cube_root_incorrect(x):
    return newton_method_incorrect(1.0, x)


# Uncommenting this will likely lead to an infinite recursion error
# because the stopping condition is never met.
# print(f"Incorrect Algorithm: Cube root of 27 is {cube_root_incorrect(27)}")
