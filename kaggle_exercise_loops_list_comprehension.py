def has_lucky_number(nums):
    """Return true if list of numbers contains a lucky number divisible by 7"""
    return any([num % 7 == 0 for num in nums])




def elementwise_greater_than(L, thresh):
    """Return a list with the same length as L, where the value at index i is
    True if L[i] is greater than thresh, and False otherwise.
     >>>elementwise_greater_than([1, 2, 3, 4], 2)
    [False, False, True, True]
    """
    return [elem >thresh for elem in L]




def menu_is_boring(meals):
    """Given a list of meals served over some period of time, return True if the
    same meal has ever been served two days in a row, and False otherwise.
    """

    for i in range(len(meals) - 1):
        if meals[i] == meals[i + 1]:
            return True
    return False

def estimate_average_slot_payout(n_runs):
    """Run the slot machine n_runs times and return the average net profit per run.
    Example calls (note that return value is nondeterministic!):
    >>> estimate_average_slot_payout(1)
    -1
    >>> estimate_average_slot_payout(1)
    0.5
    """
    return sum([ele for ele in range(1,n_runs)])/n_runs



test1 =print(has_lucky_number([1, 2, 3, 4, 5, 6,7]))
test2 = print(elementwise_greater_than([1, 2, 3, 4], 2))
test3 = print(estimate_average_slot_payout(1000))
