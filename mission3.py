from functools import reduce


# First, we created a function that checks the input of all! the functions in the mission
# This func can work with both 2 arguments and 3, and it can make the code much shorter
def check_arguments(lst, func1, func2=None):
    # check if the argument are indeed list and a function.
    if not isinstance(lst, list):
        raise TypeError('Please provide a list as the first argument')
    if not callable(func1):
        raise TypeError('The second argument must be a function')
    if func2 is not None and not callable(func2):
        raise TypeError('The third argument must be a function')
    if not lst:
        raise TypeError('The list is empty')


def count_if(lst, func):
    check_arguments(lst, func)
    count = 0
    for i in range(len(lst)):
        try:
            if func(lst[i]):
                count += 1
        except Exception:
            # Immediately returns 0 on any exception.
            return 0
    return count


def for_all(lst, func1, func2):
    # Here we check the arguments in the function we created
    check_arguments(lst, func1, func2)
    for i in range(len(lst)):
        try:
            func1(lst[i])
        except Exception:
            return False
        # Here we check the variable we changed immediately
        # we save a lot of time because if the first member in the list after implementation in func1 returns false in func2,
        # the 'for_all' func will stop running
        if not func2(lst[i]):
            return False
    return True


def for_all_red(lst, func1, func2):
    check_arguments(lst, func1, func2)
    try:
        # Here we used 'reduce' to get the final result from func1
        final = reduce(func1, lst)
    except Exception:
        return False
    return func2(final)


# We could solve this section in one line, but it was against what the lecturer said.
def there_exist(lst, n, func1):
    check_arguments(lst, func1)
    count = 0
    for i in range(len(lst)):
        try:
            if func1(lst[i]):
                count += 1
        except Exception:
            # Immediately returns 0 on any exception.
            return 0
    return count >= n