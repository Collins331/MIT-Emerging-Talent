def fibonacci(n: int) -> int:
    """fib(n) =
    if n is 0 -> 0
    if n is 1 -> 1
    else -> fib(n-1) + fib(n - 2)
    """
    return n if n <= 1 else fibonacci(n - 1) + fibonacci(n - 2)


def fibonacci_list(max: int) -> list[int]:
    all = []

    for _ in range(0, max):
        all.append(fibonacci(len(all)))

    return all



if __name__ == "__main__":
    print(fibonacci_list(5))