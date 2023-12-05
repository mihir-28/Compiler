# Loop Optimization


def split_loop_example(arr):
    n = len(arr)
    sum_even = 0
    sum_odd = 0

    for i in range(n):
        if i % 2 == 0:
            sum_even += arr[i]
        else:
            sum_odd += arr[i]

    return sum_even, sum_odd


def split_loop_optimized(arr):
    n = len(arr)
    sum_even = 0
    sum_odd = 0

    for i in range(0, n, 2):
        sum_even += arr[i]

    for i in range(1, n, 2):
        sum_odd += arr[i]

    return sum_even, sum_odd


arr = [1, 2, 3, 4, 5, 6]
original_result = split_loop_example(arr)
optimized_result = split_loop_optimized(arr)

print("Original Loop Result:", original_result)
print("Optimized Loop Result:", optimized_result)
