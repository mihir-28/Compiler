# Loop Unrolling


def loop_unrolling_example(arr):
    n = len(arr)
    total = 0

    for i in range(n):
        total += arr[i]

    return total


def loop_unrolling_optimized(arr):
    n = len(arr)
    total = 0

    for i in range(0, n, 2):
        total += arr[i]

    for i in range(1, n, 2):
        total += arr[i]

    return total


arr = [1, 2, 3, 4, 5, 6]
original_result = loop_unrolling_example(arr)
optimized_result = loop_unrolling_optimized(arr)

print("Original Loop Result:", original_result)
print("Optimized Loop Result:", optimized_result)
