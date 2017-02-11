"""Implement a function recursivly to get the desired
Fibonacci sequence value.
Your code should have the same input/output as the
iterative code in the instructions."""

compute_mapping = {}

def get_fib(position):

    if position in compute_mapping:
        return compute_mapping[position]

    if position <= 1:
        compute_mapping[position] = position
        return position
    else:
        result = get_fib(position - 1) + get_fib(position - 2)
        compute_mapping[position] = result
        return result

# Test cases
assert get_fib(0) == 0
assert get_fib(1) == 1
assert get_fib(2) == 1
assert get_fib(3) == 2
assert get_fib(4) == 3
assert get_fib(5) == 5
assert get_fib(6) == 8
assert get_fib(7) == 13
assert get_fib(8) == 21
assert get_fib(9) == 34
assert get_fib(10) == 55
assert get_fib(11) == 89
