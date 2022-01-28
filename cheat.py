# Madlen Hoffstadt, cheat() function for UvA Programming course

def cheat(exercise):
    """
    function takes assignment number as arguments and returns explanation of how to solve it
    """
    if exercise == "Q 1.2 P1":
        return ("my_numpy_array = np.array([5, 6, 1])")
    elif exercise == "Q 1.2 P10":
        return("create pandas dictionary; use multiplication and np.repeat () for repetition; then convert to pd data frame")
    elif exercise == "Q 2.2 P2":
        return("start with empty array, then for loop: increase b by 2 in each iteration and add to double_plus vector")
    elif exercise == "Q 2.2 P3":
        return("Returns error since global variable is used inside function; instead: define it as local inside the function")
    else:
        raise ValueError("we don't have the solution to this assignment")