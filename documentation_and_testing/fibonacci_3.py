def fibonnaci_list(max: int) -> list[int]:
    if max == 0:
        return []
    if max == 1:
        return [0]

    # you need at least 2 values to add together
    fib_list = [0,1]

    # stop when your list is as long as the `max` argument
    while len(fib_list) < max:
        # add the previous two values to calculate the next
        next_number = fib_list[-1] + fib_list[-2]
        fib_list.append(next_number)

    return fib_list

if __name__ == "__main__":
    print(fibonnaci_list(5))